# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hospital_m(models.Model):
    _name = 'hospital_m.hospital_m'
    _rec_name = 'fname'
    _description = 'hospital_m.hospital_m'
    _inherit = 'mail.thread', 'mail.activity.mixin'

    # p_id = fields.Integer()
    fname = fields.Char()
    lname = fields.Char()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    mobile = fields.Integer()
    email = fields.Char()
    dateofbirth = fields.Date()
    image = fields.Binary()
    address = fields.Text()
    blood_group = fields.Selection([('a', 'A'), ('a+', 'A+'), ('a-', 'A-'),
                                    ('b', 'B'), ('b+', 'B+'), ('b-', 'B-'),
                                    ('ab', 'AB'), ('ab+', 'AB+'), ('ab-', 'AB-'),
                                    ('o', 'O'), ('o+', 'O+'), ('o-', 'O-')])
    bg = fields.Char(readonly=True)
    v_charge = fields.Float()
    disease = fields.Char()
    a_date = fields.Date()
    doc_type = fields.Many2one('doctor.doctor', string='doctor type')
    doc_names = fields.Many2many('doctor.doctor', string='doctors')
    state = fields.Selection([('patient_details', 'Patient_details'), ('appointment_status', 'Appointment_status')],
                             default="patient_details", string="status_bar")
    # description = fields.Text()

    
    @api.onchange('blood_group')
    def bl_g(self):
        for rec in self:
            if(rec.blood_group):
                rec.bg = rec.blood_group

    @api.depends('value')
    def print(self):
        print('hello user')

    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100