# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductLinks(models.Model):
    _name = 'product.links'
    _description = 'Product resource link'
    
    name = fields.Char('Link label', required=True, translate=True)
    url = fields.Char('Link URL', required=True, translate=True)
    alt_desc = fields.Char('Alt Description', translate=True)
    product_tmpl_id = fields.Many2one('product.template', 'Related Product', copy=True)

class ProductTemplate(models.Model):
    _inherit = ["product.template"]
    _name = 'product.template'

    link_ids = fields.One2many(
        'product.links', 'product_tmpl_id', string='Resource link', help='URL link to resources like datasheets, brochures, white papers, etc...')