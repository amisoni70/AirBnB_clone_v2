#!/usr/bin/python3
"""
Unittest module for the Sate class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Defines tests for the State class. """

    def __init__(self, *args, **kwargs):
        """ Initialize attributes for the test class """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    '''
    def test_name3(self):
        """ Tests if 'name' attribute is a string. """
        new = self.value()
        self.assertEqual(type(new.name), str)
    '''
