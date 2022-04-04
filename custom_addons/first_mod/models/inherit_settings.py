"""
new class of inheriting settings and adding fields into the settings
"""
from odoo import fields, models, api

class Inherit_Settings(models.TransientModel):
	"""
	Inheriting main setting and adding two fields in setting
	"""
	_inherit = 'res.config.settings'
	
	bool = fields.Boolean("Test check")
	html = fields.Html()
	m2o = fields.Many2one('res.company', config_parameter='config.partner')
	
	is_active = fields.Boolean(string='Active', config_parameter='first_mod.active')
	
	@api.model
	@api.onchange('bool')
	def get_values(self):
		"""
		getting values of field
		"""
		res = super(Inherit_Settings, self).get_values()
		res['bool'] = self.env['ir.config_parameter'].get_param('first_mod.bool')
		
		# if res['bool']:
		# 	res['m2o'] = self.env['ir.config_parameter'].get_param('first_mod.m2o')
		# else:
		# 	self.m2o = False
		return res
	
	@api.model
	def set_values(self):
		"""
		setting values of fields
		"""
		self.env['ir.config_parameter'].set_param(
			'first_mod.bool', self.bool)
		
		self.env['ir.config_parameter'].set_param('first_mod.bool', self.bool)
		self.env['ir.config_parameter'].set_param('first_mod.m2o', self.m2o.id)
		print("##################################", self.m2o.id)
		super(Inherit_Settings, self).set_values()
	