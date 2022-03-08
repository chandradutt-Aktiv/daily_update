from odoo import fields, models, api


class doctor(models.Model):
    _name = 'doctor.doctor'
    _description = 'doctor.doctor'
    _rec_name = 'd_name'
    _inherit = ['mail.activity.mixin','mail.thread']
    
    img = fields.Binary()
    d_id = fields.Integer()
    d_name = fields.Char()
    d_dob = fields.Date()
    d_speciality = fields.Selection([('cardiologist','Cardiologist'),
                                     ('eye specialist','Eye Specialist'),
                                     ('family physician','Family physician'),
                                     ('plastic surgeons','Plastic Surgeons')])
    
    d_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    fname = fields.Many2one('hospital_m.hospital_m', string='Patient_Name')
    date = fields.Datetime('Date current action'
                           , default=lambda self: fields.datetime.now())
    # check_list = fields.Integer(compute='check_list', string='progress',store=True)
    
    # @api.model
    # def name_get(self):
    #     result = []
    #
    #     for rec in self:
    #         result.append((rec.d_name, '%s - %s' % (rec.fname, rec.d_gender)))
    #
    #     return result
    
    @api.model
    def default_get(self, fields):
        res = super(doctor, self).default_get(fields)
        print('test.....')
        res['d_name'] = 'enter name'
        return res


# class ProfitCenterInherited(models.Model):
#     _inherit = 'res.partner'
#
#
#     def name_get(self):
#         result = []
#
#
#         for rec in self:
#             result.append((rec.id, '%s - %s' % (rec.name, rec.email)))
#
#         return result