from odoo import models, fields

class schedular_action(models.Model):
	_inherit = 'sale.order'
	
	def test(self):
		print('hello')
		