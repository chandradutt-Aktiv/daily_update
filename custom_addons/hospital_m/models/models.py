# -*- coding: utf-8 -*-
"""
Patient details
"""
from odoo import models, fields, api


class hospital_m(models.Model):
	"""
	Patient Details
	"""
	_name = 'hospital_m.hospital_m'
	_rec_name = 'fname'
	_description = 'hospital_m.hospital_m'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	
	# p_id = fields.Integer()
	fname = fields.Char(tracking=True)
	lname = fields.Char()
	gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
	mobile = fields.Integer()
	email = fields.Char()
	dateofbirth = fields.Date()
	image = fields.Binary()
	address = fields.Text()
	blood_group = fields.Selection([('a', 'A'), ('a+', 'A+'), ('a-', 'A-'),
	                                ('b', 'B'), ('b+', 'B+'), ('b-', 'B-'),
	                                ('ab', 'AB'), ('ab+', 'AB+'), ('ab-', 'AB-'),
	                                ('o', 'O'), ('o+', 'O+'), ('o-', 'O-')])
	bg = fields.Char(readonly=True)
	v_charge = fields.Float()
	disease = fields.Char()
	a_date = fields.Date(tracking=True)
	d_name = fields.Many2one('doctor.doctor', string='doctor name')
	d_speciality = fields.Selection(string="Speciality", related="d_name.d_speciality")
	state = fields.Selection([('patient_details', 'Patient_details'), ('appointment_status', 'Appointment_status')],
	                         default="patient_details", string="status_bar")
	Medicine = fields.One2many('hospital.medicine', 'm2o_medicine', string='Medicines')
	s_count = fields.Integer(compute='associate_account')
	# doc_name = fields.Many2one('doctor.doctor', string='doctor name')
	
	def associate_account(self):
		"""
		on smart button display count of records
		"""
		for partner in self:
			partner.s_count = super(hospital_m, self).search_count([])
	
	def send_mail_patient(self):
		print('Mailllllllllllllllllll')
		template_id = self.env.ref("hospital_m.mail_template_demo").id
		self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
		# self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
	
	# def name_get(self):
	# 	"""
	# 	getting first and last name
	# 	"""
	# 	if self.lname:
	# 		return [(record.id, f"{self.fname} -- {self.mobile}") for record in self]
	# 	else:
	# 		return [(record.id, f"{self.fname}") for record in self]
	
	@api.onchange('blood_group')
	def bl_g(self):
		"""
		get blood group in readonly field
		"""
		for rec in self:
			if rec.blood_group:
				rec.bg = rec.blood_group
	
	# @api.depends('value')
	# def print(self):
	# 	print('hello user')
	
	# def _value_pc(self):
	# 	for record in self:
	# 		record.value2 = float(record.value) / 100
	
	@api.model
	def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
		"""
		this is method is for
		search with customer email,name and phone number
		"""
		args = args or []
		domain = []
		print("insideeeeeeeeeeeeeeeeeeeeeeeeeee", self._context)
		if self._context.get('fname'):
			college = self.env['hospital_m.hospital_m'].browse(self._context.get('fname'))
			domain = args + ['|', ('fname', 'in', college.fname.ids), ('mobile', 'in', college.mobile.ids)]
		return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)


class Medicine_Patient(models.Model):
	"""
	shows Patient Medicines
	"""
	_name = 'hospital.medicine'
	m2o_medicine = fields.Many2one('hospital_m.hospital_m')
	m_quantity = fields.Integer()
	m_price = fields.Float(string='Medicine Price')
