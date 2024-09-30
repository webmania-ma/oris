from odoo import fields, models , api



class ResCompany(models.Model):
    _inherit = 'res.company'

    show_percentage = fields.Boolean(string="Pourcentage de Marge Commerciale", default=False)
    percentage = fields.Integer(string="Pourcentage %", default=10)

    show_percentage_impresssion = fields.Boolean(string="Pourcentage de Marge Sans Impression", default=False)
    percentage_impression = fields.Integer(string="Pourcentage sans impression %", default=7)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    calc_percentage_marge = fields.Boolean(related='company_id.show_percentage', readonly=False)
    percentage = fields.Integer(related='company_id.percentage', readonly=False)

    calc_percentage_marge_impression = fields.Boolean(related='company_id.show_percentage_impresssion', readonly=False)
    percentage_impression = fields.Integer(related='company_id.percentage_impression', readonly=False)

