# -*- coding: utf-8 -*-
# from odoo import http


# class ChandraduttMod(http.Controller):
#     @http.route('/chandradutt_mod/chandradutt_mod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chandradutt_mod/chandradutt_mod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('chandradutt_mod.listing', {
#             'root': '/chandradutt_mod/chandradutt_mod',
#             'objects': http.request.env['chandradutt_mod.chandradutt_mod'].search([]),
#         })

#     @http.route('/chandradutt_mod/chandradutt_mod/objects/<model("chandradutt_mod.chandradutt_mod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chandradutt_mod.object', {
#             'object': obj
#         })
