from odoo import models,fields

class f_wizard(models.TransientModel):
    _name = "wiz.wiz"

    salary = fields.Integer()

    def playing(self):
        print('hello worldladkjfd;lsd;lasfkjdasf')