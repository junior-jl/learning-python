# Object-oriented programming in Python

## Procedural programming

In procedural programming, a program is divided into smaller parts called methods. These **methods** are the **basic entities** used to construct a program. One of the main advantages of procedural programming is code reusability. However, the implementation of a complex real-world scenario becomes a difficult and unwieldy task.

## Object-oriented programming

Object-oriented programming, also referred to as **OOP**, is a programming paradigm that includes, or relies on, the concept of **classes and objects**.

Programming isn't much use if you can't model real-world scenarios using code, right? This is where OOP comes.

The basic idea of OOP is to divide a sophisticated program into a number of **objects** that talk to each other. Objects in a program frequently represent real-world objects.


<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179061136-64d1ea87-4730-41fe-8086-387d63350054.png"/>
</p>

It is also possible for objects to serve application logic and have no direct, real-world parallels. They manage things like authentication, templating, request handling, or any of the other myriad features needed for a practical application.

### Anatomy of objects and classes

Objects may contain data in the form of _fields_ (variables) and methods to operate on that data. Take the example of a real-world light bulb. It has a **state** (on or off), it has a **behaviour**, which means that when it is turned on it lights up, and when it is turned off, it does not produce any light. To conclude this, one can say:

Objects are a collection of **data** and their **behaviours**.

But _where do these objects come from?_ The answer is **classes**.

A **class** can be thought of as a _blueprint_ for creating objects.

The illustration below shows what a **LightBulb** class should look like:

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179062303-c64c2241-ad56-49c4-8abc-3a7093d3d398.png"/>
</p>

From the above illustration, you can see that the state of the object is generally modeled using _variables_ in a class, and the behaviour is modeled using _methods_. There can be different objects of the same class. Each can be in an independent state, but all of them will share the same behaviour and characteristics.

### User-defined data types

It can be inferred from the discussion above that classes are user-defined data types implemented using primitive data types. While primitive data types only focus on modeling the state of the object, **user-defined data types** can encapsulate the state and its behaviours into a unit.

## Introduction to objects and classes

We see _objects_ everywhere. These objects have certain properties that define them. There are certain behaviours that these objects perform on their own, and there are actions that can be performed on them. Let's take the example of a company employee. An employee has the following properties or **attributes**:

- ID
- Salary
- Department

The following actions or behaviours can be performed on an employee:

- Calculation of tax on salary
- Calculation of salary per day

In a company, each worker has a different name, salary, and department, but the _type_ of each worker is _employee_. So there is a generic blueprint for each worker, but each of them has different attributes.

A class has a singular blueprint, and objects are part of a class and are differentiated by their distinct properties.

### Properties

Properties are variables that contain information regarding the object of a class. An employee object will have an ID, salary and department as its _properties_. 

Attributes are also referred to as properties or members. For consistency, we will be using properties throughout the course.

### Methods

Methods are like functions that have access to properties (and other methods) of a class. They can accept parameters and return values. They are used to perform an action on an object of a class. In the example above, we would have **tax()** and **salaryPerDay()** as class methods.

Behaviours are also referred to as member functions or methods. For consistency, we will be using methods throughout the course.

### Benefits of objects and classes

They allow us to create complex applications in Python. This is why they're considered the building blocks of OOP principles.

- Objects and classes are also instrumental for compartmentalizing code. Different components can become separate classes that would interact through interfaces. These ready-made components will also be available for use in future applications.
- The use of classes makes it easier to maintain different parts of an application since it is easier to make changes in classes.

## Declaring a class in Python

In Python, classes are define as follows:

```python
class ClassName:
  pass
```

The **class** keyword tells the compiler that we are creating a custom class, which is followed by the class name and the **:** sign. All the properties and methods of the class will be defined withing the class scope.

### Naming rules

1. Must start with a letter or underscore
2. Should only be comprised of numbers, letters, or underscores

### Creating a class object

Suppose a class **MyClass**. We can create an object of a class by simply using the name of the class followed by a pair of parenthesis. It looks similar to calling a function, but Python can distinguish between the two and creates a new object of corresponding class. Example:

```python
class MyClass:
  pass

obj = MyClass()
print(obj)
```

Output:

```
<__main__.MyClass object at 0x7efd1d626978>
```

By printing the object, **obj**, the output is the memory address at which this object is stored.

### Implementing properties in a class

Let's implement a class **Employee** in Python. We'll start with just adding the properties of the class and will later extend it by adding methods in it.

```python
class Employee:
  ID = None
  salary = None
  department = None
```

Note that if you do not initialize the values of properties, the Python code will **not compile**. Initializing the values of properties inside the class is necessary.

### Accessing properties and assigning values

To access properties of an object, the **dot** notation is used:

```python
object.property
```

There are two ways to assign values to properties of a class.

1. Assign values when defining the class.

```python
class Employee:
    # defining the properties and assigning values to them
    ID = 3789
    salary = 2500
    department = "Human Resources"


# creating an object of the Employee class
Steve = Employee()

# printing properties of Steve - an object of the Employee class
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
```

