# -*- coding: utf-8 -*-
from openerp.addons.mail.tests.common import TestMail
from os.path import join as opj
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def open_mail(filename=''):
    f = open(opj(HERE, 'eml', filename), 'r')
    r = f.read()
    f.close()
    return r


class TestMailGW(TestMail):

    @classmethod
    def setUpClass(cls):
        super(TestMailGW, cls).setUpClass()
        cls.mail_inqueue = cls.registry('mail.incoming.queue')
        cls.res_partner = cls.registry('res.partner')
