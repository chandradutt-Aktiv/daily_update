# -*- coding: utf-8 -*-
# from odoo import http


# class FirstMod(http.Controller):
#     @http.route('/first_mod/first_mod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/first_mod/first_mod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('first_mod.listing', {
#             'root': '/first_mod/first_mod',
#             'objects': http.request.env['first_mod.first_mod'].search([]),
#         })

#     @http.route('/first_mod/first_mod/objects/<model("first_mod.first_mod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('first_mod.object', {
#             'object': obj
#         })
