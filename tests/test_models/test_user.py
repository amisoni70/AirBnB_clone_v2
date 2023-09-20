#!/usr/bin/python3
"""
Unittest module for the User class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Defines tests for the User class """

    def __init__(self, *args, **kwargs):
        """ Initialize the test_User class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    '''
    def test_first_name(self):
        """
        Test case for validating the 'first_name'
        attribute is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Test case for validating the 'last_name'
        attribute is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Test case for validating the 'email'
        attribute is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Test case for validating the 'password'
        attribute is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
    '''
