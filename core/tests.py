from django.test import TestCase

# Create your tests here.
from .models import Projeto

class CoreViewsTestCase(TestCase):

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
