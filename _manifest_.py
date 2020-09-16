# -*- coding: utf-8 -*-
{
    'name': "Rental Cars",

    'summary': """Manage rentals""",

    'description': """
        Rental Cars module for managing car rentals:
            - Create
            - Read
            - Update
            - Delete
    """,

    'author': "Wilfredo Aleman",
    'website': "https://aleman.carrd.co/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}

