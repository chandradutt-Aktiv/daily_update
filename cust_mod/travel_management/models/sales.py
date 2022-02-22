from odoo import models, fields

class sales(models.Model):
    _inherit = 'sale.order'

    id1= fields.Integer()