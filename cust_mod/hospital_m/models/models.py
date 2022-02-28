# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hospital_m(models.Model):
    _name = 'hospital_m.hospital_m'
    _description = 'hospital_m.hospital_m'

    # p_id = fields.Integer()
    fname = fields.Char()
    lname = fields.Char()
    mobile = fields.Integer()
    email = fields.Char()
    dateofbirth = fields.Date()
    image = fields.Binary()
    address = fields.Text()
    blood_group = fields.Selection([('a','A'),('a+','A+'),('a-','A-'),
                                    ('b','B'),('b+','B+'),('b-','B-'),
                                    ('ab','AB'),('ab+','AB+'),('ab-','AB-'),
                                    ('o','O'),('o+','O+'),('o-','O-')])
    v_charge = fields.Float()
    disease = fields.Char()
    a_date = fields.Date()

    # description = fields.Text()



    @api.depends('value')
    def print(self):
        print('hello user')

    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
