import unittest
import crud_api
import json
import product_inventory


class TestCRUDAPI(unittest.TestCase):

    def setUp(self):
        crud_api.app.testing = True
        self.app = crud_api.app.test_client()

    def initialize_database(self, inventory):
        crud_api.pi = product_inventory.ProductInventory(inventory)

    def run_query(self, search_term):
        result = self.app.get('/search?query={}'.format(search_term))
        inventory = json.loads(result.data)
        return inventory

    def test_root(self):
        result = self.app.get('/')
        inventory = json.loads(result.data)
        self.assertEqual({}, inventory)

    def test_empty_db_search_provides_empty_results(self):
        self.initialize_database({})
        inventory = self.run_query('foo')
        self.assertEqual([], inventory)

    def test_single_item_db_with_matching_search(self):
        self.initialize_database({'aquarium': 5})
        inventory = self.run_query('aquarium')
        self.assertEqual([{'name': 'aquarium', 'quantity': 5}], inventory)

    def test_single_item_db_with_non_matching_search(self):
        self.initialize_database({'phone': 2})
        inventory = self.run_query('aquarium')
        self.assertEqual(0, len(inventory))

    def test_extra_query_parameter_is_400_status(self):
        result = self.app.get('/search?query=foo&value=bar')
        self.assertEqual(400, result.status_code)