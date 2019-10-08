# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestLink(TransactionCase):
    def setUp(self, *args, **kwargs):
        result = super(TestLink, self).setUp(*args, **kwargs)
        user_demo = self.env.ref('base.user_demo')
        self.env= self.env(user=user_demo)
        return result

    def test_create(self):
        "Create a simple Link"
        Test = self.env['product.link']
        link = Test.create({'product_tmpl_id': 1, 'name': 'Test Link', 'url': '#'})
        self.assertEqual(link.url, '#')
        
    def test_record_rule(self):
        "Test per user record rules"
        Test = self.env['product.link']
        link = Test.sudo().create({'product_tmpl_id': 1, 'name': 'Admin Link', 'url': '#'})
        with self.assertRaises(AccessError):
        Test.browse([task.id]).name