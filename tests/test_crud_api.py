import unittest
import crud_api


class TestCRUDAPI(unittest.TestCase):

    def setUp(self):
        crud_api.app.testing = True
        self.app = crud_api.app.test_client()

    def test_root(self):
        result = self.app.get('/')
        self.assertEqual('{}', result.data)