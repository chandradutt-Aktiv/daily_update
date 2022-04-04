from odoo import fields, models, api


class server_change(models.Model):

	_inherit = 'res.partner'
	
	def writeeee(self):
		print('beforeeeeeeeeeeeeeeeeeeeeeee')
		context = self._context
		self.env[context["active_model"]].create({"name": "ABC"})
		
		# self.update({
		# 	'name': 'chandradutt',
		# 	'phone': '111111111',
		# 	'email': 'aaa@gmail.com'
		# })
		
	# def create_partner(self):
	# 	print('hello')
		