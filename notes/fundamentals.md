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

- Docstrings are regular strings that are not assigned to any variables, being discarded by the interpreter. So, they are sometimes used as multiline comments. More on that later.

```py
# This is a comment.
''' This 
is
not
a 
comment, but it 
will be ignored
by the interpreter.
'''
"""This 
is
not
a 
comment, but it 
will be ignored
by the interpreter.
"""
```

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

Also known as _floats_, floats are positive and negative decimal numbers. A float occupies 24 bytes of memory.

In Python, 5 is considered to be an integer, while 5.0 is a float.

### Complex numbers

To create a complex number (numbers that have a real and an imaginary part) we use **complex()** the same way as we would use **print()**. 

```py
complex(real, imaginary)
```

Following the _electrical engineering_ convention, Python uses **j** to denote the imaginary part of a number, instead of **i**.

A complex number usually takes up 32 bytes of memory.

## Booleans

The **boolean** (or **bool**) data type allow us to choose between two values: **True** or **False**, yes, T and F capitalized.

It is used to determine whther the logic of an expression or a comparison is correct.

## Strings

A _string_ is a collection of characters closed withing single, double or triple quotation marks. It can also contain a single character or be entirely empty.

### Length of a string

The length of a string can be found by the built-in function **len()**. It indicates the number of characters in the string.

### Indexing

In a string, every character is given a numberical index based on its position. Like most programming languages, Python indexes a string from 0 to n-1 where n is its length. So, the first character in a string is on index 0.

#### Accessing characters

Each character in a string can be accessed using its index. The index must be closed withing square brackets and appended to the string.

```py
batman = "Bruce Wayne"

first = batman[0]
space = batman[5]
last = batman[len(batman) - 1]
```

If we try to execute 

```py
err = batman[len(batman)]
```

we would get an error, because the maximum index is **len(batman) - 1**.

#### Reverse indexing

We can also change our indexing convention by using negative indices. They start from the opposite end of the string. Hence, the index -1 corresponds to the last character.

### String immutability

After assigning a value to a string, trying to update it like **string[0] = 'P'** will cause a **TypeError**, because Python doesn't support item assignment in case of strings.

But, assigning a new value to string variable doesn't mean that you've changed the value.

```py
str1 = "hello"
print(id(str1))
print(str1)
str1 = "bye"
print(id(str1))
print(str1)
```

This code prints different **id's** through the **id()** method.

### ASCII vs Unicode

In Python 3, all strings are unicode. But older versions of Ppython support only ASCII characters. To use unicode in Python 2, preceding the string with a **u** is a must.

```py
string = u"This is unicode"
```

### String slicing

Slicing is the process of obtaining a portion (substring) of a string by using its indices.

Given a string, we can use the following template to slice it and obtain a substring:

```py
string[start:end]
```

The character at the **end** index will not be included in the substring obtained through this method. So, the code below

```py
my_string = "This is MY string!"
print(my_string[0:4])
print(my_string[1:7])
print(my_string[8:len(my_string)])
```

would give us

```
This
his is
MY string!
```

#### Slicing with a step

Python 3 also allows us to slice a string by defining a step through which we can skip characters in the string. The default step is 1.

The step is defined after the **end** index:

```py
string[start:end:step]
```
Code:
```py
my_string = "This is MY string!"
print(my_string[0:7])  # A step of 1
print(my_string[0:7:2])  # A step of 2
print(my_string[0:7:5])  # A step of 5
```

Output:
```
This is
Ti s
Ti
```

#### Reverse slicing

Strings can also be sliced to return a reversed substring. We would need to switch the order of the start and end indices and provide a negative step.

Code:

```py
my_string = "This is MY string!"
print(my_string[13:2:-1]) # Take 1 step back each time
print(my_string[17:0:-2]) # Take 2 steps back.
```

Output:

```
rts YM si s
!nrsY ish
```

#### Partial slicing

To specify the **start** and **end** indices is optional.

Code:
```py
my_string = "This is MY string!"
print(my_string[:8])  # All the characters before 'M'
print(my_string[8:])  # All the characters starting from 'M'
print(my_string[:])  # The whole string
print(my_string[::-1])  # The whole string in reverse (step is -1)
```

Output:
```
This is 
MY string!
This is MY string!
!gnirts YM si sihT
```

## Operators

Operators are used to perform arithmetic and logical operations on data. In general, Python's operators follow the **in-fix** or **prefix** notations.

- **In-fix** operators appear between two **operands**, so they are known as **binary** operators;
- A **prefix** operator works on one operand and appears before it. Hence, they are known as **unary** operators.

The five main operator types in Python are:

1. arithmetic operators;
2. comparison operators;
3. assignment operators;
4. logical operators;
5. bitwise operators;

### Arithmetic operators

The table below presents the basic arithmetic operators in order of **precedence**. The operator listed higher will be computed first.

**Operator** | **Purpose** | **Notation**
|:--:|:--:|:--:|
| () | Parentheses | Encapsulates the precedent operation |
| \*\* | Exponent | In-fix |
| %, \*, /, // | Modulo, multiplication, division, floor division | In-fix |
| +, - | Addition, subtraction | In-fix |

#### Addition

We can add two numbers using the + operator.

Summing an integer and a float gives us a float. Python automatically converts the integer to float, and this applies to all arithmetic operations.

#### Subtraction

We can subtract one number from other using the - operator.

#### Multiplication

We can multiply two numbers using the \* operator.

#### Division

We can divide one number by another using the / operator. And a division always results in a floating-point number.

#### Floor division

In floor division, the result is _floored_ to the nearest smaller integer, also known as **integer** division.

For floor division, we must use the // operator. Unlike normal division, floor division between two integers results in an integer.

#### Modulo

The modulo operation is done with the % operator. It returns the remainder of the division. The remainder can be a float.

### Precedence

An arithmetic expression containing different operator will be computed on the basis of **operator precedence**. Whenever operators have equal precedence, the expression is computed from the left side.

#### Parentheses

An expression which is enclosed inside parentheses will be computed first, regardless of operator precedence.

### Comparison operators

They are used to compare values in mathematical terms.

**Operator** | **Purpose** | **Notation**
|:--:|:--:|:--:|
| > | Greater than | In-fix |
| < | Less than | In-fix |
| >= | Greater than or equal to | In-fix |
| <= | Less than or equal to | In-fix |
| == | Equal to | In-fix |
| != | Not equal to | In-fix |
| is | Equal to (identity) | In-fix |
| is not | Not equal to (identity) | In-fix |

#### Comparisons

The result of a comparison is always a bool.

##### Difference between == and is, != and is not

- == and != compare the **values** of both operands;
- is and is not check if the operands are the **exact same object**.

### Assignment operators


