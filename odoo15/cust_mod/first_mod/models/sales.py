from odoo import models, fields, api

class sales(models.Model):
    _inherit = 'sale.order'
    
    mobile = fields.Integer()
    email = fields.Char()
    # date1 = fields.Date()

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for rec in self:
            rec.email = rec.partner_id.email
            rec.mobile = rec.partner_id.phone
    
    
    
    # @api.model
    # def _name_search(self, name, args=None, operator='=', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|', ('email', operator, name), ('name', operator, name)]
    #
    #     return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
    #
    #
    #
    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         result.append((rec.id, '%s - %s' % (rec.name, rec.phone)))
    #         print(result)
    #     return result
    