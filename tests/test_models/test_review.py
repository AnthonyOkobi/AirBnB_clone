#!/usr/bin/python3
""" doctest unittest """
import unittest
import pep8
from models.review import Review
import os


class TestBase(unittest.TestCase):
    """ test """

    def test_pep8(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        file_review = "models/review.py"
        file_test_review = "tests/test_models/test_review.py"
        check = style.check_files([file_review, file_test_review])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

    @classmethod
    def setUpClass(cls):
        """ first set up
        check = style.check_files([file_user, file_test_user])
        """
        cls.ins = Review()

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
        self.assertNotEqual(len(Review.__doc__), 0)

    def test_BaseModelAttr(self):
        """ test basemodel attributes """
        self.assertEqual(hasattr(self.ins, "place_id"), True)
        self.assertEqual(hasattr(self.ins, "user_id"), True)
        self.assertEqual(hasattr(self.ins, "text"), True)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.ins, Review))

if __name__ == '__main__':
    unittest.main()
