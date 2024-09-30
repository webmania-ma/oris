from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order'

    margin_par_commercial = fields.Monetary(
        string='Marge Commerciale',
        compute='_compute_margin_par_commercial',
        currency_field='currency_id',
        store=True
    )
    total_expense_amount = fields.Monetary(string="Autres Charges",
                                           currency_field='currency_id',
                                           readonly=True)
    def btn_calculate_charge(self):
        for order in self:
            expenses = self.env['hr.expense'].search([('included_sale_orders', '=', order.id),
                                                      ('state', '=', 'approved')])
            total_amount = sum(expense.total_amount for expense in expenses)
            order.total_expense_amount = total_amount
            
    @api.model
    def action_update_all_sale_order_calculations(self):
        sale_orders = self.search([('state', 'in', ['sale', 'done'])])
        for order in sale_orders:
            order.btn_calculate_charge()
        self.env.cr.commit()

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
            'params': {
                'title': 'Mise à jour terminée',
                'message': f'{len(sale_orders)} Ces calculs de commande de vente ont été mis à jour.',
                'sticky': False,
            }
        }


    @api.depends('margin', 'company_id.percentage', 'company_id.show_percentage', 'company_id.percentage_impression', 'company_id.show_percentage_impresssion', 'total_expense_amount', 'sans_impression')
    def _compute_margin_par_commercial(self):
        for order in self:
            exclue_charge = order.margin - order.total_expense_amount
            percentage = 1

            if order.sans_impression and order.company_id.show_percentage_impresssion:

                percentage = order.company_id.percentage_impression / 100.0

            elif not order.sans_impression and order.company_id.show_percentage:
                percentage = order.company_id.percentage / 100.0

            order.margin_par_commercial = exclue_charge * percentage
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        default['total_expense_amount'] = 0
        return super(SaleOrderLine, self).copy(default)




