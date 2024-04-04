# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    user_default_warehouse = fields.Many2one('res.company', string="Warehouse", related='user_id.warehouse', readonly=True)

