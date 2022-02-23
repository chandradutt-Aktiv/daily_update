from odoo import models, fields

class chandradutt_wizard(models.TransientModel):

    _name = 'chandradutt_wizard.wizard'

    id = fields.Integer()
    name = fields.Char()
    dob = fields.Date()
    email = fields.Char()