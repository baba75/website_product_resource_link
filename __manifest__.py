# -*- coding: utf-8 -*-
{
    'name': "Website Product Resource Links",

    'summary': """
        Products resource links
        """,

    'description': """
        Extend the product with links to resources. You can add any url you like,
        e.g. link to product video, link to brochure, technical datasheets, and
        so on.
    """,

    'author': "Alberto Carollo - Ecobeton",
    'website': "https://www.ecobeton.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}