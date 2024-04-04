
from odoo import models, fields, api

class LastPrice(models.Model):
    _inherit = "product.template"
    new_price = fields.Boolean(string="Nouveau Prix De Vente", default=False)
    last_price = fields.Float(string="Ancien Prix De Vente", readonly=True)


class UpdatePrice(models.Model):
    _inherit = "purchase.order.line"
    list_price = fields.Float("Prix De Vente", readonly=False)

    @api.model
    def invoke_func_list_price(self):
        purchase_orders = self.env['purchase.order'].search([])
        for purchase in purchase_orders:
            for line in purchase.order_line:
                line.list_price = line.product_id.list_price

    @api.onchange('product_id')
    def product_related_fields(self):
        if self.product_id:
            self.list_price = self.product_id.list_price


class ConfirmInherit(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        for order in self:
            for line in order.order_line:
                product_data = {
                    "standard_price": line.price_unit,
                    "list_price": line.list_price,
                }
                current_product = self.env['product.product'].browse(line.product_id.id)
                if current_product.list_price != line.list_price:
                    product_data["new_price"] = True
                    product_data["last_price"] = current_product.list_price
                current_product.write(product_data)
        return super(ConfirmInherit, self).button_confirm()
