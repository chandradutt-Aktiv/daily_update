from odoo import models,fields, api

class salex(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        res = super(salex, self).create(vals)
        if res.partner_id.customer_rank > 5:
            res.partner_id.write({'category_id': [(4, 8)]})  # 4 - Link, 8 - id of Best Customer tag
        return res