2. Assign values in the main code.

```python
class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# creating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
```

#### Creating properties outside a class

Python provides a feature to create properties of an object **outside** the class. Let's see an example of this by extending the example of Employee class above.

```python
class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# creating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
# creating a new attribute for Steve
Steve.title = "Manager"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Title:", Steve.title)
```

The property **title** will only be added to Steve and all other future objects will only have the properties which are declared in the class.

### Initializing objects

To _initialize_ an object of a class we use an **initializer**. It is a special method that outlines the steps that are performed when an object of a class is created in the program. It's used to define and assign values to **instance variables** (discussed after this section). The initialization method is similar to other methods but has a predefined name, **\_\_init\_\_**

The double underscores mean that is a special method that the Python interpreter will treat as a special case.

The initializer is a special method because it does not have a return type. The first parameter of **\_\_init\_\_** is **self**, which is a way to refer to the object being initialized. It is always a good practice to define it as the first member method in the class definition.

Initializers are called when an object of a class is created. Example:

```python
class Employee:
  def __init__(self, ID, salary, department):
    self.ID = ID
    self.salary = salary
    self.department = department
    
Steve = Employee(3789, 2500, "Human Resources")

print("ID :", Steve.ID)
print("Salary:", Steve.salary)
print("Department:", Steve.department)

```

#### Initializer with optional parameters

Similar to methods, we can also define initializers with optional parameters. As discussed previously, it's necessary to assign initial values to class properties when defining the class. So, when defining an initializer with optional parameters, it's essential to assign default values to the properties.

You can also have a **default initializer** that has all properties as optional. In this case, all the new objects will be created using the properties initialized in the initializer definition.

Below is an example where one **Employee** class object is created **without** the initializer parameters and one is created **with** the initializer parameters.

```python
class Employee:
    # defining the properties and assigning None to them
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee()
Mark = Employee("3789", 2500, "Human Resources")

# Printing properties of Steve and Mark
print("Steve")
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)
print("Mark")
print("ID :", Mark.ID)
print("Salary :", Mark.salary)
print("Department :", Mark.department)
```

## Class and instance variables

In Python, properties can be defined into two parts:

- class variables
- instance variables


### Class variables

The **class variables** are shared by all instances or objects of the classes. A change in the class variable will change the value of that property in all the objects of the class.

### Instance variables

The **instance variables** are unique to each instance or object of the class. A change in the instance variable will change the value of the property in that _specific object only_.

### Defining class variables and instance variables

Class variables are defined **outside** the initializer and instance variables are defined inside the initializer.

```python
class Player:
  teamName = 'Liverpool' # class variables
  
  def __init__(self, name):
    self.name = name # creating instance variables
    
    
p1 = Player('Mark')
p2 = Player('Steve')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print("Name:", p2.name)
print("Team Name:", p2.teamName)    
```


Output:

```
Name: Mark
Team Name: Liverpool
Name: Steve
Team Name: Liverpool
```

#### Using class variables smartly

Class variables are useful when implementing properties that should be common and accessible to all class objects. Let's see an example of this:

```python
class Player:
    teamName = 'Liverpool'      # class variables
    teamMembers = []

    def __init__(self, name):
        self.name = name        # creating instance variables
        self.formerTeams = []
        self.teamMembers.append(self.name)


p1 = Player('Mark')
p2 = Player('Steve')

print("Name:", p1.name)
print("Team Members:")
print(p1.teamMembers)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.teamMembers)

```

Output:

```
Name: Mark
Team Members:
['Mark', 'Steve']

Name: Steve
Team Members:
['Mark', 'Steve']
```

### Implementing methods in a class

There are three types of methods in Python:

1. instance methods
2. class methods
3. static methods

Instance methods are the most commonly used in Python, so the term **methods** apply to them. Class methods and static methods will be named explicitly as they are.

#### The purpose of methods

Methods act as an interface between a program and the properties of a class in the program. These methods can either alter the content of the properties or use their values to perform a particular computation.

#### Definition and declaration

A **method** is a group of statements that performs some operations and may or may not return a result.

We will extend the **Employee** class example by adding methods to it.

#### Method parameters

Method **parameters** make it possible to pass values to the method. In Python, the first parameter of the method should ALWAYS be **self** and which followed by the remaining parameters.

#### Return statement

The **return** statement makes it possible to get the value from the method. It must be immediately followed by the return value.

#### The self argument

One of the major differences between functions and methods in Python is the first argument in the method definition. Conventionally, this is named **self**. 

This pseudo-variable provides a reference to the calling object, that is the object to which the method or property belongs to. If the user does not mention the **self** as the first argument, the first parameter will be treated for reference to the object.

The **self** argument only needs to be passed in the method definition and not when the method is called.

Given below is an example of implementing methods in a class:

