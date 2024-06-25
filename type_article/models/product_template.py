from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    locimport = fields.Selection([
        ('local', 'Local'),
        ('import', 'Import')
    ], string='Local / Import', default='local' , required=True)
