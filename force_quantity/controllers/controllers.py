# -*- coding: utf-8 -*-
# from odoo import http


# class ForceQuantity(http.Controller):
#     @http.route('/force_quantity/force_quantity/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/force_quantity/force_quantity/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('force_quantity.listing', {
#             'root': '/force_quantity/force_quantity',
#             'objects': http.request.env['force_quantity.force_quantity'].search([]),
#         })

#     @http.route('/force_quantity/force_quantity/objects/<model("force_quantity.force_quantity"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('force_quantity.object', {
#             'object': obj
#         })
