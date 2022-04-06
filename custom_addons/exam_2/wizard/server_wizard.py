from odoo import models, fields


class ServerWizard(models.TransientModel):
    _name = "server.wizard"
    
    product = fields.Many2many('sale.order')
    qty = fields.Float(string='Qty')
    unit_price = fields.Float(string='Unit Price')
    
    def wizarddd(self):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', self._context("active_id"))
        