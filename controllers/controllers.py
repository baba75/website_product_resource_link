# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteProductResourceLink(http.Controller):
#     @http.route('/website_product_resource_link/website_product_resource_link/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_product_resource_link/website_product_resource_link/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_product_resource_link.listing', {
#             'root': '/website_product_resource_link/website_product_resource_link',
#             'objects': http.request.env['website_product_resource_link.website_product_resource_link'].search([]),
#         })

#     @http.route('/website_product_resource_link/website_product_resource_link/objects/<model("website_product_resource_link.website_product_resource_link"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_product_resource_link.object', {
#             'object': obj
#         })