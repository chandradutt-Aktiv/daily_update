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
    addimage = fields.Binary()
    city = fields.Selection([('ahmedabad','Ahmedabad'),('mahesana','Mahesana'),('Bhavnagar','Bhavnagar')])
    boarding = fields.Char()
    destination = fields.Char()
    gender = fields.Selection([('male','Male'),('female','Female')])
    maritialstatus = fields.Selection([('married','Married'),('unmarried','Unmarrid')])
    invs = fields.Many2one('account.move', string='invoices')
    appointment_lines = fields.One2many('travel_management_pro.travel_management_pro', 'appointment_id', string='Appointment_Lines')
    stat = fields.Selection([('send','Send'),('sent','Sent'),('cancel','Cancel')])

    @api.depends('Id')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.Id) / 100



class travel_management_pro(models.Model):

    _name = 'travel_management_pro.travel_management_pro'
    _description = 'travel_management_pro.travel_management_pro'

    product_id = fields.Many2one('product.product', string='product')
    product_qty = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one('travel_management.travel_management', string='Appointment ID')