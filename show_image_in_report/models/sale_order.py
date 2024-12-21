# -*- coding: utf-8 -*-


from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    show_images_in_report = fields.Boolean(
        string='Afficher les images dans le rapport',
        default=False,
        help='Si coché, les images des produits seront affichées dans le rapport de devis/commande'
    )
