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
- The use of classes makes it easier to maintain differnt parts of an application since it is easier to make changes in classes.
