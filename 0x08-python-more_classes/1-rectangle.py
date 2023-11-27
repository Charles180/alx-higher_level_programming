#!/usr/bin/python3
"""module documentation"""


class Rectangle():
    """Defines a class Rectangle"""

    def __init__(self, w = 0, h = 0):
        """Initializes the class Rectangle"""
        self.width = w
        self.height = h

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be grater than 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an int")
        if value < 0:
            raise ValueError("height must be greater than 0")
        self.__height = value
