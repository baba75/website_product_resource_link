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

    'author': "Alberto Carollo",
    'website': "https://github.com/baba75",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '16.0.1.0.0',
    'license': "AGPL-3",

    # any module necessary for this one to work correctly
    'depends': ['base','website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
     "assets": {
        "web.report_assets_common": [
                                     '/website_product_resource_link/static/src/scss/prodlinks.scss',
                                     ],
    },
}