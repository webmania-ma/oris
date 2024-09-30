# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2021-Today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = "product.template"

    warehouse_quantity = fields.Char(compute='_get_warehouse_quantity', string='Quantité par entrepot')

    def _get_warehouse_quantity(self):
        for record in self:
            warehouse_quantity_text = ''
            product_id = self.env['product.product'].sudo().search([('product_tmpl_id', '=', record.id)])
            if product_id:
                quant_ids = self.env['stock.quant'].sudo().search([('product_id', '=', product_id[0].id), ('location_id.usage', '=', 'internal')])
                t_warehouses = {}
                for quant in quant_ids:
                    if quant.location_id:
                        if quant.location_id not in t_warehouses:
                            t_warehouses.update({quant.location_id: 0})
                        t_warehouses[quant.location_id] += quant.quantity

                # Get the reserved quantities
                move_line_ids = self.env['stock.move.line'].sudo().search([('product_id', '=', product_id[0].id), ('location_id.usage', '=', 'internal')])
                reserved_warehouses = {}
                for move_line in move_line_ids:
                    if move_line.location_id:
                        if move_line.location_id not in reserved_warehouses:
                            reserved_warehouses.update({move_line.location_id: 0})
                        reserved_warehouses[move_line.location_id] += move_line.product_uom_qty

                # Calculate the unreserved quantities
                unreserved_warehouses = {}
                for location in t_warehouses:
                    unreserved_quantity = t_warehouses[location] - reserved_warehouses.get(location, 0)
                    if location not in unreserved_warehouses:
                        unreserved_warehouses.update({location: 0})
                    unreserved_warehouses[location] += unreserved_quantity

                # Map locations to warehouses and aggregate quantities
                tt_warehouses = {}
                for location in unreserved_warehouses:
                    warehouse = False
                    location1 = location
                    while not warehouse and location1:
                        warehouse_id = self.env['stock.warehouse'].sudo().search([('lot_stock_id', '=', location1.id)])
                        if len(warehouse_id) > 0:
                            warehouse = True
                        location1 = location1.location_id
                    if warehouse_id:
                        if warehouse_id.name not in tt_warehouses:
                            tt_warehouses.update({warehouse_id.name: 0})
                        tt_warehouses[warehouse_id.name] += unreserved_warehouses[location]

                # Build the display string

                for item in tt_warehouses:
                    if tt_warehouses[item] != 0:
                        warehouse_quantity_text += ' ** ' + item + ': ' + str(tt_warehouses[item])
                        print(warehouse_quantity_text)
                record.warehouse_quantity = warehouse_quantity_text



