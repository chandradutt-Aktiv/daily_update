from odoo import models,fields

class clg_wizard(models.TransientModel):
    _name = 'wiz.wiz'

    fees = fields.Float()
    paid = fields.Selection([('paid','Paid'),('unpaid','Unpaid')])

    def print1(self):
        print('hello world')