# In this exercise, you have to calculate a student's total marks using the concept of Classes.

# My solution

class Student:

    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return self.phy + self.chem + self.bio

    def percentage(self):
        return self.totalObtained()/3

# Educative solution

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return(self.phy + self.chem + self.bio)

    def percentage(self):
        return((self.totalObtained() / 300) * 100)
