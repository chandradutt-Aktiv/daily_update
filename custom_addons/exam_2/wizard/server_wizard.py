from odoo import models, fields


class ServerWizard(models.TransientModel):
    _name = "server.wizard"
    
    order_line = fields.One2many('all.fields', 'sale_order')
    # qty = fields.Float(string='Qty')
    # unit_price = fields.Float(string='Unit Price')
    
    def wizarddd(self):
        order_lines = []
        for product in self.order_line.product_id:
            order_lines.append((0, 0, {'product_id': product.id}))
        
        for i in self._context.get('active_ids'):
            self.env['sale.order'].create({
                'partner_id': i,
                'order_line': order_lines
            })
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    
class AllFields(models.TransientModel):
    _name = 'all.fields'
    
    sale_order = fields.Many2one('server.wizard')
    product_id = fields.Many2one('product.product')
    qty = fields.Float(string='Qty', default=1)
    unit_price = fields.Float(string='unit_price')
    