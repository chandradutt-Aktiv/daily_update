import datetime

from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date


class sales(models.Model):
    """
    jhgjhgjhg
    """
    _inherit = 'res.partner'
    
    # mobile = fields.Char()
    # email = fields.Char()
    
    # @api.onchange('partner_id')
    # def _onchange_partner_id(self):
    #     for rec in self:
    #         rec.email = rec.partner_id.email
    #         rec.mobile = rec.partner_id.phone
    
    @api.constrains('payment_term_id', 'partner_id')
    def _constraint_methods(self):
        for rec in self:
            if rec.payment_term_id.name != rec.partner_id.property_payment_term_id.name:
                raise UserError('Payment Term is not same')
            
    @api.model
    def _name_search(self, name, args=None, operator='=', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('email', operator, name), ('phone', operator, name)]

        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
    
    def name_get(self):
        # result = []
        # for rec in self:
        br = self.env['sale.order'].browse(['phone'])
        print('browseeeeeeeeeeeeeeee', br)
        #     result.append((rec.id, '%s ## %s' % (rec.name, rec.payment_term_id)))
        # return [(record.id, "%s : %s" % (record.name, record.ref)) for record in self]
        return [(record.id, f"{record.name} - {record.phone} +  {record.email}") for record in self]
        # return result


class Sale_Order_Inherited(models.Model):
    """
    Inheriting sale order new class
    """
    _inherit = 'sale.order'
    
    age = fields.Float(compute='Calculate_Age')
    Birth_Date = fields.Date(string='Birth Date', default=date.today())
    todays_date = fields.Date(default=date.today())
    
    def search_data(self):
        res = self.env['sale.order'].search([("payment_term_id","!=",False)]).read(['payment_term_id'])
        print(res, "---------------------------------")
        return res
    
    @api.depends('Birth_Date', 'todays_date')
    def Calculate_Age(self):
        """
        calculate Age from date of birth
        """
        print(type(self.todays_date), type(self.Birth_Date), "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2")
        if self.Birth_Date:
            self.age = (self.todays_date-self.Birth_Date).days // 365
        else:
            self.age = 0
    
    def action_confirm(self):
        """
        In saleorder Order lines are more than 3
        """
        print('action confirm calledddddddddddd')
        res = super(Sale_Order_Inherited, self).action_confirm()
        for rec in self:
           if len(rec.order_line) > 3:
                raise UserError('order lines needs less than 3')
        return res