# -*- coding: utf-8 -*-

from odoo import models, fields, api
class invoice(models.Model):
    _inherit = "invoice_gface.invoice_gface"
    
    date = fields.date(string='fecha')
    
# class invoice_gface(models.Model):
#     _name = 'invoice_gface.invoice_gface'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100