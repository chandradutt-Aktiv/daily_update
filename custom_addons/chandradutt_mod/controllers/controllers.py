# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ChandraduttMod(http.Controller):
	@http.route('/chandradutt', auth='public', type='http', website=True)
	def chandradutt(self, **kw):
		contacts = request.env['res.partner'].sudo().search([])
		
		return request.render('chandradutt_mod.webdemo', {
			'contacts': contacts,
		})
	
	@http.route('/chandradutt/<model("res.partner"):con>', auth='public', type='http', website=True)
	def display_contacts(self, con):
		print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', con)
		return request.render('chandradutt_mod.dis_contact', {
			'details': con,
		})
	