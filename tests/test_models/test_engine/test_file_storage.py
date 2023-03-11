#!/usr/bin/python3
""" doctest unittest """
import unittest
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestBase(unittest.TestCase):
    """ test """

    def test_pep8_filestorage(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        file_fs = "models/engine/file_storage.py"
        file_test_fs = "tests/test_models/test_engine/test_file_storage.py"
        check = style.check_files([file_fs, file_test_fs])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

    @classmethod
    def setUpClass(cls):
        """ first set up
        check = style.check_files([file_base_model, file_test_base_model])
        """
        cls.ins = FileStorage()

    @classmethod
    def teardown(cls):
        """ final statement """
        del cls.ins
        try:
            os.remove("file.json")
        except:
            pass

    def test_FileStorage_methods(self):
        """ test base model documentation
        self.assertNotEqual(len(models.__doc__), 0)
        self.assertNotEqual(len(models.base_model.__doc__), 0)
        """
        self.assertNotEqual(len(FileStorage.__doc__), 0)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_FileStorsageAttr(self):
        """ test basemodel attributes """
        self.assertEqual(hasattr(self.ins, "_FileStorage__file_path"), True)
        self.assertTrue(type(self.ins._FileStorage__file_path) is str)
        self.assertEqual(hasattr(self.ins, "_FileStorage__objects"), True)

    def test_isinstanceofFileStorage(self):
        self.assertTrue(isinstance(self.ins, FileStorage))

    def test_allFS(self):
        my_dict = self.ins.all()
        self.assertTrue(type(my_dict) is dict)

    def test_saveFS(self):
        dummy = BaseModel()
        my_id = dummy.id
        dummy.name = "Haroldo"
        dummy.save()
        storage.reload()
        my_objs = storage.all()["BaseModel.{}".format(my_id)]
        self.assertTrue(hasattr(my_objs, "name"))
        self.assertTrue(my_objs.name == "Haroldo")
        self.assertTrue(os.path.exists('file.json'))

    def test_newFS(self):
        l1 = len(storage.all())
        dummy = BaseModel()
        l2 = len(storage.all())
        self.assertEqual(l1, l2 - 1)

if __name__ == '__main__':
    unittest.main()
