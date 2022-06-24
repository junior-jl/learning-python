## Introduction

- Python is a high level programming language;
- The most recent version of Python is Python 3;
- It is a general purpose language;
- It is an interpreted language: the code is converted to bytecode line-by-line.

## Hello, world

- To print something on screen, we use the *print* statement.

```py
print("Hello, world")
```

- As a standart, _print_ always print a newline at the end of the string. To choose what comes at the end, we do:

```py
print("Hello, ", end="")
print("world")
```


## Comments

- Comments in Python are written with the # character.

- Docstrings are, in essence, multiline comments. They are encapsulated by triple quotes

```py
# This is a comment.
''' This 
is
also
a 
comment.
'''
```

Also... Python doesn't care if you use single or double quotes. They are equivalent.

## Data types

Python coding is way simpler when talking about data types as it doesn't need the definition of the object data type. There are three main data types:

- numbers;
- strings;
- booleans.

## Variables

'A variable is simply a name to which a value can be _assigned_.'

The simplest way to assign a value to a variable is through the '=' operator.

Variables are **mutable**.

### Naming convention

Some rules must be followed when picking the name of a variable:

- it can start with an upper or lower case letter;
- all names are case sensitive;
- a number can appear in the name, but not at the beginning;
- the underscore (\_) character can appear anywhere in the name.
- spaces are not allowed. Instead use 'snake_case';
- the name must be meaninful.

## Numbers

There are three main types of numbers in Python:

- Integers;
- Floating-point numbers;
- Complex numbers.

### Integers

Integers are positive and negative whole numbers and the amount of memory an integer occupies depends on its value. For example, 0 will take up 24 bytes whereas 1 would occupy 28 bytes.

### Floating-point numbers

Also known as _floats_, refer to positive and negative decimal numbers. A float occupies 24 bytes of memory.

In Python, 5 is considered to be an integer, while 5.0 is a float.
