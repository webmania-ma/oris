from odoo import models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def product_id_change(self):
        if self.env.user.activer_prix_update:
            super(SaleOrderLine, self).product_id_change()
            fraction = 1.2
            if self.product_id:
                price_excluding_tax = self.product_id.list_price / fraction
                self.price_unit = self.product_id.standard_price + ((price_excluding_tax - self.product_id.standard_price) / 2)
        else:
            return super(SaleOrderLine, self).product_id_change()
