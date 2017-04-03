# -*- coding: utf-8 -*-
from .common import TestMailGW, open_mail
# from email.utils import formataddr
# from openerp.tools import mute_logger
# import socket

MAIL_TEMPLATE = """Return-Path: <whatever-2a840@postmaster.twitter.com>
To: {to}
Received: by mail1.openerp.com (Postfix, from userid 10002)
    id 5DF9ABFB2A; Fri, 10 Aug 2012 16:16:39 +0200 (CEST)
From: {email_from}
Subject: {subject}
MIME-Version: 1.0
Content-Type: multipart/alternative;
    boundary="----=_Part_4200734_24778174.1344608186754"
Date: Fri, 10 Aug 2012 14:16:26 +0000
Message-ID: {msg_id}
{extra}
------=_Part_4200734_24778174.1344608186754
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: quoted-printable

Please call me as soon as possible this afternoon!

--
Sylvie
------=_Part_4200734_24778174.1344608186754
Content-Type: text/html; charset=utf-8
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>=20
  <meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3Dutf-8" />
 </head>=20
 <body style=3D"margin: 0; padding: 0; background: #ffffff;-webkit-text-size-adjust: 100%;">=20

  <p>Please call me as soon as possible this afternoon!</p>

  <p>--<br/>
     Sylvie
  <p>
 </body>
</html>
------=_Part_4200734_24778174.1344608186754--
"""  # noqa

MAIL_TEMPLATE_PLAINTEXT = """Return-Path: <whatever-2a840@postmaster.twitter.com>
To: {to}
Received: by mail1.openerp.com (Postfix, from userid 10002)
    id 5DF9ABFB2A; Fri, 10 Aug 2012 16:16:39 +0200 (CEST)
From: Sylvie Lelitre <test.sylvie.lelitre@agrolait.com>
Subject: {subject}
MIME-Version: 1.0
Content-Type: text/plain
Date: Fri, 10 Aug 2012 14:16:26 +0000
Message-ID: {msg_id}
{extra}

Please call me as soon as possible this afternoon!

--
Sylvie
"""  # noqa

MAIL_MULTIPART_MIXED = """Return-Path: <ignasse.carambar@gmail.com>
X-Original-To: raoul@grosbedon.fr
Delivered-To: raoul@grosbedon.fr
Received: by mail1.grosbedon.com (Postfix, from userid 10002)
    id E8166BFACA; Fri, 23 Aug 2013 13:18:01 +0200 (CEST)
X-Spam-Checker-Version: SpamAssassin 3.3.1 (2010-03-16) on mail1.grosbedon.com
X-Spam-Level:
X-Spam-Status: No, score=-2.6 required=5.0 tests=BAYES_00,FREEMAIL_FROM,
    HTML_MESSAGE,RCVD_IN_DNSWL_LOW autolearn=unavailable version=3.3.1
Received: from mail-ie0-f173.google.com (mail-ie0-f173.google.com [209.85.223.173])
    by mail1.grosbedon.com (Postfix) with ESMTPS id 9BBD7BFAAA
    for <raoul@openerp.fr>; Fri, 23 Aug 2013 13:17:55 +0200 (CEST)
Received: by mail-ie0-f173.google.com with SMTP id qd12so575130ieb.4
        for <raoul@grosbedon.fr>; Fri, 23 Aug 2013 04:17:54 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20120113;
        h=mime-version:date:message-id:subject:from:to:content-type;
        bh=dMNHV52EC7GAa7+9a9tqwT9joy9z+1950J/3A6/M/hU=;
        b=DGuv0VjegdSrEe36ADC8XZ9Inrb3Iu+3/52Bm+caltddXFH9yewTr0JkCRQaJgMwG9
         qXTQgP8qu/VFEbCh6scu5ZgU1hknzlNCYr3LT+Ih7dAZVUEHUJdwjzUU1LFV95G2RaCd
         /Lwff6CibuUvrA+0CBO7IRKW0Sn5j0mukYu8dbaKsm6ou6HqS8Nuj85fcXJfHSHp6Y9u
         dmE8jBh3fHCHF/nAvU+8aBNSIzl1FGfiBYb2jCoapIuVFitKR4q5cuoodpkH9XqqtOdH
         DG+YjEyi8L7uvdOfN16eMr7hfUkQei1yQgvGu9/5kXoHg9+Gx6VsZIycn4zoaXTV3Nhn
         nu4g==
MIME-Version: 1.0
X-Received: by 10.50.124.65 with SMTP id mg1mr1144467igb.43.1377256674216;
 Fri, 23 Aug 2013 04:17:54 -0700 (PDT)
Received: by 10.43.99.71 with HTTP; Fri, 23 Aug 2013 04:17:54 -0700 (PDT)
Date: Fri, 23 Aug 2013 13:17:54 +0200
Message-ID: <CAP76m_V4BY2F7DWHzwfjteyhW8L2LJswVshtmtVym+LUJ=rASQ@mail.gmail.com>
Subject: Test mail multipart/mixed
From: =?ISO-8859-1?Q?Raoul Grosbedon=E9e?= <ignasse.carambar@gmail.com>
To: Followers of ASUSTeK-Joseph-Walters <raoul@grosbedon.fr>
Content-Type: multipart/mixed; boundary=089e01536c4ed4d17204e49b8e96

--089e01536c4ed4d17204e49b8e96
Content-Type: multipart/alternative; boundary=089e01536c4ed4d16d04e49b8e94

--089e01536c4ed4d16d04e49b8e94
Content-Type: text/plain; charset=ISO-8859-1

Should create a multipart/mixed: from gmail, *bold*, with attachment.

--
Marcel Boitempoils.

--089e01536c4ed4d16d04e49b8e94
Content-Type: text/html; charset=ISO-8859-1

<div dir="ltr">Should create a multipart/mixed: from gmail, <b>bold</b>, with attachment.<br clear="all"><div><br></div>-- <br>Marcel Boitempoils.</div>

--089e01536c4ed4d16d04e49b8e94--
--089e01536c4ed4d17204e49b8e96
Content-Type: text/plain; charset=US-ASCII; name="test.txt"
Content-Disposition: attachment; filename="test.txt"
Content-Transfer-Encoding: base64
X-Attachment-Id: f_hkpb27k00

dGVzdAo=
--089e01536c4ed4d17204e49b8e96--"""  # noqa

