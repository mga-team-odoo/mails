# -*- coding: utf-8 -*-
# © 2016-2017 Christophe CHAUVET <christophe.chauvet@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Add incoming queue for unknown email",
    "version": "8.0.1.0.0",
    "author": "Christophe CHAUVET",
    "license": "AGPL-3",
    "category": "Social Network",
    "summary": """Allows to place incoming mail in queue,
                  an user can reject or accept it""",
    "depends": [
        'mail',
        'document',
    ],
    "data": [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'view/mail_routing.xml',
    ],
    "installable": False,
}
