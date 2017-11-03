import unittest
import crud_api
import json


class TestCRUDAPI(unittest.TestCase):

    def setUp(self):
        crud_api.app.testing = True
        self.app = crud_api.app.test_client()

    def test_root(self):
        result = self.app.get('/')
        inventory = json.loads(result.data)
        self.assertEqual({}, inventory)

    def test_empty_db_search_provides_empty_results(self):
        result = self.app.get('/search?query=foo')
        inventory = json.loads(result.data)
        self.assertEqual([], inventory)

    def test_single_item_db_with_matching_search(self):
        crud_api.pi.new_item('aquarium', 5)
        result = self.app.get('/search?query=aquarium')
        inventory = json.loads(result.data)
        self.assertEqual([{'name': 'aquarium', 'quantity': 5}], inventory)
