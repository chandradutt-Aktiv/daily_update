from datetime import date

from odoo import fields, models, api


class InheritContacts(models.Model):
	"""
	This class shows age in contact
	"""
	_inherit = 'res.partner'
	_description = 'contacts'
	
	b_date = fields.Date(string='Birth Date')
	age = fields.Float(string='Age', compute='Calculate_Age')
	todays_date = fields.Date(default=date.today())
	
	@api.depends('b_date', 'todays_date')
	def Calculate_Age(self):
		"""
		calculate Age from date of birth
		"""
		if self.b_date:
			self.age = (self.todays_date - self.b_date).days // 365
		else:
			self.age = 0
