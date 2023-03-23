#!/usr/bin/python3
""" testing review class """

from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """ test user class """
    model = Review()

    def test_checking_for_docstring_User(self):
        """ test if all docstring were written """
        self.assertIsNotNone(Review.__doc__)

    def test_subclass_instance_Review(self):
        """ test if my_model 1 and 2 are subclasses of BaseModel """
        self.assertIsInstance(self.model, Review)

    def test_attribute_place_id(self):
        """ test attr """
        self.assertEqual(hasattr(self.model, "place_id"), True)
        self.assertEqual(hasattr(self.model, "user_id"), True)
        self.assertEqual(hasattr(self.model, "text"), True)

    def test_types(self):
        """ test types """
        self.assertEqual(type(self.model.place_id), str)
        self.assertEqual(type(self.model.user_id), str)
        self.assertEqual(type(self.model.text), str)


if __name__ == '__main__':
    unittest.main()
