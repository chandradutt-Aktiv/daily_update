# -*- coding: utf-8 -*-

from odoo import models, fields, api


class first_mod(models.Model):
    _name = 'first_mod.first_mod'
    _description = 'first_mod.first_mod'

    name = fields.Char()
    Id = fields.Integer()
    email = fields.Char()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    city=fields.Char()
    date=fields.Datetime()
    time=fields.Date()
    selection=fields.Selection([('hello','abcd'),('xyz','xyz')])
    addimage=fields.Binary()
    anhtml=fields.Html()
    gender=fields.Selection([('male','male'),('female','female')])
    

    @api.depends('Id')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.Id) / 100
