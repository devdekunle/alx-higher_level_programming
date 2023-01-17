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

    def update(self, *args, **kwargs):
        """ method to update the values of the instance attributes"""
        if len(args) > 0:
            for i, val in enumerate(args):
                if i == 0:
                    setattr(self, "id", val)
                elif i == 1:
                    setattr(self, "size", val)
                elif i == 2:
                    setattr(self, "x", val)
                elif i == 3:
                    setattr(self, "y", val)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    setattr(self, "id", value)
                elif key == "x":
                    setattr(self, "x", value)
                elif key == "y":
                    setattr(self, "y", value)
                elif key == "size":
                    setattr(self, "size", value)

    def to_dictionary(self):
        """returns the dictionary representation of a class"""
        square_dict = {}
        square_dict['id'] = self.id
        square_dict['x'] = self.x
        square_dict['y'] = self.y
        square_dict['size'] = self.width
        return square_dict
