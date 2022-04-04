# -*- coding: utf-8 -*-

from odoo import models, fields, api


class first_mod(models.Model):
    _name = 'first_mod.first_mod'
    _rec_name = 'name'
    _description = 'first_mod.first_mod'

    name = fields.Char()
    Id = fields.Integer()
    email = fields.Char()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    city = fields.Char()
    date = fields.Datetime()
    time = fields.Date()
    selection = fields.Selection([('hello','abcd'),('xyz','xyz')])
    addimage = fields.Binary()
    anhtml = fields.Html()
    gender = fields.Selection([('male', 'male'), ('female', 'female')])
    # customer_rank = fields.Many2many('sale.order')
    
    def openwizard(self):
        return self.env['ir.actions.act_window']._for_xml_id("first_mod.first_mod_added_wiz")

    @api.model
    def create(self, vals):
        rtn = super().create(vals)
        # rtn = self.env['ir.actions.act_window'].create(vals)
        return rtn
    
    # @api.model_create_multi
    # def create(self, vals):
    #     print("CREATEEEEEEEEEEE", vals)
    #     res = super(vals).create(vals)
    #     print("resresres", res)
    #     return res
    
    
    def unlink(self):
        print("unlinkunlinkunlink", self)
        res = super(self).unlink()
        print("unlinkkkkkkkkkk"
              "kkkk---res", res)
        return res

    def write(self, vals):
        print('write calleddddddddddddddd', vals)
        vals.update({
            'name': 'Chandradutt'
        })
        res = super().write(vals)
        print('resresresresresres',res)
        return res
    
    @api.depends('Id')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.Id) / 100
