# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    margin_par_commercial = fields.Float('Marge Commerciale')

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['margin_par_commercial'] = ", SUM(s.margin_par_commercial) as margin_par_commercial"
        groupby += ', s.margin_par_commercial'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)


