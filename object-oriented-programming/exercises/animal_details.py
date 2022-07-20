# A parent class named Animal.

# Inside it, define:
# name
# sound
# __init__()
# Animal_details() function
# It prints the name and sound of the Animal.
# Then there are two derived classes*

# Dog class
# Has a property family
# Has an initializer that calls the parent class initializer in it through super()
# Has an overridden method named Animal_details() which prints detail of the dog.
# Sheep class
# Has a property color
# Has an initializer that calls the parent class initializer in it through super()
# Has an overridden method named Animal_details(), which prints detail of the sheep
# The derived classes should override the Animal_details() method defined in the Animal class.

# The overridden method in Dog class should print the value of family as well as the name and sound.
# The overridden method in Sheep class should print the value of color as well as the name and sound


# My solution

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def Animal_details(self):
        print("Name: {}".format(self.name))
        print("Sound: {}".format(self.sound))

class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family
        

    def Animal_details(self):
        print("Name: {}".format(self.name))
        print("Sound: {}".format(self.sound))
        print("Family: {}".format(self.family))

class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color
        

    def Animal_details(self):
        print("Name: {}".format(self.name))
        print("Sound: {}".format(self.sound))
        print("Color: {}".format(self.color))