```python
class Employee:
  def __init__(self, ID=None, salary=None, department=None):
    self.ID = ID
    self.salary = salary
    self.department = department
    
  def tax(self):
    return (self.salary * 0.2)
  
  def salaryPerDay(self):
    return (self.salary / 30)
    
Steve = Employee(3789, 2500, "Human Resources")

print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())

```

Output:

```
ID = 3789
Salary 2500
Department: Human Resources
Tax paid by Steve: 500.0
Salary per day of Steve 83.33333333333333
```

#### Method overloading

Overloading referes to making a method perform different operations based on the nature of its arguments.

Unlike in other programming languages, methods **cannot** be explicitly overloaded in Python but can be implicitly overloaded.

In order to include optional arguments, we assign default values to those arguments rather than creating a duplicate method with the same name. If the user chooses not to assign a value to the optional parameter, a default value will automatically be assigned to the variable.

```python
class Employee:
    # defining the properties and assigning them None to the
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    def tax(self, title=None):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)


# creating an object of the Employee class
Steve = Employee()

# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)
```

Output:

```
Demo 1
a = 1
b = 2
c = 3
d = 5
e = None


Demo 2
a = 1
b = 2
c = 3
d = 4
e = None


Demo 3
a = 1
b = 2
c = 3
d = 4
e = 5
```

##### Advantages of method overloading

One might wonder that we could have simply created new methods to perform different jobs rather than overloading the same method. However, under the hood, overloading saves us memory in the system.

An obvious benefit is that the code becomes simple and clean. We don't have to keep track of different methods.

Polymorphism is a very important concept in object-oriented-programming. Method overloading plays a vital role in its implementation. The concept will come up later on in the course.


<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179078353-db38eb57-e8cf-4d0c-bff3-f0b652e0aa0f.png"/>
</p>

### Class methods and static methods

#### Class methods

Class methods work with class variables and are accessible using the class name rather than its object. Since all class objects share the class variables, class methods are used to access and modify class variables.

##### Syntax

To declare a method as a class method, we use the decorator **@classmethod**. **cls** is used to refer to the class just like **self** is used to refer to the object of the class. Just like instance methods, all class methods have **at least one** argument **cls**.

```python
class MyClass:
  classVariable = 'educative'
  
  @classmethod
  def demo(cls):
    return cls.classVariable
    
```

#### Static methods

Static methods are methods that are usually limited to class only and not their objects. They have no direct relation to class variables or instance variables. They are used as utility functions inside the class or when we do not want the inherited classes (more on this later) to modify a method definition.

They can be accessed using the class name or the object name.

##### Syntax

To declare a method as a static method, we used the decorator **@staticmethod**. It does not use a reference to the object or class, so we do not have to use **self** or **cls**. We can pass as many arguments as we want and use this method to perform any function without interfering with the instance or class variables.

```python
class MyClass:
  
  @staticmethod
  def demo():
    print("I am a static method")
```

Static methods do not know anything about the state of the class, i.e., they cannot modify class attributes. The purpose of a static method is to use its parameters and produce a useful result.

Suppose that there is a class, **BodyInfo**, containing information about the physical attributes of a person. We can make a static method for calculating the BMI of any given weight and height:

```python
class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))
```

## Access modifiers

In Python, we can impose access restrictions on different data members and member functions. The restrictions are specified through **access modifiers**. Access modifiers are tags we can associate with each member to define which parts of the program can access it directly.

### Public attributes

**Public attributes** are those that can be accessed inside the class and outside the class. By default, all methods and properties in a class are publicly available. If we want to suggest that a method should not be used publicly, we have to declare it as private explicitly.

Example:

```python
class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary)
```

In the code above, the properties ID and salary and the method **displayID()** are _public_ as they can be accessed in the class as well as outside the class.

### Private attributes

Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class.

The aim is to keep it hidden from the users and other classes. Unlike in different languages, it is not a widespread practice in Python to keep the data members private since we do not want to create hindrances for the users. We can make members private using the double underscore **\_\_** prefix. Trying to access private attributes in the main code will generate an _error_. An example is shown below.

```python
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error
```

- ID is a public property, but \_\_salary is a private property, so it cannot be accessed outside the class
- When it is tried to be accessed outside the class, the following error is generated

```
'Employee' object has no attribute '__salary'
```

- To ensure that no one from the outside knows about this private property, the error does not reveal its identity.

### Private methods

```python
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displaySalary()
Steve.__displayID()  # this will generate an error
```

- ID is a public property, so it can be accessed from outside and inside the class.
- \_\_salary is a private property, so it cannot be accessed outside the class but can be accessed from inside the class.
- The displaySalary() method is a public method, so it can be accessed from outside the class. This method can access the private property, \_\_salary, as well.
- The \_\_displayID() method is a private method, so it cannot be accessed from outside the class.
- When you try to access displayID() from outside the class, the following error is generated:
```
'Employee' object has no attribute '__displayID()'
```
- To ensure that no one from the outside knows about this private property, the error does not reveal its identity.

#### Accessing private attributes in the main code

