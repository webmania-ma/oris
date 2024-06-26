from odoo import api, fields, models


class Expense(models.Model):
    _inherit = "hr.expense"

    included_sale_orders = fields.Many2one('sale.order', string='Bon de commande',
                                           domain=[('state', 'in', ['done', 'sale']),
                                                   ('include_in_expenses', '=', True)],
                                           help="Select confirmed sale orders")
