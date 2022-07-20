# You have to implement a Sedan class, which inherits from the Car class and contains a SedanEngine object.
# Note: You already know that in such a composition relation, the Sedan class will be responsible for SedanEngine lifetime.

# My solution

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def printDetails(self):
        print("Model: {}".format(self.model))
        print("Color: {}".format(self.color))


class SedanEngine:
    def start(self):
        print("Car has started.")

    def stop(self):
        print("Car has stopped.")


class Sedan(Car):
    def __init__(self, model, color):
        super().__init__(model, color)
        self.engine = SedanEngine()

    def setStart(self):
        self.engine.start()

    def setStop(self):
        self.engine.stop()
        
        
# Educative solution was exactly the same.
