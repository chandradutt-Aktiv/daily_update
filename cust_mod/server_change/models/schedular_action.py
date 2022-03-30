from odoo import models, fields

class schedular_action(models.Model):
	_inherit = 'sale.order'
	
	def test(self):
		print('testttttttt calleddddddddddddd')
		# for rec in self:
		if self.state == 'draft':
			self.search([]).write({"state": "sent"})
				# rec.state = 'sent'
		