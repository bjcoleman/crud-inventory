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