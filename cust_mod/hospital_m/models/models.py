# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hospital_m(models.Model):
    _name = 'hospital_m.hospital_m'
    _rec_name = 'fname'
    _description = 'hospital_m.hospital_m'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # p_id = fields.Integer()
    fname = fields.Char(tracking=True)
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
    a_date = fields.Date(tracking=True)
    d_name = fields.Many2one('doctor.doctor', string='doctor name')
    d_speciality = fields.Selection(string="Speciality", related="d_name.d_speciality")
    state = fields.Selection([('patient_details', 'Patient_details'), ('appointment_status', 'Appointment_status')],
                             default="patient_details", string="status_bar")
    Medicine = fields.One2many('hospital.medicine', 'm2o_medicine', string='Medicines')
    s_count = fields.Integer(compute='associate_account')
    
    # description = fields.Text()
    
    # @api.onchange('fname')
    # def patient_count(self):
    #     print('patient counttttttttttttttttttt', len(self.fname))
    #     count = 0
    #     for fname in self:
    #         count += 1
    #     print('countttttttt', fname, count)
    #     for rec in self:
    #         count += 1
    #         appoinment_count = self.env['hospital_m.hospital_m'].search_count([('fname', '=', rec.id)])
    #         rec.appoinment_count = appoinment_count
    #
    #     return rec.appoinment_count
    
    
    def associate_account(self):
        for partner in self:
            partner.s_count = super(hospital_m, self).search_count([])
            
        
    def name_get(self):
        return [(record.id, f"{self.lname} -- {self.fname}") for record in self]
    
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
     
            
class Medicine_Patient(models.Model):
    _name = 'hospital.medicine'
    m2o_medicine = fields.Many2one('hospital_m.hospital_m')
    m_quantity = fields.Integer()
    m_price = fields.Float(string='Medicine Price')
    