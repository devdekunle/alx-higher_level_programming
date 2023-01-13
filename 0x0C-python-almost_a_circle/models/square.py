#!/usr/bin/python3
"""Module that contains the Square class which will be a subclass 
   of the Rectangle class"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """ The square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """object instantiation"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the value of size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value
    
    def __str__(self):
        """method to make object printable"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
        
