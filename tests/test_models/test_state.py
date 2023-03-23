#!/usr/bin/python3
"""testing for state class """

from models.state import State
import datetime
import unittest


class TestUser(unittest.TestCase):
    """ test User class """
    model = Sate()

    def test_checking_for_docstring_User(self):
        """ test if all docstrings were written """
        self.assertIsNotNone(State.__doc__)

    def test_subclass_instance_User(self):
        """ test if my_model 1 and 2 are subclasses of BaseModel """
        self.assertIsInstance(self.model, State)

    def test_attribute(self):
        """ test attr """
        self.assertEqual(hasattr(self.model, "name"), True)

    def test_types(self):
        """ test types """
        self.assertEqual(type(self.model.name), str)


if __name__ == '__main':
    unittest.main()
