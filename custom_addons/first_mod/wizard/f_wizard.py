from odoo import models,fields,api

class f_wizard(models.TransientModel):
    _name = "wiz.wiz"
    _rec_name = 'customer'
    customer = fields.Char()
    quotation_template = fields.Char()
    order_date = fields.Char()
    pricelist = fields.Char()
    payment_terms =fields.Char()

    @api.model
    def default_get(self, fields):
        """
        get the form data into wizard default
        """
        
        res = super(f_wizard, self).default_get(fields)
        customer = self.env['sale.order'].browse([self.env.context.get('active_id')])
        res['customer'] = customer.partner_id.name
        res['quotation_template'] = customer.partner_id.email
        res['order_date'] = customer.user_id.name
        res['pricelist'] = customer.user_id.phone
        res['payment_terms'] = customer.payment_term_id.name
        return res
    
    @api.model_create_multi
    def create(self, vals):
        print("CREATEEEEEEEEEEE", vals)
        res = super().create(vals)
        print("resresres", res)
        return res
    
    
    def playing(self):
        print('hello worldladkjfd;lsd;lasfkjdasf')