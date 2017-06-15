# -*- coding: utf-8 -*-
# © 2017 Christophe CHAUVET <christophe.chauvet@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": "New gateway to manage incomming mail",
    "version": "10.0.1.0.0",
    "author": "Christophe CHAUVET",
    "license": "LGPL-3",
    "category": "Social Network",
    "summary": """Additionnal API to manage API
    Better than the existing one that use admin account and hardocde password
    New API use a Token as Authentication, better to manage multiple database
    and instance
    """,
    "depends": [
        'mail',
        # 'document',
    ],
    "data": [],
    "installable": True,
}
