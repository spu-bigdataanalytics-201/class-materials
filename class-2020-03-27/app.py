"""
This is my module.

This module is going to help me for my assignment.
"""
import datetime


def find_age(birth_year):
    """
    Returns the age from given birth year.
    """
    now = datetime.datetime.now()
    return now.year - birth_year


class Person:
    """
    This class represents a Person.

    This this called docstring.
    """
    first_name: str
    last_name: str
    birth_year: int

    def __init__(self, first_name, last_name, birth_year):
        """
        Creating an instance from person class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
