from odoo import models,fields,api

class f_wizard(models.TransientModel):
    _name = "wiz.wiz"
    _rec_name = 'name'
    name = fields.Char()
    salary = fields.Integer()

    
    
    @api.model_create_multi
    def create(self, vals):
        print("CREATEEEEEEEEEEE", vals)
        res = super().create(vals)
        print("resresres", res)
        return res
    
    
    def playing(self):
        print('hello worldladkjfd;lsd;lasfkjdasf')