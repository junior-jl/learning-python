# In this challenge, you need to implement a method that squares passing variables and returns their sum.

# My solution

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        result = self.x ** 2 + self.y ** 2 + self.z ** 2
        return result

# Educative solution

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z
        return(a + b + c)
