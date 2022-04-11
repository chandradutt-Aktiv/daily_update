from odoo import models, fields, api


class sale(models.Model):
    _inherit = "sale.order"

    ddaa = fields.Date()