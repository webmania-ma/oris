from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    include_in_expenses = fields.Boolean(string="Payée")