# -*- coding: utf-8 -*-
{
    'name': "Default warehouse",

    # 'summary': """
    #     Short (1 phrase/line) summary of the module's purpose, used as
    #     subtitle on modules listing or apps.openerp.com""",

    'description': """
        This Odoo apps is helpful for the user who are looking forward to add warehouse according to the salesperson, It allows to set default warehouse for each salespersons, it makes sales person life easier to set default warehouse/inventory selection automatically when makes the sales order or quotation in Odoo. When you want that specific sales person sell goods from specific warehouse stock then you can use this odoo module, After installing this apps you can set default warehouse for each user and this warehouse automatically populates on quotation when quote creates using those users.
    """,

    'author': "Webmania",
    'website': "https://www.webmania.ma/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/warehouse_view.xml',
        'views/sale_order_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
