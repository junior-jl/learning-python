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
