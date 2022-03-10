from odoo import fields, models, api


class doctor(models.Model):
    _name = 'doctor.doctor'
    _description = 'doctor.doctor'
    # _rec_name = 'd_name'
    _inherit = ['mail.activity.mixin','mail.thread']
    
    img = fields.Binary()
    d_id = fields.Integer()
    d_name = fields.Char()
    d_dob = fields.Date()
    city = fields.Char()
    # ncity= fields.Many2one('doctor.doctor', string='city and name')
    d_speciality = fields.Selection([('cardiologist','Cardiologist'),
                                     ('eye specialist','Eye Specialist'),
                                     ('family physician','Family physician'),
                                     ('plastic surgeons','Plastic Surgeons')])
    
    d_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    fname = fields.Many2one('hospital_m.hospital_m')
    date = fields.Datetime('Date current action'
                           , default=lambda self: fields.datetime.now())
    # check_list = fields.Integer(compute='check_list', string='progress',store=True)
    
    
    @api.model
    def default_get(self, fields):
        res = super(doctor, self).default_get(fields)
        print('test.....')
        res['d_name'] = 'enter name'
        return res

    # @api.model
    # def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
    #     if args is None:
    #         args = []
    #     domain = args + ['|', '|', ('city', operator, name), ('name', operator, name)]
    #     return self._search(domain, limit=limit, access_rights_uid=name_get_uid)

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s - %s' % (rec.d_name, rec.city)))
            print(result)
        return result