As discussed above, it is not common to have private variables in Python.

Properties and methods with the double underscore prefix are usually present to make sure that the user does not _carelessly_ access them. Python allows for free hand to the user to avoid any future complications in the code. If the user believes it is **absolutely necessary** to access a private property or a method, they can access it using the _ClassName prefix for the property or method. An example of this is shown below:
  
```python
  
class Employee:
  def __init__(self, ID, salary):
      self.ID = ID
      self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print(Steve._Employee__salary)  # accessing a private property
  
```
  
Protected properties and methods in other languages can be accessed by classes and their subclasses, which will be discussed later in the course. As we have seen, Python does not have a strict rule for accessing properties and methods, so it does not have the protected access modifier.

## Information hiding
  
**Information hiding** refers to the concept of **hiding the inner workings of a class** and simply providing an interface through which the outside world can interact with the class without knowing what's going on inside.

### A real life example
  
Take the doctor-patient model. In the case of an illness, the patient consults the doctor, after which he or she is prescribed and appropriate medicine. The patient only knows the process of going to the doctor. The logic and reasoning behind the doctor's prescription are unknown to the patient. This is a classic example of the patient class interacting with the doctor class without knowing the inner workings of the doctor class.
  

### Components of data hiding

1. Encapsulation
2. Abstraction

#### Encapsulation

Encapsulation is a fundamental programming technique used to achieve data hiding in OOP. It refers to binding **data** and the **methods to manipulate that data** together in a single _unit_, that is, class.

A class can be thought of as a **capsule** having methods and properties inside it. When encapsulating classes, a good convention is to declare all variables of a class **private**. This will restrict direct access by the code outside that class.

Now, to allow the outside world to communicate with the class, one has to implement **public** methods. These methods are called **getters** and **setters**.

##### Advantages of encapsulation

- classes make the code easy to change and maintain.
- properties to be hidden can be specified easily.
- we decide which outside classes or functions can access the class properties.

#### Getters and setters

- A **getter** method allows reading a property's value.
- A **setter** method allows modifying a property's value.

It is a common convention to write the name of the corresponding member fields with the get or set command.

```python
class User:
    def __init__(self, username=None):  # defining initializer
        self.__username = username

    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return (self.__username)


Steve = User('steve1')
print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())

```

Output:

```
Before setting: steve1
After setting: steve2

```

#### Understanding encapsulation using examples

Remember: the goal is to prevent this bound data from any unwanted access by the code outside this class. Let's understand this by using an example of a very basic **User** class.

Consider that we are up for designing an application and are working on modeling the **log in** part of that application. We know that a user needs a **username** and a **password** to log into the app.

An elementary **User** class will be modeled as:

- having a property **userName**
- having a property **password**
- A method named **login()** to grant access

##### A bad example

```python
class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password

    def login(self, userName, password):
        if ((self.userName.lower() == userName.lower())
                and (self.password == password)):
            print("Access Granted!")
        else:
            print("Invalid Credentials!")


Steve = User("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("steve", "6789")
Steve.password = "6789"
Steve.login("steve", "6789")
```

In the above coding example, we can observe that **anyone** can access, change, or print the **password** and **userName** fields directly from the main code. This is dangerous in the case of this **User** class because there is no encapsulation of the credentials of a user, which means anyone can access their account by manipulating the stored data. So, the above code does not follow good coding practices.

##### A good example

```python
class User:
    def __init__(self, userName=None, password=None):
        self.__userName = userName
        self.__password = password

    def login(self, userName, password):
        if ((self.__userName.lower() == userName.lower())
                and (self.__password == password)):
            print(
                "Access Granted against username:",
                self.__userName.lower(),
                "and password:",
                self.__password)
        else:
            print("Invalid Credentials!")


# created a new User object and stored the password and username
Steve = User("Steve", "12345")
Steve.login("steve", "12345")  # Grants access because credentials are valid

# does not grant access since the credentials are invalid
Steve.login("steve", "6789")
Steve.__password  # compilation error will occur due to this line
```

If you comment the last line, the program will work. 

We can observe that **no one** can access, change, or print the **\_\_password** and **\_\_userName** fields directly from the main code. This is a proper implementation of encapsulation.

- For encapsulating a class, all the properties should be private and any access to the properties should be through methods such as _getters_ and _setters_.

## Inheritance

Inheritance provides a way to create a new class from an existing class. The new class is a specialized version of the existing class such that it _inherits_ all the _non-private fields_ (variables) and _methods_ of the existing class. The existing class is used as a starting point or as a _base_ to create the new class.

### The IS A relationship

- Square **IS A** shape
- Python **IS A** programming language
- Car **IS A** vehicle

So, we can conclude that we can build new classes by extending _existing classes_.

|     Existing Class     |  Derived class  |
|:----------------------:|:---------------:|
|         Shape          |     Square      |
|  Programming language  |     Python      |
|        Vehicle         |       Car       |


### The Python object class

The primary purpose of object-oriented programming is to enable a programmer to model the real-world objects using a programming language.

