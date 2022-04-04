from odoo import models, fields, api


class salex(models.Model):
    """
    Inherited Res Partner
    """
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        """
        Find a customer_rank field and check if customer rank
        is greater than 5 then add a new tag in category_id named
        'Best Customer'
        """
        print('tryingggggggggggggggg')
        # id = self.env['res.partner'].context('active_id')
        res = super(salex, self).create(vals)
        if res.partner_id.customer_rank > 5:
            best_cos = self.env.ref('clg.res_partner_category_best').id
            res.partner_id.write({'category_id': [(0, 0, {'name': 'best customer', 'color': 9})]})  # 4 - Link, 8 - id of Best Customer tag
        return res
    