# -*- coding: utf-8 -*-
{
    'name': "force_quantity",

    'summary': """
        Make goods available forcefully in the time of delivery 
               when there is an availability problem occurs.  """,

    'description': "This module will help you to make goods available"
                   "forcefully in the time of delivery and deliver goods to "
                   "the customer without any interruptions when there is an"
                   "availability problem occurs.Force availability button in "
                   "delivery/stock picking.Can change done quantities just by "
                   "a button click.",

    'author': "Web mania",
    'website': "https://www.webmania.ma/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'account', 'sale', 'stock'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/apply_quantity_view.xml',

    ],
    'images': ['static/description/webmanialogo.png'],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
