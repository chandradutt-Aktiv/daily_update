from odoo import fields,models

class doctor(models.Model):
    _name = 'doctor.doctor'
    _description = 'doctor.doctor'
    _rec_name = 'd_speciality'
    
    d_id = fields.Integer()
    d_name = fields.Char()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    d_dob = fields.Date()
    d_speciality = fields.Selection([('cardiologist','Cardiologist'),
                                     ('eye specialist','Eye Specialist'),
                                     ('family physician','Family physician'),
                                     ('plastic surgeons','Plastic Surgeons')])
    
    