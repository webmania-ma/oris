
from odoo import fields, models , api



class ResCompany(models.Model):
    _inherit = 'res.company'

    show_percentage = fields.Boolean(string="Pourcentage de Marge Commerciale", default=False)
    percentage = fields.Integer(string="Pourcentage %", default=10)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    calc_percentage_marge = fields.Boolean(related='company_id.show_percentage', readonly=False)
    percentage = fields.Integer(related='company_id.percentage', readonly=False)

