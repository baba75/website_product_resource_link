# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase


class ProductLinksCommon(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product_tmpl = cls.env['product.template'].create({
            'name': 'Test Mortar',
            'is_published': True,
        })
        cls.link_tds = cls.env['product.links'].create({
            'name': 'Technical datasheet',
            'url': 'https://example.com/tds.pdf',
            'alt_desc': 'Technical datasheet PDF',
            'product_tmpl_id': cls.product_tmpl.id,
        })
        cls.link_sds = cls.env['product.links'].create({
            'name': 'Safety datasheet',
            'url': 'https://example.com/sds.pdf',
            'product_tmpl_id': cls.product_tmpl.id,
        })
