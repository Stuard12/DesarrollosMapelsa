# -*- coding: utf-8 -*-

from odoo import models, fields, api

class configuracion(models.Model):
    _name = 'modulo_gface.modulo_gface'
    _description = 'prueba modulo'
    
    requestor = fields.Char(string='ID de cuenta', size=140, required=True)
    transaction = fields.Char(string='Tipo de transaccion', size=140, required=True)
    contry = fields.Char(string='Pais', size=140, required=True)
    entity = fields.Char(string='Nit', size=140, required=True)
    user = fields.Char(string='Usuario', size=140, required=True)
    userName = fields.Char(string='Nombre de usuario', size=140, required=True)
    establishmentCode = fields.Char(string='Codigo de establecimiento', size=140, required=True)
    electronicDevice = fields.Char(string='Dispositivo electronico', size=140, required=True)
    typeOfAsset = fields.Char(string='Tipo de activio', size=140, required=True)
    exchangeRate = fields.Char(string='tipo de cambio', size=140, required=True)
    regimenInformationIsr = fields.Char(string='ISR', size=140, required=True)
    electronicDeviceCreditNote = fields.Char(string='Dispositivo electronico de nota de credito', size=140, required=True)
    invoiceDescription = fields.Char(string='Informacion Adicional', size=250, required=True)
     
# class modulo_gface(models.Model):
#     _name = 'modulo_gface.modulo_gface'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100