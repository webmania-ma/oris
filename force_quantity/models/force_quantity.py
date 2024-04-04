# -*- coding: utf-8 -*-

from odoo import models, fields, api


# from odoo.tools.float_utils import float_compare, float_is_zero, float_round


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    is_available = fields.Boolean('Make Available',
                                  help='The Force Availability button '
                                       'will show based on this field.')

    def action_force_availability(self):
        """Function for make quantity done."""
        for lines in self.move_lines:
            lines.quantity_done = lines.product_uom_qty
        self.is_available = True
        self.state = 'assigned'

    @api.depends('show_validate', 'immediate_transfer',
                 'move_ids.reserved_availability',
                 'move_ids.quantity_done')
    def _compute_show_qty_button(self):
        res = super(StockPicking, self)._compute_show_qty_button()
        if self.products_availability_state == 'late':
            self.show_set_qty_button = False
        return res


