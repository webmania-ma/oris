# -*- coding: utf-8 -*-
# from odoo import http


# class DefaultWarehouse(http.Controller):
#     @http.route('/default_warehouse/default_warehouse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/default_warehouse/default_warehouse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('default_warehouse.listing', {
#             'root': '/default_warehouse/default_warehouse',
#             'objects': http.request.env['default_warehouse.default_warehouse'].search([]),
#         })

#     @http.route('/default_warehouse/default_warehouse/objects/<model("default_warehouse.default_warehouse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('default_warehouse.object', {
#             'object': obj
#         })
