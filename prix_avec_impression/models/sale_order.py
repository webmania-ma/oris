from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sans_impression = fields.Boolean(string='Prix Sans impression')
    def update_unit_price(self):
        for order in self:
            for line in order.order_line:
                 if order.sans_impression:
                    line.price_unit = line.product_id.prix_vente_sans_impression
                 else:
                    line.price_unit = line.product_id.list_price
