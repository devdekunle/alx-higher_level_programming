#!/usr/bin/python3
""" This module contains the rectangle class
    which inherits from thr base class"""


from models.base import Base


class Rectangle(Base):

    """ definition of Rectangle which is subclass of base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """object instantiation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ return the value of width"""
        return self.__width

    @property
    def height(self):
        """return the value of height"""
        return self.__height

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @property
    def y(self):
        """"return the value of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Method to set the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Method to set the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """Method to set the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Method to set the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ method to return the area of a rectangle"""
        return self.height * self.width


    def display(self):
        """ function to display the rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end='')
            print(self.width * "#")

    def __str__(self):
        """"make object printable"""
        string = f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return string
