# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Warehouse(models.Model):
    _inherit = 'res.users'

    warehouse = fields.Many2one('res.company', 'Warehouse', required=True, index=True,
                                default=lambda self: self.env.company)



