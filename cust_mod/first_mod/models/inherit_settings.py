"""
new class of inheriting setting
"""
from odoo import fields, models, api


class Inherit_Settings(models.TransientModel):
	"""
	Inheriting main setting and adding two fields in setting
	"""
	_inherit = 'res.config.settings'
	
	bool = fields.Boolean("Test check")
	html = fields.Html()
	
	is_active = fields.Boolean(string='Active', config_parameter='first_mod.active')
	
	@api.model
	def get_values(self):
		"""
		getting value on parameter on field
		"""
		res = super(Inherit_Settings, self).get_values()

		res['bool'] = self.env['ir.config_parameter'].get_param('first_mod.bool')
		res['html'] = self.env['ir.config_parameter'].get_param('first_mod.html')

		return res

	@api.model
	def set_values(self):
		"""
		setting value on parameter on field
		"""
		self.env['ir.config_parameter'].set_param('first_mod.bool', self.bool)
		self.env['ir.config_parameter'].set_param('first_mod.html', self.html)
		super(Inherit_Settings, self).set_values()
		