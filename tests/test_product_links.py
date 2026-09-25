# -*- coding: utf-8 -*-
from psycopg2 import IntegrityError

from odoo.tests import Form, tagged
from odoo.tools import mute_logger

from .common import ProductLinksCommon


@tagged('post_install', '-at_install')
class TestProductLinks(ProductLinksCommon):

    def test_links_on_product_template(self):
        self.assertEqual(self.product_tmpl.link_ids, self.link_tds | self.link_sds)
        self.assertEqual(self.link_tds.product_tmpl_id, self.product_tmpl)

    def test_create_links_from_template(self):
        product = self.env['product.template'].create({
            'name': 'Test Primer',
            'link_ids': [
                (0, 0, {'name': 'Brochure', 'url': 'https://example.com/brochure.pdf'}),
                (0, 0, {'name': 'Video', 'url': 'https://example.com/video'}),
            ],
        })
        self.assertEqual(len(product.link_ids), 2)
        self.assertEqual(set(product.link_ids.mapped('name')), {'Brochure', 'Video'})
        self.assertEqual(product.link_ids.product_tmpl_id, product)

    def test_remove_link_from_template(self):
        self.product_tmpl.write({'link_ids': [(2, self.link_sds.id)]})
        self.assertEqual(self.product_tmpl.link_ids, self.link_tds)
        self.assertFalse(self.link_sds.exists())

    @mute_logger('odoo.sql_db')
    def test_name_required(self):
        with self.assertRaises(IntegrityError):
            self.env['product.links'].create({'url': 'https://example.com'})

    @mute_logger('odoo.sql_db')
    def test_url_required(self):
        with self.assertRaises(IntegrityError):
            self.env['product.links'].create({'name': 'No url'})

    def test_copy_link_keeps_product(self):
        link_copy = self.link_tds.copy()
        self.assertEqual(link_copy.product_tmpl_id, self.product_tmpl)
        self.assertEqual(link_copy.url, self.link_tds.url)
        self.assertIn(link_copy, self.product_tmpl.link_ids)

    def test_translated_fields(self):
        self.env['res.lang']._activate_lang('it_IT')
        self.link_tds.with_context(lang='it_IT').write({
            'name': 'Scheda tecnica',
            'url': 'https://example.com/it/tds.pdf',
        })
        self.assertEqual(self.link_tds.with_context(lang='en_US').name, 'Technical datasheet')
        self.assertEqual(self.link_tds.with_context(lang='en_US').url, 'https://example.com/tds.pdf')
        self.assertEqual(self.link_tds.with_context(lang='it_IT').name, 'Scheda tecnica')
        self.assertEqual(self.link_tds.with_context(lang='it_IT').url, 'https://example.com/it/tds.pdf')

    def test_product_form_links_tab(self):
        arch = self.env['product.template'].get_view(view_type='form')['arch']
        self.assertIn('name="links"', arch)
        self.assertIn('name="link_ids"', arch)

    def test_product_form_add_link(self):
        with Form(self.env['product.template']) as product_form:
            product_form.name = 'Test Sealant'
            with product_form.link_ids.new() as link:
                link.name = 'Declaration of performance'
                link.url = 'https://example.com/dop.pdf'
                link.alt_desc = 'DoP'
        product = product_form.save()
        self.assertEqual(len(product.link_ids), 1)
        self.assertEqual(product.link_ids.url, 'https://example.com/dop.pdf')
        self.assertEqual(product.link_ids.alt_desc, 'DoP')
