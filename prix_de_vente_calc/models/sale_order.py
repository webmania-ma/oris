from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    price_unit = fields.Float('Unit Price', compute='_onchange_discount', required=True, default=0.0)

    @api.onchange('product_id', 'price_unit', 'product_uom', 'product_uom_qty', 'tax_id')
    def _onchange_discount(self):
        for line in self:
            if line.product_id and line.order_id.partner_id.activer_prix_update_partner:
                price_excluding_tax = line.product_id.list_price
                line.price_unit = line.product_id.standard_price + (
                        (price_excluding_tax - line.product_id.standard_price) / 2)
            else:
                line.price_unit = line.product_id.list_price if line.product_id else 0.0
