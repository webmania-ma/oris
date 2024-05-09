# -*- coding: utf-8 -*-
{
    'name': "Mise à jour  des prix de vente",
    'summary': """
        Mise à jour  des prix de vente""",
    'description': """
        Cette extension ajoute une fonctionnalité permettant de calculer automatiquement les prix de vente des produits en se basant sur leurs coûts et les préférences définies par l'utilisateur. Lorsque l'utilisateur sélectionne un produit dans une commande de vente,le prix de vente est automatiquement ajusté en fonction du coût du produit et des paramètres de configuration
    """,
    'author': "Webmania",
    'website': "https://www.webmania.ma",
    'category': 'Sales Management',
    'version': '0.1',
    'depends': ['base', 'sale_management', 'sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/view_res_partner.xml',
    ],
}