from  odoo import fields, model

class ExcelReport(model.TransientModel):
	_name = 'excel.report'
	
	Employee = fields.Many2many('hr.employee', 'Excel_Report', 'rows', 'columns')
	start_date = fields.Date(string="Start Date")
	end_data = fields.Date(string='End Date')
	