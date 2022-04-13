from odoo import models, fields, api


class AccountMoveLine(models.Model):
	# _name = 'pioneer.pioneer'
	# _description = 'pioneer.pioneer'
	_inherit = 'account.move.line'
	
	delivery_address = fields.Many2one('res.partner', string='Delivery Address')
	vendor = fields.Many2one('res.partner', string='vendor')
	vendor_price = fields.Float(string='vendor price')
	planned_gp = fields.Float(string='Planned GP')
	description = fields.Char(string='Description', compute='concatinate_description')
	
	@api.depends('delivery_address', 'product_id.description')
	def concatinate_description(self):
		result = []
		print('concatinateeeeeee ')
		for rec in self:
			# product_description =
			# delivery_address =
			rec.description = f"{rec.product_id and rec.product_id.description or ''} {rec.delivery_address and rec.delivery_address.name or ''}"
		# result.append(rec.description)
		print('notedddddddddd')
	
	# return result
	
	@api.onchange('vendor_price', 'price_unit')
	def calculategp(self):
		for rec in self:
			if rec.price_unit:
				rec.planned_gp = ((rec.price_unit - rec.vendor_price) / rec.price_unit) * 100
				print('planneddddddddddd', rec.planned_gp)
			else:
				rec.planned_gp = 0


class AccountMove(models.Model):
	_inherit = 'account.move'
	
	def test(self):
		print('hello')