In Python, whenever we create a **class**, it is, by default, a subclass of the build-in Python **object class**. This makes it an excellent example of inheritance in Python. This class has very few properties and methods, but id does provide a strong basis for object-oriented programming in Python.

### Terminologies

In inheritance, in order to create a new class based on an existing class, we use the following terminology:

- Parent class (super class or base class): this class allows the _reuse_ of its **public** properties in another class.
- Child class (subclass or derived class): this class _inherits_ or _extends_ the superclass.

### Syntax

In Python, to implement inheritance, the syntax is quite similar to the basic class definition. The syntax is given below:

```python
class ParentClass:
    # attributes of the parent class
  
class ChildClass(ParentClass):
    # attributes of the child class
```

#### Example

Let's take an example of a Vehicle class as the _parent class_ and implement a **Car** class that will extend from this Vehicle class. Because a _car_ **IS A** _vehicle_, the implementation of inheritance relation between these classes will stand valid.

```python
class Vehicle:
  def __init__(self, make, color, model):
    self.make = make
    self.color = color
    self.model = model
    
  def printDetails(self):
    print("Manufacturer:", self.make)
    print("Color:", self.color)
    print("Model:", self.model)
    
class Car(Vehicle):
  def __init__(self, make, color, model, doors):
    # calling the constructor from parent class
    Vehicle.__init__(self, make, color, model)
    self.doors = doors
  
  def printCarDetails(self):
    self.printDetails()
    print("Doors:", self.doors)
    
obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()
```

- In the code above, we have defined a parent class, Vehicle, and a child class, Car.
- Car inherits all the properties and methods of the Vehicle class and can access and modify them.
- For example, we have called the **printDetails()** method, which was actually defined in the Vehicle class in the **printCarDetails()** method.

### The super function

The use of **super()** comes into play when we implement inheritance. It is used in a child class to **refer** to the parent class without explicitly naming it. It makes the code more manageable, and there is no need to know the name of the parent class to access its attributes.

### Use cases of the **super()** function

#### Accessing parent class properties

Consider the fields name **fuelCap** defined inside a Vehicle class to keep track of the _fuel capacity_ of a vehicle. Another class named Car extends from this Vehicle class. We declare a **class property** inside the Car class with the same name, i.e., fuelCap, but with a different value. Now, if we want to refer to the fuelCap field of the parent class inside the child class, we will have to use the **super()** function.

```python
class Vehicle:  # defining the parent class
    fuelCap = 90


class Car(Vehicle):  # defining the child class
    fuelCap = 50

    def display(self):
        # accessing fuelCap from the Vehicle class using super()
        print("Fuel cap from the Vehicle Class:", super().fuelCap)

        # accessing fuelCap from the Car class using self
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()
```

#### Calling the parent class methods

Just like properties, super() is also used with methods. Whenever a parent class and the immediate child class have any methods with the same name, we use super() to access the methods from the parent class inside the child class. Let's go through an example:

```python
class Vehicle:  # defining the parent class
    def display(self):  # defining display method in the parent class
        print("I am from the Vehicle Class")


class Car(Vehicle):  # defining the child class
    # defining display method in the child class
    def display(self):
        super().display()
        print("I am from the Car Class")


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()
```

#### Using with initializers

Another essential use of the function super() is to call the initializer of the parent class from inside the initializer of the child class.

Below, we have two codes that perform the same way to show that the call to super() in a method or an initializer is not necessarily in the first line of the method.

```python
class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
```

```python
class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)


obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
```

Now, let's take a previous example and use super() to refer to the parent class:

```python
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Door:", self.doors)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()
```

```python
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        super().__init__(make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Door:", self.doors)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()
```

### Types of inheritance

Based upon parent classes and child classes, there exists the following **five** types of inheritance:

1. Single
2. Multi-level
3. Hierarchical
4. Multiple
5. Hybrid

#### Single inheritance

In single inheritance, there is only a single class extending from another class. We can take the example of the Vehicle class as the parent class, and the Car class as the child class.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179842181-e3ff8ac2-2c4b-4c86-99dd-05655a99de67.png"/>
</p>

```python
class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):  # child class
    def openTrunk(self):
        print("Trunk is now open.")


corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(220)  # accessing methods from the parent class
corolla.openTrunk()  # accessing method from its own class
```

#### Multi-level inheritance

When a class is derived from a class which itself is derived from another class, it is called multilevel inheritance. We can extend the classes to as many levels as we want to.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179842465-316006f5-af9e-40f8-a2fb-5bb83c6bc4e8.png"/>
</p>

Let’s implement the three classes illustrated above:

- A car IS A vehicle
- A hybrid IS A car

```python
class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):  # child class of Vehicle
    def openTrunk(self):
        print("Trunk is now open.")


class Hybrid(Car):  # child class of Car
    def turnOnHybrid(self):
        print("Hybrid mode is now switched on.")


priusPrime = Hybrid()  # creating an object of the Hybrid class
priusPrime.setTopSpeed(220)  # accessing methods from the parent class
priusPrime.openTrunk()  # accessing method from the parent class
priusPrime.turnOnHybrid()  # accessing method from the child class
```

