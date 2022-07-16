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

From the above illustration, you can see that the state of the object is generally modeled using _variables_ in a class, and the behaviour is modeled using _methods_. There can be many different objects of the same class. Each can be in an independent state, but all of them will share the same behaviour and characteristics.

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

- Objects and classes are also instrumental for compartmentalizing code. Differente components can become separate classes that would interact through interfaces. These ready-made components will also be avaliable for use in future applications.
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


# cerating an object of the Employee class
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


# cerating an object of the Employee class
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

#### Creating properties outside of a class

Python provides a feature to create properties of an object **outside** the class. Let's see an example of this by extending the example of Employee class above.

```python
class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# cerating an object of the Employee class
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

The initializer is a special method because it does not have a return type. The first parameter of **\_\_init\_\_** is **self**, which is a way to refer to the object beign initialized. It is always a good practice to define it as the first member method in the class definition.

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

Instance methods are the most commonly used in Python, so the term **methods** apply to them. Class methods and static methods will be name explicitly as they are.

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

One of the major differences between functions and methods in Python is the first argument in the method definition. Conventionally, this is name **self**. 

This pseudo-variable provides a reference to the calling object, that is the object to which the method or property belongs to. If the user does not mention the **self** as the first argument, the first parameter will be treated for reference to the object.

The **self** argument only needs to be passed in the method definition and not when the method is called.

Given below is an example of implementing methods in a class:

```
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


# cerating an object of the Employee class
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

One might wonder that we could simply created new methods to perform different jobs rather than overloading the same method. However, under the hodd, overloading saves us memory in the system.

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
  def demo()
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

**Public attributes** are those that can be accessed inside the class and outside the class. By default, all methods and properties in a class are publicly avaliable. If we want to suggest that a method should not be used publicly, we have to declare it as private explicitly.

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

The aim is to keep it hiddent from the users and other classes. Unlike in many different languages, it is not a widespread practice in Python to keep the data members private since we do not want to create hindrances for the users. We can make members private using the double underscore **\_\_** prefix. Trying to access private attributes in the main code will generate an _error_. An example is shown below.

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

Properties and methods with the double underscore prefix are usually present to make sure that the user does not _carelessly_ access them. Python allows for free hand to the user to avoid any future complications in the code. If the user believes it is **absolutely necessary** to access a private property or a method, they can access it using the \_<ClassName> prefix for the property or method. An example of this is shown below:
  
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
