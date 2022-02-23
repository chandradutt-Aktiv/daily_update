#-*- coding: utf-8 -*-

from odoo import models, fields, api


class clg(models.Model):
    _name = 'clg.clg'
    _description = 'clg.clg'
    #_inherit = 'travel_management.travel_management'

    s_name = fields.Char()
    s_rollno = fields.Integer()
    s_age = fields.Integer()
    s_mobile = fields.Integer()
    s_email = fields.Char()
    s_image = fields.Binary()
    sex = fields.Selection([('male','Male'),('female','Female'),('transgender','Transgender')])
    fees = fields.Float()
    #city = fields.Selection()
    description = fields.Text()


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
