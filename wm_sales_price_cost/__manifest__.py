# -*- coding: utf-8 -*-
{
    'name': "Add selling price and cost to the purchase order.",
    'summary':"""
        Prix de vente et côut et le margin dans bon commandes 
    """,
    'description': """
    Adding the fields 'selling price' and 'cost' to the purchasing module within the command line.
    """,
    'author': 'WEBMANIA',
    "website": "https://www.webmania.ma",
    'category': 'Purchase Management',
    'version': '0.1',
    'depends': ['base', 'purchase'],
    'data': [
        #'security/ir.model.access.csv',
        'data/invoke_function.xml',
        'reports/report_bon_commande.xml',
        'reports/report_bon_commande_template.xml',
        'views/purchase_order_line_inherit.xml',
    ],

}