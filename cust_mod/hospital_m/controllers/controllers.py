# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalM(http.Controller):
#     @http.route('/hospital_m/hospital_m', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_m/hospital_m/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_m.listing', {
#             'root': '/hospital_m/hospital_m',
#             'objects': http.request.env['hospital_m.hospital_m'].search([]),
#         })

#     @http.route('/hospital_m/hospital_m/objects/<model("hospital_m.hospital_m"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_m.object', {
#             'object': obj
#         })
