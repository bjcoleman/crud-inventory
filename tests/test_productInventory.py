from unittest import TestCase

from product_inventory import ProductInventory


def make_inventory():
    return ProductInventory({'foo': 15, 'bar': 20})


class TestProductInventory(TestCase):

    def test_new_empty_inventory(self):
        pi = ProductInventory({})
        self.assertEqual(0, len(pi.get_product_list()))
        self.assertFalse(pi.is_product('nothing'))

    def test_new_nonempty_inventory(self):
        pi = make_inventory()
        self.assertInventory({'foo': 15, 'bar': 20}, pi)

    def test_reduce_product_inventory_with_full_availability(self):
        pi = make_inventory()
        quantity_removed = pi.reduce_inventory('foo', 5)
        self.assertEqual(5, quantity_removed)
        self.assertInventory({'foo': 10, 'bar': 20}, pi)

    def test_reduce_product_inventory_with_partial_availability(self):
        pi = make_inventory()
        quantity_removed = pi.reduce_inventory('foo', 30)
        self.assertEqual(15, quantity_removed)
        self.assertInventory({'foo': 0, 'bar': 20}, pi)

    def test_increase_product_inventory(self):
        pi = make_inventory()
        pi.increase_inventory('foo', 5)
        self.assertInventory({'foo': 20, 'bar': 20}, pi)

    def test_new_product(self):
        pi = make_inventory()
        pi.new_item('abc', 13)
        self.assertInventory({'foo': 15, 'bar': 20, 'abc': 13}, pi)

    def test_add_existing_product(self):
        pi = make_inventory()
        self.assertRaises(Exception, pi.new_item, 'foo', 5)

    def test_reduce_nonexistent_product(self):
        pi = make_inventory()
        self.assertRaises(Exception, pi.reduce_inventory, 'abc', 5)

    def test_get_quantity_nonexistent_product(self):
        pi = make_inventory()
        self.assertRaises(Exception, pi.get_quantity, 'abc')

    def test_increase_nonexistent_product(self):
        pi = make_inventory()
        self.assertRaises(Exception, pi.increase_inventory, 'abc', 5)

    def assertInventory(self, expected_inventory, pi):
        self.assertEqual(len(expected_inventory), len(pi.get_product_list()))
        self.assertFalse(pi.is_product('nothing'))

        for product in expected_inventory:
            self.assertTrue(pi.is_product(product))
            self.assertEqual(expected_inventory[product], pi.get_quantity(product))
