#!/usr/bin/python3
"""
BaseModel Class Tests
"""

import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class BaseModelTest(unittest.TestCase):
    """
    Tests for BaseModel Class
    """

    @classmethod
    def setUpClass(cls):
        """ set up an instance for tests """
        cls.my_model = BaseModel()
        cls.my_model.name = "My First Model"
        cls.my_model.my_number = 89
        cls.my_model2 = BaseModel()
        cls.my_model2.name = "My First Model"
        cls.my_model2.my_number = 89

    @classmethod
    def teardown(cls):
        """ delete the instance at the end of the tests """
        del cls.my_model
        del cls.my_model2
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_BaseModel(self):
        """ test if all docstring were written """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_instance_BaseModel(self):
        """ test if my_model 1 and 2 are instance of BaseModel
        if they are instances, check if the attributes are well
        assigned
        """
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertTrue(isinstance(self.my_model2, BaseModel))
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model2.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(self.my_model2.my_number, 89)

    def test_diff_instances_BaseModel(self):
        """ test if two instances were created at different times
        and have different id's
        """
        self.assertNotEqual(self.my_model.id, self.my_model2.id)

    def test_str(self):
        """ test if __str__ method show correct output """
        string = "[BaseModel] ({}) {}".format(self.my_model.id,
                                              self.my_model.__dict__)
        self.assertEqual(string, str(self.my_model))

    def test_save_BaseModel(self):
        """ test if updated at changes """
        self.my_model.save()
