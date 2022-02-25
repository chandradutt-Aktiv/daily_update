from odoo import models,fields

class invoice(models.Model):
    _inherit = 'account.move'

    p_id =fields.Integer()