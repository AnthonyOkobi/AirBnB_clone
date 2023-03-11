#!/usr/bin/python3
""" doctest unittest """
import unittest
import pep8
from models.place import Place
import os


class TestBase(unittest.TestCase):
    """ test """

    def test_pep8(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        file_place = "models/place.py"
        file_test_place = "tests/test_models/test_place.py"
        check = style.check_files([file_place, file_test_place])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

    @classmethod
    def setUpClass(cls):
        """ first set up
        check = style.check_files([file_place, file_test_place])
        """
        cls.ins = Place()

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
        self.assertNotEqual(len(Place.__doc__), 0)

    def test_BaseModelAttr(self):
        """ test basemodel attributes """
        self.assertEqual(hasattr(self.ins, "city_id"), True)
        self.assertEqual(hasattr(self.ins, "user_id"), True)
        self.assertEqual(hasattr(self.ins, "name"), True)
        self.assertEqual(hasattr(self.ins, "description"), True)
        self.assertEqual(hasattr(self.ins, "number_rooms"), True)
        self.assertEqual(hasattr(self.ins, "number_bathrooms"), True)
        self.assertEqual(hasattr(self.ins, "max_guest"), True)
        self.assertEqual(hasattr(self.ins, "price_by_night"), True)
        self.assertEqual(hasattr(self.ins, "latitude"), True)
        self.assertEqual(hasattr(self.ins, "longitude"), True)
        self.assertEqual(hasattr(self.ins, "amenity_ids"), True)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.ins, Place))

if __name__ == '__main__':
    unittest.main()
