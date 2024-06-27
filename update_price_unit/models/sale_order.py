from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_unit = fields.Float('Unit Price', required=True, default=0.0)

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        self.update_price_unit()
        return res

    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        res = super(SaleOrderLine, self).product_uom_change()
        self.update_price_unit()
        return res

    @api.onchange('order_id.partner_id.activer_prix_update_partner')
    def onchange_activer_prix_update_partner(self):
        self.update_price_unit()

    def update_price_unit(self):
        for line in self:
            if line.product_id and line.order_id.partner_id.activer_prix_update_partner:
                price_excluding_tax = line.product_id.list_price
                line.price_unit = line.product_id.standard_price + (
                        (price_excluding_tax - line.product_id.standard_price) / 2)
            else:
                line.price_unit = line.product_id.list_price if line.product_id else 0.0