#### Hierarchical inheritance

In hierarchical inheritance, more than one class extends from the same base class. The common attributes of these child classes are implemented inside the base class.

Example:

- A car **IS A** vehicle
- A truck **IS A** vehicle

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179842887-cc329eb9-fc4a-4949-97d4-529eb050bc04.png"/>
</p>

```python
class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):  # child class of Vehicle
    pass


class Truck(Vehicle):  # child class of Vehicle
    pass


corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(220)  # accessing methods from the parent class

volvo = Truck()  # creating an object of the Truck class
volvo.setTopSpeed(180)  # accessing methods from the parent class
```

#### Multiple inheritance

When a class is derived from more than one base class, i.e., when a class has more than one immediate parent class, it is called multiple inheritance.

Example:
- HybridEngine IS A ElectricEngine
- HybridEngine IS A CombustionEngine as well.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179843170-a6b4e547-b4ee-4ef7-be35-5807105acffd.png"/>
</p>

```python
class CombustionEngine():  
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine():  
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
```

#### Hybrid inheritance

A type of inheritance which is a combination of Multiple and Multi-level inheritance is called _hybrid inheritance_.

- CombustionEngine IS A Engine
- ElectricEngine IS A Engine
- HybridEngine IS A ElectricEngine and a CombustionEngine

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179843403-160c98f6-c116-4ec1-937b-1e77dd7209b6.png"/>
</p>

```python
class Engine:  # Parent class
    def setPower(self, power):
        self.power = power


class CombustionEngine(Engine):  # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine(Engine):  # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine


class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)


car = HybridEngine()
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
```

### Advantages of inheritance

#### Reusability

It makes the code reusable. Consider that you are up for designing a banking system using classes. Your model might have these:

- A parent class: BankAccount
- A child class: SavingsAccount
- Another child class: CheckingAccount

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179843705-e14a7a28-0dfa-444f-8a69-93e6986c19ec.png"/>
</p>

In the above example, you don't need to duplicate the code for the **deposit()** and **withdraw()** methods inside the child classes. 

#### Code modification

Suppose you put the same code in different classes, but what happens when you have to make changes to a function and in several places? There is a high likelihood that you will forget some places and bugs will be introduced. You can avoid this with inheritance, which will ensure that all changes are localized, and inconsistencies are avoided.

#### Extensibility

It provides an easy way to upgrade or enhance specific parts of a product without changing the core attributes. An existing class can act as a base class from which a new class with upgraded features can be derived.

In the example above, you realize at a later point that you have to diversify this banking application by adding another class for MoneyMarketAccount. So, rather than implementing this class from scratch, you can extend it from the existing BankAccount class as a starting point. You can also reuse its attributes that are common with MoneyMarketAccount.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179844255-6b263d4d-7ef8-4b4d-ae47-bbe7040ad262.png"/>
</p>

#### Data hiding

The base class can keep some data private so that the derived class cannot alter it. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179844402-25a7f5dc-1364-4e25-aaab-055bf5dd998c.png"/>
</p>


## Polymorphism

The word polymorphism is a combination of two greek words, **poly** meaning _many_ and **morph** meaning _forms_.

In programming, _polymorphism_ refers to the same object exhibiting different forms and behaviours.

For example, take the Shape Class. The exact shape you choose can be anything. It can be a rectangle, a circle, a polygon, or a diamond. While these are all shapes, their properties are different. This is called **polymorphism**.

Assume there is a parent class named **Shape** and child classes: **Rectangle, Circle, Polygon** and **Diamond**.

Suppose your application will need methods to calculate the area of each specific shape. You could throw in separate methods in each class (for instance, getSquareArea(), getCircleArea(), etc). But this makes it harder to remember each method's name.

### Making things simpler with polymorphism

It would be better if all specific area calculation methods could be called getArea(). This can be achieved in OOP using polymorphism. The base class declares a function without providing an implementation. Each derived class inherits the function declaration and can provide its own implementation.

### What does polymorphism achieve?

It cuts down the work of the developer. When the time comes to create more specific subclasses with certain unique attributes and behaviours, the developer can alter the code in the specific areas where the responses differ. All the other pieces of code can be left untouched.

### Implementation

#### Implementation with methods

Consider two shapes that are defined as classes: Rectangle and Circle. These classes contain the getArea() method that calculates the area for the respective shape depending on the values of their properties.

```python
class Rectangle():

    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)


class Circle():
    # initializer
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].getArea()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].getArea()))
```

Output:

```
Sides of a rectangle are 4
Area of rectangle is: 60
Sides of a circle are 0
Area of circle is: 153.958
```

#### Implementation using inheritance

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/179857878-9ca562ff-4d4f-401a-8c5c-66fb09190e58.png"/>
</p>

