#!/usr/bin/python3
""" testing the city class """

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """ test city class """
    model = City()

    def test_checking_for_docstring_User(self):
        """ test if all docstring were written """
        self.assertIsNotNone(City.__doc__)

    def test_subclass_instance_User(self):
        """ test if my_model 1 and 2 are subclasses of BaseModel """
        self.assertIsInstance(self.model, City)

    def test_attribute(self):
        """ test attributes """
        self.assertEqual(hasattr(self.model, "state_id"), True)
        self.assertEqual(hasattr(self.model, "name"), True)

    def test_types(self):
        """ test types """
        self.assertEqual(type(self.model.state_id), str)
        self.assertEqual(type(self.model.name), str)


if __name__ == '__main__':
    unittest.main()
