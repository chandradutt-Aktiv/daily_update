from odoo import models, fields

class sales(models.Model):
    _inherit = 'sale.order'

    date1 = fields.Date()