We will be implementing the parent class first, and then the child classes.

##### Shape class

```python
class Shape:
  def __init__(self):
    self.sides = 0
    
  def getArea(self):
    pass
```

##### Rectangle class

```python
# Rectangle IS A Shape with a specific width and height
class Rectangle(Shape):
  # initializer
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.sides = 4
    
  # method to calculate Area
  def getArea(self):
    return self.width * self.height
```

##### Circle class

```python
# Circle IS A Shape with a specific radius
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
    self.sides = 0
  
  # method to calculate Area
  def getArea(self):
    return self.radius * self.radius * 3.142
```

**Note**: I don't see the point yet. The code would work if the getArea() method wasn't defined in Shape class.

### Method overriding

It is the process of redefining a parent class's method in a subclass. In the previous example, the Rectangle and Circle classes were overriding the getArea() method from the Shape class. In this case:

- the method in the parent class is called the **overridden method**.
- the methods in the child classes are called the **overriding methods**.

#### Advantages and key features of method overriding

- The derived classes can give their own specific implementations to inherited methods without modifying the parent class methods.
- For any method, a child class can use the implementation in the parent class or make its own implementation.
- Method overriding needs inheritance, and there should be at least one derived class to implement it.
- The methods in the derived classes usually have a dissimilar implementation.

### Operator overloading

Operators in Python can be overloaded to operate in a certain user-defined way. Whenever an operator is used in Python, its corresponding method is invoked to perform its predefined function. For example, when the + operator is called, it invokes the special function **\_\_add\_\_** in Python, but this operator acts differently for different data types. For example, the + operator adds the numbers when it is used between two int data types and merges two strings when it is used between string data types.

```python
print(5 + 3)
print("money" + "maker")
```

outputs

```
8
moneymaker
```

#### Overloading operators for a user-defined class

When a class is defined, its objects can interact with each other through the operators, but is necessary to define the behaviour of these operators through operator overloading.

We are going to implement a class that represents a complex number. It consists of a real part and an imaginary part.

When we add a complex number, the real part is added to the real part, and the imaginary part is added to the imaginary part.

Let's implement the complex number class and overload the + and - operators below:

```python
class Com:
  def __init__(self, real=0, imag = 0):
    self.real = real
    self.imag = imag
    
  def __add__(self, other):
    temp = Com(self.real + other.real, self.imag + other.imag)
    return temp
    
  def __sub__(self, other):
    temp = Com(self.real - other.real, self.imag - other.imag)
    return temp
    
obj1 = Com(3, 7)
obj2 = Com(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imag)
print("real of obj4:", obj4.real)
print("imag of obj4:", obj4.imag)
```

Output:

```
real of obj3: 5
imag of obj3: 12
real of obj4: 1
imag of obj4: 2
```

#### Special functions for some common operators

| Operators |            Method             |
|:---------:|:-----------------------------:|
|    \+     |   \_\_add\_\_ (self, other)   |
|    \-     |   \_\_sub\_\_ (self, other)   |
|     /     | \_\_truediv\_\_ (self, other) |
|    \*     |   \_\_mul\_\_ (self, other)   |
|     <     |   \_\_lt\_\_ (self, other)    |
|     >     |   \_\_gt\_\_ (self, other)    |
|    ==     |   \_\_eq\_\_ (self, other)    |

| Operators | Method |
| :--: | :--: |
\+ | \_\_add\_\_ (self, other)
\- | \_\_sub\_\_ (self, other)
/ | \_\_truediv\_\_ (self, other)
\* | \_\_mul\_\_ (self, other)
< | \_\_lt\_\_ (self, other)
\> | \_\_gt\_\_ (self, other)
== | \_\_eq\_\_ (self, other)

#### Implementing polymorphism using duck typing

##### What is duck typing?

We say that if an object _quacks_ like a duck, _swims_ like a duck, _eats_ like a duck or in short, _acts_ like a duck, that object is a duck.

##### Dynamic typing

Duck typing extends the concept of dynamic typing in Python. Dynamic typing means that we can change the type of an object later in the code.

See the code below for a better understanding of dynamic typing in Python:

```python
x = 5  # type of x is an integer
print(type(x))
x = "Educative"  # type of x is now string
print(type(x))
```

Output:

```
<class 'int'>
<class 'str'>
```

##### Implementing duck typing

```python
class Dog:
  def Speak(self):
    print("Woof woof")
    
class Cat:
  def Speak(self):
    print("Meow meow")
    
class AnimalSound:
  def Sound(self, animal):
    animal.Speak()
    
sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)

```

Output:

```
Woof woof
Meow meow
```

- The type of **animal** is not defined in the definition of the method Sound.
- Type of animal is determined when the method is called, so it does not matter which object type you are passing as a parameter in the Sound() method, what matters is that the Speak() method should be defined in all the classes whose objects are passed in the Sound() method.
- We can use any property or method of animal in the AnimalSound class as long as it is declared in that class.

