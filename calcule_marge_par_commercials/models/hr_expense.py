from odoo import models, fields, api

class HrExpense(models.Model):
    _inherit = 'hr.expense'

    @api.model
    def action_update_all_hr_expense_calculations(self):
        approved_expenses = self.search([
            ('state', '=', 'approved'),
            ('included_sale_orders', '!=', False)
        ])

        sale_orders = approved_expenses.mapped('included_sale_orders')
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
