#!/usr/bin/python3
""" doctest unittest """
import unittest
import pep8
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestBase(unittest.TestCase):
    """ test """

    def test_pep8(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        file_base_model = "models/base_model.py"
        file_test_base_model = "tests/test_models/test_base_model.py"
        check = style.check_files([file_base_model, file_test_base_model])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

    @classmethod
    def setUpClass(cls):
        """ first set up
        check = style.check_files([file_base_model, file_test_base_model])
        """
        cls.ins = BaseModel()

    @classmethod
    def teardown(cls):
        """ final statement """
        del cls.ins
        try:
            os.remove("file.json")
        except:
            pass

    def test_BaseModeldoc(self):
        """ test base model documentation
        self.assertNotEqual(len(models.__doc__), 0)
        self.assertNotEqual(len(models.base_model.__doc__), 0)
        """
        self.assertNotEqual(len(BaseModel.__doc__), 0)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_BaseModelAttr(self):
        """ test basemodel attributes """
        self.assertEqual(hasattr(self.ins, "id"), True)
        self.assertEqual(hasattr(self.ins, "created_at"), True)
        self.assertEqual(hasattr(self.ins, "updated_at"), True)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.ins, BaseModel))

    def test_save_updated_at_created_at(self):
        self.ins.save()
        self.assertNotEqual(self.ins.created_at, self.ins.updated_at)
        dummy = BaseModel()
        my_id = dummy.id
        dummy.name = "Haroldo"
        dummy.save()
        storage.reload()
        my_objs = storage.all()["BaseModel.{}".format(my_id)]
        self.assertTrue(hasattr(my_objs, "name"))
        self.assertTrue(my_objs.name == "Haroldo")
        self.assertTrue(os.path.exists('file.json'))

    def test_dict(self):
        dicto = self.ins.to_dict()
        self.assertTrue(dicto.get("__class__"))
        self.assertTrue(type(dicto) is dict)
        self.assertTrue("to_dict" in dir(self.ins))

    def test_var_storage(self):
        my_objs = storage.all()

        self.assertTrue(type(my_objs) is dict)
        self.assertTrue(isinstance(storage, FileStorage))

    def test_reload(self):
        self.ins.save()
        storage.reload()
        my_dict = storage.all()
        self.assertTrue(len(my_dict) != 0)

if __name__ == '__main__':
    unittest.main()
