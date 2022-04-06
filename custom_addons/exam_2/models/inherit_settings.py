from ast import literal_eval
from datetime import date, datetime
from odoo import fields, models, api


class InheritSettings(models.TransientModel):
	"""
	Inheriting main setting and adding two fields in setting
	"""
	_inherit = 'res.config.settings'
	
	module_mass_mailing = fields.Boolean("Test check")
	sale_details = fields.Many2many('sale.order', 'sale_settings', 'sale', 'settings',
	                                domain=[("date_order", ">=", datetime(date.today().year, date.today().month, 1))])
	
	@api.model
	def get_values(self):
		"""
		getting values of field
		"""
		res = super(InheritSettings, self).get_values()
		Values = self.env['ir.config_parameter']
		sale_details = Values.get_param('exam_2.sale_details')
		if sale_details:
			lines = [(6, 0, literal_eval(sale_details))]
			res.update({"sale_details": lines})
		return res
	
	@api.model
	def set_values(self):
		"""
		setting values of data
		"""
		res = super(InheritSettings, self).set_values()
		print(self.sale_details.ids, "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
		self.env['ir.config_parameter'].set_param(
			'exam_2.sale_details', self.sale_details.ids)
		return res
