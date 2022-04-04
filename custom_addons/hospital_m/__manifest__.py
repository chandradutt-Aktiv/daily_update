# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Hospital",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','mail','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/doctor_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'report/patient_details.xml',
        'report/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'licence':'LGPL-3',
    'application':True
}
