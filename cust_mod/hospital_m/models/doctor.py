from odoo import fields,models

class doctor(models.Model):
    _name = 'doctor.doctor'
    _description = 'doctor.doctor'
    _rec_name = 'd_speciality'
    _inherit = 'mail.activity.mixin'
    
    d_id = fields.Integer()
    d_name = fields.Char()
    d_dob = fields.Date()
    d_speciality = fields.Selection([('cardiologist','Cardiologist'),
                                     ('eye specialist','Eye Specialist'),
                                     ('family physician','Family physician'),
                                     ('plastic surgeons','Plastic Surgeons')])
    d_gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    patient_name = fields.Many2one('hospital_m.hospital_m',string='student id')
    # check_list = fields.Integer(compute='check_list', string='progress',store=True)

    # project_progress = fields.Float(
    #     compute='_compute_project_progress_by_user', string='Project Progress')

    
    # def pro(self):
    #     check_list=int(input('enter value'))
    #     print(check_list)
    # print(pro(check_list))