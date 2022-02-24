from odoo import models, fields, api

class travel_management(models.TransientModel):

    _name = 'travel_management.wizard'

    id = fields.Integer()
    name = fields.Char()
    dob = fields.Date()
    email = fields.Char()

    def print(self):
        print('hello world')