### Abstract base classes

Abstract base classes (ABC) define a set of methods and properties that a class must implement in order to be considered a duck-type instance of that class.

Let's look at an example to understand why we should use abstract base classes.

```python
class Shape: # Shape is a child class of ABC
  def area(self):
    pass
    
  def perimeter(self):
    pass
    
class Square(Shape):
  def __init__(self, length):
    self.length = length
    
  def area(self):
    return self.length * self.length
    
  def perimeter(self):
    return 4 * self.length
    
shape = Shape()
square = Square(4)

```

In the example above, you can see that an instance of Shape can be created even though an object from this class cannot stand on its own. Shape class should provide a blueprint for its child classes to implement methods in it. To prevent the user from making a Shape class object, we use abstract base classes.

#### Syntax

To define an abstract base class, we use the abc module. The abstract base class is inherited from the built-in ABC class. We have to use the decorator @abstractmethod above the method that we want to declare as an abstract method.

```python
from abc import ABC, abstractmethod

class ParentClass(ABC):

  @abstractmethod
  def method(self)
  
```

Example:

```python
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length


shape = Shape()
# this code will not compile since Shape has abstract methods without
# method definitions in it
```

```python
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length


square = Square(4)
# this will code will not compile since abstract methods have not been
# defined in the child class, Square
```

As you can see above, the code does not compile since we have not defined the abstract methods, area and perimeter, inside the parent class, Shape, or the child class, Square. Let’s do it and see what happens:

```python
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


shape = Shape()
# this code will not compile since Shape has abstract methods without
# method definitions in it
```

```python
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


square = Square(4)
# this code will not generate an error since abstract methods have been
# defined in the child class, Square
```

- Note: Methods with @abstractmethod decorators must be defined in the child class.

By using abstract base classes, we can control classes whose objects can or cannot be created.

## Object relationships

The concepts of inheritance and polymorphism taught us how to create dependent classes out of a base class. While inheritance represents a relationship between classes, there are situations where there are relationships between objects.

### Relationships between classes

There are three main class relationships we need to know. We have studied the **IS A** relation. Let's study the other two below.

#### Part-of

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180064036-1b9c6313-e6e2-4919-9e4e-320c5649efe5.png"/>
</p>

In this relationship, one class object is a component of another class object. An instance of the component class can only be created inside the main class. In the example above, class B and class C have their own implementations, but their objects are only created once a class A object is created. Hence, **part-of** is a dependent relationship.

#### Has-a

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180064389-ad17d38d-f12b-45cf-9113-a0f420e5304c.png"/>
</p>

This is a slightly less concrete relationship between two classes. Class A and class B have a **has-a** relationship if one or both need the other's object to perform an operation, but both class objects can exist independently of each other. 

### Association

In OOP, **association** is the common term for both the **has-a** and **part-of** relationships but is not limited to these. Two objects are in an association relationship is a generic statement, which means that we don't worry about the lifetime dependency between the objects.

### Aggregation

Aggregation follow the **has-a** model. This creates a parent-child relationship between two classes, with one class owning the object of another.

#### Independent lifetimes

In aggregation, the lifetime of the owned object does not depend on the lifetime of the owner.

The owner object could get deleted, but the owned object can continue to exist in the program. In aggregation, the parent only contains a **reference** to the child, which removes the child's dependency.

#### Example

Let's take the example of people and their country of origin. Each person is associated with a country, but the country can exist without the person.

```python
class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country Name:", self.name)
        print("Country Population", self.population)


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person Name:", self.name)
        self.country.printDetails()


c = Country("Wales", 1500)
p = Person("Joe", c)
p.printDetails()

# deletes the object p
del p
print("")
c.printDetails()
```

As we can see, the Country object c lives on even after we delete the Person object p. This creates a weaker relationship between the two classes.

### Composition

Composition is the practice of accessing other class objects in your class. In such a scenario, the class which creates the object of the other class is known as the owner and is responsible for the lifetime of that object.

Composition relationships are **part-of** relationships where the part must constitute a segment of the whole object. We can achieve composition by adding smaller parts of other classes to make a complex unit.

#### Example

A car is composed of an engine, tires, and doors. In this case, a Car owned these objects, so a Car is an owner class, and the tires, doors and engine are the owned classes.

```python
class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details:", self.capacity)


class Tires:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires:", self.tires)


class Doors:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of doors:", self.doors)


class Car:
    def __init__(self, eng, tr, dr, color):
        self.eObj = Engine(eng)
        self.tObj = Tires(tr)
        self.dObj = Doors(dr)
        self.color = color

    def printDetails(self):
        self.eObj.printDetails()
        self.tObj.printDetails()
        self.dObj.printDetails()
        print("Car color:", self.color)


car = Car(1600, 4, 2, "Grey")
car.printDetails()
```

We have created a Car class which contains the objects of Engine, Tires, and Doors classes. Car class is responsible for their lifetime, i.e, when a Car dies, so does tire, engine and doors too.
