from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    prix_vente_sans_impression = fields.Float(
        string='Prix de vente sans impression',
        required=True
    )

class ProductProduct(models.Model):
    _inherit = 'product.product'

    prix_vente_sans_impression = fields.Float(
           string='Prix de vente sans impression',
           related='product_tmpl_id.prix_vente_sans_impression',
           readonly=False
)