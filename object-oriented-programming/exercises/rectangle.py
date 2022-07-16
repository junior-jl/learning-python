# In this challenge, you will implement a rectangle class using the concepts of encapsulation.

# Implement a constructor to initialize the values of two private properties: length and width.

# Implement the methods area() and perimeter()

# My solution

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)
      
# Educative solution was basically the same
