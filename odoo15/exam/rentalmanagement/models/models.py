# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rentalmanagement(models.Model):
    _name = 'rentalmanagement.rentalmanagement'
    # _description = 'rentalmanagement.rentalmanagement'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
    customer = fields.Many2one('res.partner', string='customer names')
    rental_type = fields.Many2one('rental.type', string='rental_Type')
    sdate = fields.Date(string='Start Date' ,required=True)
    edate = fields.Date(string='End Date', required=True)
    price = fields.Float()
    description = fields.Text()
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'),
                             ('approve', 'Approve'), ('cancel', 'Cancel')], default="waiting")
    
    
    @api.constrains('sdate','edate')
    def datechangeval(self):
        if(self.sdate > self.edate):
            raise 'start date cannot be greater than end date'

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
