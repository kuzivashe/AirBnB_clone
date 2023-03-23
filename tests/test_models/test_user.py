#!/usr/bin/python3
""" testing User class """

from models.user import User
import datetime
import unittest
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ testing user class """
    model = User()
    model.name = "My First Model"

    def test_checking_for_docstring_User(self):
        """ test if ll docstrings were written """
        self.assertIsNotNone(User.__doc__)

    def test_subclass_instance_User(self):
        """ test if my_model 1 and 2 are subclasses of BaseModel """
        self.assertTrue(isinstance(self.model, User))

    def test_attribute_email(self):
        """ test email """
        self.assertTrue(hasattr(self.model, 'email'))

    def test_attribute_password(self):
        """ test password """
        self.assertTrue(hasattr(self.model, 'password'))

    def test_attribute_first_name(self):
        """ check first name """
        self.assertTrue(hasattr(self.model, 'first_name'))

    def test_attribute_last_name(self):
        """ check last name """
        self.assertTrue(hasattr(self.model, 'last_name'))

    def test_hasattr(self):
        """ attributes inherited from BaseModel """
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_attributes_types(self):
        """ test types """
        self.assertEqual(type(self.model.email), str)
        self.assertEqual(type(self.model.last_name), str)
        self.assertEqual(type(self.model.first_name), str)
        self.assertEqual(type(self.model.password), str)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
