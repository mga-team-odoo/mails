# -*- coding: utf-8 -*-
# Copyright 2016-2017 Christophe CHAUVET, Mirounga
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, fields
from openerp.addons.mail import mail_thread as mt
from openerp.exceptions import Warning
from openerp.tools.translate import _
import email
import xmlrpclib
import re

EMAIL_STATUS = [
    ('normal', 'Normal'),
    ('spam', 'SPAM'),
    ('mailing', 'Mailing list'),
    ('unsubscribe', 'Unsubscribed'),
]


class MailIncomingQueue(models.Model):
    _name = 'mail.incoming.queue'
    _description = 'Store unknown incoming email'
    _rec_name = 'message'

    message = fields.Char(string='Message-Id',
                          help='Message-ID for this email')
    model = fields.Char(string='Model', size=64,
                        help='Model relate to this message')
    email_from = fields.Char(string='From', size=256, help='Sender')
    email_to = fields.Char(string='To', help='Recipient(s)')
    email_cc = fields.Char(string='CC', help='Copy')
    email_subject = fields.Char('Subject', help='Email Subject')
    email_date = fields.Datetime(string='Date', help='Email date')
    email_count_attachments = fields.Integer(
        string='Number of attachments',
        help='Number of attachments in this email')
    original = fields.Binary(string='Raw email', help='Email in eml format')
    status = fields.Selection(EMAIL_STATUS, string='Status',
                              help='Email status', default='normal')

    @api.multi
    def delete_mail(self):
        self.unlink()
        return True

    @api.multi
    def accept_mail(self):
        self.ensure_one()
        self.env['mail.thread'].message_process(self.model, self.original)
        self.unlink()
        return True

    @api.multi
    def unsubscribe(self):
        """
        If mail come from a mailing list, we can unsubscribe in one clic
        """
        self.ensure_one()
        unsub = None
        msg_txt = email.message_from_string(self.original)
        if msg_txt.get('List-Unsubscribe'):
            unsub = msg_txt.get('List-Unsubscribe').split(',')

        if unsub is None:
            raise Warning(_('No unsubscribe link found!!!'))

        ims = self.env['ir.mail_server']
        check_mail = False
        for el in unsub:
            el = self.clean_ref(el)
            if el.startswith('mailto:'):
                body = """Unsubscribe
This mail is automatically sent by odoo mail_routing
https://www.odoo.com/apps/modules/8.0/mail_routing/
"""
                mess = ims.build_email(
                    email_from=msg_txt.get('To'),
                    email_to=(el[7:],),
                    subject='Unsubscribe',
                    body=body,
                    references=msg_txt.get('Message-ID'),
                    headers={
                        'X-Mail-Routing-ID': self.id,
                        'X-Mail-From': self.email_from,
                        'X-Mail-Subject': self.email_subject,
                    }
                )
                check_mail = True
            elif el.startswith('http'):
                # Not implemented
                http_link = el

        if not check_mail and el:
            raise Warning(_('Unsubscribe link %s') % http_link)

        if not mess:
            raise Warning(_('No unsubscribe link found!'))

        ims.send_email(message=mess)
        self.status = 'unsubscribe'
        return True

    @api.model
    def clean_ref(self, reference):
        return reference.replace('<', '').replace('>', '')

    @api.model
    def message_queue(self, model, message, custom_values=None,
                      save_original=False, strip_attachments=False,
                      thread_id=None):

        if isinstance(message, xmlrpclib.Binary):
            message = str(message.data)

        if isinstance(message, unicode):
            message = message.encode('utf-8')

        msg_txt = email.message_from_string(message)
        msg = self.env['mail.thread'].message_parse(
            msg_txt, save_original=save_original)

        in_reply_to = mt.decode_header(msg_txt, 'In-Reply-To')
        if in_reply_to:
            # Search id message id has a message inside odoo
            self.env['mail.thread'].message_process(model, message)
            return True

        mails_from = re.findall(r"<[^>]+>", msg_txt.get('From'))
        part_obj = self.env['res.partner']
        for m in mails_from:
            p_ids = part_obj.search([('email', '=', self.clean_ref(m))])
            if p_ids:
                self.env['mail.thread'].message_process(model, message)
                return True

        # Search if message already integrate
        message_id = self.clean_ref(msg_txt.get('Message-ID'))
        queue_ids = self.search([('message', '=', message_id)])
        if queue_ids:
            return True

        mess_type = 'normal'
        if msg_txt.get('List-Post') or msg_txt.get('List-ID'):
            mess_type = 'mailing'
        elif msg_txt.get('X-Spam-Flag','') == 'YES':
            mess_type = 'spam'

        args = {
            'message': message_id,
            'model': model,
            'original': message,
            'email_from': msg.get('from'),
            'email_to': msg.get('to'),
            'email_cc': msg.get('cc'),
            'email_subject': msg.get('subject'),
            'email_count_attachments': len(msg.get('attachments', 0)),
            'email_date': msg.get('date'),
            'status': mess_type,
        }
        return self.create(args)

    @api.model
    def rpc_message_queue(self, model, message, custom_values=None,
                          save_original=False, strip_attachments=False,
                          thread_id=None):
        """
        In XMLRPC we cannot return a python object
        """
        trt = self.message_queue(
            model, message, custom_values, save_original,
            strip_attachments, thread_id)

        if not isinstance(trt, bool):
            return trt.id

        return True