MAIL_MULTIPART_MIXED_TWO = """X-Original-To: raoul@grosbedon.fr
Delivered-To: raoul@grosbedon.fr
Received: by mail1.grosbedon.com (Postfix, from userid 10002)
    id E8166BFACA; Fri, 23 Aug 2013 13:18:01 +0200 (CEST)
From: "Bruce Wayne" <bruce@wayneenterprises.com>
Content-Type: multipart/alternative;
 boundary="Apple-Mail=_9331E12B-8BD2-4EC7-B53E-01F3FBEC9227"
Message-Id: <6BB1FAB2-2104-438E-9447-07AE2C8C4A92@sexample.com>
Mime-Version: 1.0 (Mac OS X Mail 7.3 (1878.6))

--Apple-Mail=_9331E12B-8BD2-4EC7-B53E-01F3FBEC9227
Content-Transfer-Encoding: 7bit
Content-Type: text/plain;
    charset=us-ascii

First and second part

--Apple-Mail=_9331E12B-8BD2-4EC7-B53E-01F3FBEC9227
Content-Type: multipart/mixed;
 boundary="Apple-Mail=_CA6C687E-6AA0-411E-B0FE-F0ABB4CFED1F"

--Apple-Mail=_CA6C687E-6AA0-411E-B0FE-F0ABB4CFED1F
Content-Transfer-Encoding: 7bit
Content-Type: text/html;
    charset=us-ascii

<html><head></head><body>First part</body></html>

--Apple-Mail=_CA6C687E-6AA0-411E-B0FE-F0ABB4CFED1F
Content-Disposition: inline;
    filename=thetruth.pdf
Content-Type: application/pdf;
    name="thetruth.pdf"
Content-Transfer-Encoding: base64

SSBhbSB0aGUgQmF0TWFuCg==

--Apple-Mail=_CA6C687E-6AA0-411E-B0FE-F0ABB4CFED1F
Content-Transfer-Encoding: 7bit
Content-Type: text/html;
    charset=us-ascii

<html><head></head><body>Second part</body></html>
--Apple-Mail=_CA6C687E-6AA0-411E-B0FE-F0ABB4CFED1F--

--Apple-Mail=_9331E12B-8BD2-4EC7-B53E-01F3FBEC9227--
"""  # noqa


