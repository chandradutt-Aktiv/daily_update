from odoo import models, fields

class sales(models.Model):
    _inherit = 'res.partner'

    # id1= fields.Integer()
    
    
    # def name_get(self):
    #     return [(record.id, "%s:%s" % (record.name, record.phone)) for record in self]