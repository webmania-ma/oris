from odoo import models, fields , api



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_unit = fields.Float('Unit Price', compute='_onchange_discount', required=True, default=0.0)

    @api.onchange('product_id', 'price_unit', 'product_uom', 'product_uom_qty', 'tax_id')
    def _onchange_discount(self):
        if self.product_id and self.order_id.partner_id.activer_prix_update_partner:
            fraction = 1.2
            price_excluding_tax = self.product_id.list_price / fraction
            self.price_unit = self.product_id.standard_price + (
                                    (price_excluding_tax - self.product_id.standard_price) / 2)




