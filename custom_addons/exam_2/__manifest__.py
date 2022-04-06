# -*- coding: utf-8 -*-
{
    'name': "exam2",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "exam",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/server_wizard.xml',
        'views/server_wizard.xml',
        'views/inherit_contacts.xml',
        'views/inherit_settings.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'licence': 'LGPL-3',
    'application': True
}
