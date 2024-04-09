# -*- coding: utf-8 -*-
{
    'name': "Add selling price and cost to the purchase order",
    'summary':"""
        Prix de vente et côut  dans bon commandes
    """,
    'description': """
          L'ajout de champs 'prix de vente' est le coût  sur le module  d'achat dans la ligne de commande
    """,
    'author': 'WEBMANIA',
    "website": "https://www.webmania.ma",
    'category': 'Purchase Management',
    'version': '0.1',

    'depends': ['base', 'purchase'],
    # always loaded
    'data': [
        'data/invoke_function.xml',
        'reports/report_bon_commande.xml',
        'reports/report_bon_commande_template.xml',
        'views/purchase_order_line_inherit.xml',


    ],
}
