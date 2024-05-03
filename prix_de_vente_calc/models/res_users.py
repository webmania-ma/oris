from odoo import api, models, fields, _


class User(models.Model):
    _inherit = ['res.users']
    activer_prix_update = fields.Boolean(string='Calculer Prix de Vente ', default=True)

