# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import tools
from odoo import fields, models, api

class SaleReport(models.Model):
    _inherit = 'sale.report'

    margin_par_commercial = fields.Float('Marge Commerciale', readonly=True)
    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['margin_par_commercial'] = ", s.margin_par_commercial / NULLIF((SELECT COUNT(DISTINCT product_id) FROM sale_order_line WHERE order_id = s.id), 0) AS margin_par_commercial"
        groupby += ', s.margin_par_commercial'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)





