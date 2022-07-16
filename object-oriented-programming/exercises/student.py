# In this challenge, you will implement a student class.

# Implement the following properties as private:

# name
# rollNumber
# Include the following methods to get and set the private properties above:

# getName()
# setName()
# getRollNumber()
# setRollNumber()
# Implement this class according to the rules of encapsulation.

# Note: Do not use initializers to initialize the properties. Use the set methods to do so. 
# If the setter is not defined properly, the corresponding getter will also generate an 
# error even if the getter is defined properly.

# My solution

class Student:
    def setName(self, name):
        self.__name = name 

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

# Educative solution (better? it initializes/declares the variables)

class Student:
    __name = None
    __rollNumber = None
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber
