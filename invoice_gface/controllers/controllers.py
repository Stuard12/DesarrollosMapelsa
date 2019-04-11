# -*- coding: utf-8 -*-
from odoo import http

# class InvoiceGface(http.Controller):
#     @http.route('/invoice_gface/invoice_gface/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_gface/invoice_gface/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_gface.listing', {
#             'root': '/invoice_gface/invoice_gface',
#             'objects': http.request.env['invoice_gface.invoice_gface'].search([]),
#         })

#     @http.route('/invoice_gface/invoice_gface/objects/<model("invoice_gface.invoice_gface"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_gface.object', {
#             'object': obj
#         })