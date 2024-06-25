from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"
    new_cost_price = fields.Float("Prix De revient")

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.new_cost_price = self.product_id.standard_price