class TestMailgateway(TestMailGW):

    def test_00_message_parse(self):
        """ Testing incoming emails parsing """
        cr, uid = self.cr, self.uid
        res = self.mail_thread.message_parse(cr, uid, MAIL_TEMPLATE_PLAINTEXT)
        self.assertIn(
            'Please call me as soon as possible this afternoon!',
            res.get('body', ''),
            'message_parse: missing text in text/plain body after parsing')
        res = self.mail_thread.message_parse(cr, uid, MAIL_TEMPLATE)
        self.assertIn(
            '<p>Please call me as soon as possible this afternoon!</p>',
            res.get('body', ''),
            'message_parse: missing html in multipart/alternative '
            'body after parsing')

        res = self.mail_thread.message_parse(cr, uid, MAIL_MULTIPART_MIXED)
        self.assertNotIn(
            'Should create a multipart/mixed: from gmail, *bold*, '
            'with attachment', res.get('body', ''),
            'message_parse: text version should not be in body after '
            'parsing multipart/mixed')
        self.assertIn(
            '<div dir="ltr">Should create a multipart/mixed: from gmail, '
            '<b>bold</b>, with attachment.<br clear="all"><div><br></div>',
            res.get('body', ''),
            'message_parse: html version should be in body after parsing '
            'multipart/mixed')

    def test_10_message_queue(self):
        """ Testing message in queue """
        cr, uid = self.cr, self.uid
        res = self.mail_inqueue.message_queue(
            cr, uid, 'crm.lead', MAIL_TEMPLATE_PLAINTEXT)
        self.assertEqual(res.model, 'crm.lead', 'Model must be crm.lead')
        self.assertTrue(res.delete_mail(), 'Delete message failed !!')

        res = self.mail_inqueue.message_queue(
            cr, uid, 'crm.lead', MAIL_MULTIPART_MIXED)
        self.assertEqual(res.model, 'crm.lead', 'Model must be crm.lead')
        self.assertEqual(res.email_subject, 'Test mail multipart/mixed',
                         'Subject is incorrect')
        self.assertTrue(res.delete_mail(), 'Delete message failed !!')

    def test_20_release_message_queue(self):
        """ Release the message in queue """
        cr, uid = self.cr, self.uid
        res = self.mail_inqueue.message_queue(
            cr, uid, 'crm.lead', MAIL_MULTIPART_MIXED)
        self.assertEqual(res.model, 'crm.lead', 'Model must be crm.lead')
        self.assertTrue(res.accept_mail(), 'Accept message failed !!')

    def test_30_store_mail_thread(self):
        """ Store 5 emails conversation with reply """
        cr, uid = self.cr, self.uid
        res = self.mail_inqueue.message_queue(
            cr, uid, 'res.partner', open_mail('mail1.eml'))
        self.assertEqual(res.model, 'res.partner', 'Model must be crm.lead')
        self.assertEqual(res.status, 'mailing', 'mail1.eml is a mailing')
        self.assertTrue(res.accept_mail(), 'Accept message failed !!')
        res = self.mail_inqueue.message_queue(
            cr, uid, 'res.partner', open_mail('mail2.eml'))
        self.assertTrue(res, 'Message 2 must be a reply to')

    def test_40_known_partner_mail(self):
        """ Known partner is directly integrate """
        cr, uid = self.cr, self.uid
        self.res_partner.create(cr, uid, {
            'name': 'IMMOTEP', 'email': 'immotep@pyramid.com'})
        res = self.mail_inqueue.message_queue(
            cr, uid, 'res.partner', open_mail('mail_known_partner.eml'))
        self.assertTrue(res, 'Mail is known, direct delivery')
        res = self.mail_inqueue.message_queue(
            cr, uid, 'res.partner', open_mail('mail_known_partner2.eml'))
        self.assertTrue(res, 'Mail is known Name+mail, direct delivery')

    def test_50_unsubscribe_mailing(self):
        """ Unsubscribe from mailing """
        cr, uid = self.cr, self.uid
        res = self.mail_inqueue.message_queue(
            cr, uid, 'res.partner', open_mail('mailing1.eml'))
        self.assertTrue(res.unsubscribe(), 'Unsubscribe message 1 failed !!')
