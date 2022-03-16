#-*- coding: utf-8 -*-

from odoo import models, fields, api


class clg(models.Model):
    _name = 'clg.clg'
    _description = 'clg.clg'
    _rec_name = 's_name'
    # _inherit = 'travel_management.travel_management'

    name = fields.Char()
    s_name = fields.Char()
    s_rollno = fields.Integer()
    s_age = fields.Date()
    s_mobile = fields.Integer()
    s_email = fields.Char()
    s_image = fields.Binary()
    sex = fields.Selection([('male','Male'),('female','Female'),('transgender','Transgender')])
    fees = fields.Float()
    invo = fields.Many2one('utm.campaign',string='invoices')
    # city = fields.Selection([()])
    # description = fields.Text()
    mca = fields.Char()
    functions = fields.Selection([('navaratri','Navaratri'),('holi','Holi'),
                                  ('christmas','Christmas'),('alldays','Alldays')])

    state = fields.Selection([('to_send','To_send'),('sent','Sent'),
                              ('to_cancel','To_cancel'),('cancelled','Cancelled')], default="sent",string='status')

    aabb = fields.One2many('o2m.o2m','receipts',string='onemany')


    def students(self):
        return{
            'type':'ir.actions.act_window',
            'name':'print',
            'res_model':'wiz2.wiz2',
            'view_type':False,
            'view_mode':'tree,form',
            'target':'current',
        }

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class o2m(models.Model):
    _name = 'o2m.o2m'
    _description = 'o2m.o2m'

    dept = fields.Char()
    receipts = fields.Many2one('clg.clg', string='receipts')

