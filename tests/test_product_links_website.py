# -*- coding: utf-8 -*-
from odoo.tests import HttpCase, new_test_user, tagged

from .common import ProductLinksCommon


@tagged('post_install', '-at_install')
class TestProductLinksWebsite(HttpCase, ProductLinksCommon):

    def test_product_page_shows_links(self):
        response = self.url_open(self.product_tmpl.website_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Resources', response.text)
        self.assertIn('href="https://example.com/tds.pdf"', response.text)
        self.assertIn('alt="Technical datasheet PDF"', response.text)
        self.assertIn('Technical datasheet', response.text)
        self.assertIn('href="https://example.com/sds.pdf"', response.text)
        self.assertIn('Safety datasheet', response.text)

    def test_product_page_shows_links_to_portal_user(self):
        new_test_user(
            self.env, login='link_portal_web', password='link_portal_web',
            groups='base.group_portal',
        )
        self.authenticate('link_portal_web', 'link_portal_web')
        response = self.url_open(self.product_tmpl.website_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('href="https://example.com/tds.pdf"', response.text)
        self.assertIn('href="https://example.com/sds.pdf"', response.text)

    def test_product_page_without_links(self):
        product = self.env['product.template'].create({
            'name': 'Product Without Links',
            'is_published': True,
        })
        response = self.url_open(product.website_url)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('<h3>Resources</h3>', response.text)
