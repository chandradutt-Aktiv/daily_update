# -*- coding: utf-8 -*-
# from odoo import http


# class Clg(http.Controller):
#     @http.route('/clg/clg', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clg/clg/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clg.listing', {
#             'root': '/clg/clg',
#             'objects': http.request.env['clg.clg'].search([]),
#         })

#     @http.route('/clg/clg/objects/<model("clg.clg"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clg.object', {
#             'object': obj
#         })
