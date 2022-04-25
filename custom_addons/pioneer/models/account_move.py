from odoo import models, fields, api


class AccountMoveLine(models.Model):
	# _name = 'pioneer.pioneer'
	# _description = 'pioneer.pioneer'
	_inherit = 'account.move.line'
	
	delivery_address_id = fields.Many2one('res.partner', string='Delivery Address', domain=[("type", "=", "delivery")])
	vendor_id = fields.Many2one('res.partner', string='vendor',
	                            domain=[("type", "=", "contact"), ("supplier_rank", ">", 0)])
	vendor_price = fields.Float(string='vendor price')
	planned_gp = fields.Float(string='Planned GP')
	description = fields.Char(string='Description', compute='concatinate_description')
	
	@api.depends('delivery_address_id', 'product_id.description')
	def concatinate_description(self):
		result = []
		print('concatinateeeeeee ')
		for rec in self:
			# product_description =
			# delivery_address =
			rec.description = f"{rec.product_id and rec.product_id.description or ''} {rec.delivery_address_id and rec.delivery_address_id.name or ''}"
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
		vendor_ids = self.invoice_line_ids.mapped("vendor_id.id")
		print('idssssssssssss', vendor_ids)
		for vendor_id in vendor_ids:
			a = []
			for line in self.invoice_line_ids.filtered(lambda x: x.vendor_id.id == vendor_id):
				a.append((0, 0, {"product_id": line.product_id.id, "price_unit": line.vendor_price}))
			res = self.create({
				'move_type': 'in_invoice',
				'partner_id': vendor_id,
				'invoice_line_ids': a
			})
		# for rec in self:
		# 	records = self.create({
		# 		"move_type": "in_invoice",
		# 		"partner_id": rec.invoice_line_ids.vendor_id,
		# 	})
		# 	comp_id = self.invoice_line_ids.search([('vendor_id', '=', rec.vendor_id.id),
		# 	                                        ('id', 'in', [line.id for line in self.invoice_line_ids])])
		#
		# 	for line_id in comp_id:
		# 		print("line_id\n\n\n", line_id)
		# 		records.write({'invoice_line_ids': [(0, 0, {'product_id': line_id.product_id,
		# 		                                            'price_unit': line_id.vendor_price,
		# 		                                            'quantity': line_id.quantity,
		# 		                                            'delivery_address_id': line_id.delivery_address_id,
		# 		                                            'planned_gp': line_id.planned_gp})]})

# print('hello')
# ids = self.env.context.get('active_ids', [])
# print('idsssssssssssssssss', ids)
