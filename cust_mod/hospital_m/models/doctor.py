from odoo import fields,models

class doctor(models.Model):
    _name = 'doctor.doctor'
    _description = 'doctor.doctor'
    _rec_name = 'd_speciality'
    _inherit = 'mail.activity.mixin'
    
    img = fields.Binary()
    d_id = fields.Integer()
    d_name = fields.Char()
    d_dob = fields.Date()
    d_speciality = fields.Selection([('cardiologist','Cardiologist'),
                                     ('eye specialist','Eye Specialist'),
                                     ('family physician','Family physician'),
                                     ('plastic surgeons','Plastic Surgeons')])
    d_gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    patient_name = fields.Many2one('hospital_m.hospital_m',string='Patient_Name')
    date = fields.Datetime('Date current action'
                           , default=lambda self: fields.datetime.now())
    # check_list = fields.Integer(compute='check_list', string='progress',store=True)

    