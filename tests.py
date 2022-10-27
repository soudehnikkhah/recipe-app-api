"""Sample Test"""

from django.test import SimpleTestCase
from app  import calc
class calctests(SimpleTestCase):
    def test_add_Numbers(self):
        res=calc.Add(5,6)
        self.assertEqual(res,11)



