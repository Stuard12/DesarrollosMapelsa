# -*- coding: utf-8 -*-
from odoo import http

# class ModuloGface(http.Controller):
#     @http.route('/modulo_gface/modulo_gface/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_gface/modulo_gface/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_gface.listing', {
#             'root': '/modulo_gface/modulo_gface',
#             'objects': http.request.env['modulo_gface.modulo_gface'].search([]),
#         })

#     @http.route('/modulo_gface/modulo_gface/objects/<model("modulo_gface.modulo_gface"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_gface.object', {
#             'object': obj
#         })