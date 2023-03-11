#!/usr/bin/python3
""" doctest unittest """
import unittest
import pep8
from models.city import City
import os


class TestBase(unittest.TestCase):
    """ test """

    def test_pep8(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        file_city = "models/city.py"
        file_test_city = "tests/test_models/test_city.py"
        check = style.check_files([file_city, file_test_city])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

    @classmethod
    def setUpClass(cls):
        """ first set up
        check = style.check_files([file_city, file_test_city])
        """
        cls.ins = City()

    @classmethod
    def teardown(cls):
        """ final statement """
        del cls.ins
        try:
            os.remove("file.json")
        except:
            pass

    def test_Userdoc(self):
        """ test base model documentation
        self.assertNotEqual(len(models.__doc__), 0)
        self.assertNotEqual(len(models.base_model.__doc__), 0)
        """
        self.assertNotEqual(len(City.__doc__), 0)

    def test_BaseModelAttr(self):
        """ test basemodel attributes """
        self.assertEqual(hasattr(self.ins, "state_id"), True)
        self.assertEqual(hasattr(self.ins, "name"), True)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.ins, City))

if __name__ == '__main__':
    unittest.main()
