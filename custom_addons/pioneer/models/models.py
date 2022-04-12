# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pioneer(models.Model):
    _name = 'pioneer.pioneer'
    _description = 'pioneer.pioneer'
    # _inherit = 'res.partner'
    
    # delivery_address = fields.Many2one('res.partner', string='Delivery Address')
    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
