from odoo import models, fields, api


class AccountMove(models.Model):

    _inherit = 'account.move'
    hrsft_ice = fields.Char(string="ICE", requirerd=True)


