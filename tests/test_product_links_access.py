# -*- coding: utf-8 -*-
from odoo.exceptions import AccessError
from odoo.tests import new_test_user, tagged
from odoo.tools import mute_logger

from .common import ProductLinksCommon


@tagged('post_install', '-at_install')
class TestProductLinksAccess(ProductLinksCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.designer = new_test_user(
            cls.env, login='link_designer',
            groups='base.group_user,website.group_website_designer',
        )
        cls.public_user = cls.env.ref('base.public_user')
        cls.portal_user = new_test_user(cls.env, login='link_portal', groups='base.group_portal')
        cls.employee = new_test_user(cls.env, login='link_employee', groups='base.group_user')

    def test_designer_full_access(self):
        Links = self.env['product.links'].with_user(self.designer)
        link = Links.create({
            'name': 'Gallery',
            'url': 'https://example.com/gallery',
            'product_tmpl_id': self.product_tmpl.id,
        })
        link.write({'url': 'https://example.com/new-gallery'})
        self.assertEqual(link.url, 'https://example.com/new-gallery')
        link.unlink()
        self.assertFalse(link.exists())

    def test_public_read_only(self):
        link = self.link_tds.with_user(self.public_user)
        self.assertEqual(link.name, 'Technical datasheet')
        self.assertEqual(link.url, 'https://example.com/tds.pdf')

    def test_portal_read_only(self):
        product = self.product_tmpl.with_user(self.portal_user)
        self.assertEqual(
            set(product.link_ids.mapped('url')),
            {'https://example.com/tds.pdf', 'https://example.com/sds.pdf'},
        )

    def test_employee_read_only(self):
        product = self.product_tmpl.with_user(self.employee)
        self.assertEqual(
            set(product.link_ids.mapped('url')),
            {'https://example.com/tds.pdf', 'https://example.com/sds.pdf'},
        )

    @mute_logger('odoo.addons.base.models.ir_model')
    def test_read_only_users_cannot_write(self):
        for user in (self.public_user, self.portal_user, self.employee):
            with self.subTest(user=user.login):
                Links = self.env['product.links'].with_user(user)
                with self.assertRaises(AccessError):
                    Links.create({'name': 'Hack', 'url': 'https://evil.example.com'})
                with self.assertRaises(AccessError):
                    self.link_tds.with_user(user).write({'url': 'https://evil.example.com'})
                with self.assertRaises(AccessError):
                    self.link_tds.with_user(user).unlink()
