from odoo import models, fields


class p_template(models.Model):
	_inherit = "product.template"
	
	is_rental = fields.Boolean()
	rental_type = fields.Many2one('rental.type', string="Type")
