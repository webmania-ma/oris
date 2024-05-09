from odoo import api, models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    activer_prix_update_partner = fields.Boolean(string='Calculer Prix de Vente ')
