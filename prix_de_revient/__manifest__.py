# -*- coding: utf-8 -*-
{
    'name': "Add cost price in Purchase Order Line",
    'description': """
        Add cost price in Purchase Order Line
    """,
    'author': "Webmania",
    'website': "http://www.webmania.ma",
    'category': 'Purchase Management',
    'version': '0.1',
    'depends': ['base', 'purchase'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/view_purchase_order_line.xml',
    ],
}
