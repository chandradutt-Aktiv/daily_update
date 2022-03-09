from odoo import models, fields


class rental_type(models.Model):
    _name = 'rental.type'
    
    name = fields.Char()
    code = fields.Char()
    description = fields.Char()
