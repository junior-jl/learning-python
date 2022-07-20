# When a method in a derived class overrides a method in a base class, it is still possible to call the overridden method using the super() function.
# If you write super().method(), it will call the method that was defined in the superclass.
# You are given a partially completed code in the editor. Modify the code so that it returns the following:

# Sample input
# circle = XShape("Circle");
# circle.getName()

# Sample output
# "Shape, Circle"


# My solution (the problem was a little unclear)

class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return super().getName() + ', ' + self.xsname
      
      
# Educative solution was identical.      
