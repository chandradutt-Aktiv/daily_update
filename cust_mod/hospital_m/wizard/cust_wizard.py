from odoo import fields,models

class cust_wizard(models.TransientModel):
    _name = 'cust_wizard'

    fname = fields.Char()
    lname = fields.Char()
    mobile = fields.Integer()
    email = fields.Char()
