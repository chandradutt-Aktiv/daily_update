# -*- coding: utf-8 -*-

from odoo import models, fields, api


class travel_management(models.Model):

    _name = 'travel_management.travel_management'
    _description = 'travel_management.travel_management'


    Id = fields.Integer()
    name = fields.Char()
    dob = fields.Date()
    email = fields.Char()
    mobileNo = fields.Integer()
    city = fields.Selection([('ahmedabad','Ahmedabad'),('mahesana','Mahesana'),('Bhavnagar','Bhavnagar')])
    boarding = fields.Char()
    destination = fields.Char()
    gender = fields.Selection([('male','Male'),('female','Female')])
    maritialstatus = fields.Selection([('married','Married'),('unmarried','Unmarrid')])

    @api.depends('Id')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.Id) / 100
