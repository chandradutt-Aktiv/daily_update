from odoo import fields, models, api


class server_change(models.Model):
	"""
	open wizard on server action and save data
	"""
	_inherit = 'res.partner'
	
	
	
	def writeeee(self):
		print('beforeeeeeeeeeeeeeeeeeeeeeee')
		# context = self._context
		# self.env[context["active_model"]].create({"name": "ABC"})
