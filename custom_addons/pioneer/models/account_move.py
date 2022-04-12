from odoo import models, fields, api


class AccountMove(models.Model):
    # _name = 'pioneer.pioneer'
    # _description = 'pioneer.pioneer'
    _inherit = 'account.move.line'

    delivery_address = fields.Many2one('res.partner', string='Delivery Address')
    vendor = fields.Many2one('res.partner', string='vendor')
    vendor_price = fields.Float(string='vendor price')
    planned_gp = fields.Float(string='Planned GP')
    description = fields.Char(string='Description')
    
    # @api.depends('vendor_price', 'price_unit')
    @api.onchange('vendor_price', 'price_unit')
    def calculategp(self):
        for rec in self:
            if rec.price_unit:
                rec.planned_gp = ((rec.price_unit - rec.vendor_price)/rec.price_unit)*100
                print('planneddddddddddd', rec.planned_gp)
            else:
                rec.planned_gp = 0
    