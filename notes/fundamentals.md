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

A category of operators which is used to assign values to a variable. 

**Operator** | **Purpose** | **Notation**
|:--:|:--:|:--:|
| = | Assign | In-fix |
| += | Add and assign | In-fix |
| -= | Subtract and assign | In-fix |
| \*= | Multiply and assign | In-fix |
| /= | Divide and assign | In-fix |
| //= | Divide, floor, and assign | In-fix |
| \*\*= | Raise power and assign | In-fix |
| %= | Take modulo and assign | In-fix |
| \|= | OR and assign | In-fix |
| &= | AND and assign | In-fix |
| ^= | XOR and assign | In-fix |
| >>= | Right-shift and assign | In-fix |
| <<= | Left-shift and assign | In-fix 

#### Assigning values

We can change variables values whenever we want. But, one thing to note is: when a variable x is assigned to another variable y, its value is **copied** into y. Hence, if we later change the value of x, y will remain unaffected.

### Logical operators

They are used to manipulate the logic of **Boolean expressions**.

**Operator** | **Purpose** | **Notation**
|:--:|:--:|:--:|
| and | AND | In-fix |
| or | OR | In-fix |
| not | NOT | Prefix |

#### Bit value

In bit terms, the value of True is 1. False corresponds to 0. So, the code:

```py
print(10 * True)
print(10 * False)
```

will output

```
10
0
```

### Bitwise operators

In programming, all data is actually made up of 0s and 1s known as **bits**. Bitwise operators allow us to perform bit-related operations on values.

**Operator** | **Purpose** | **Notation**
|:--:|:--:|:--:|
| & | Bitwise AND | In-fix |
| | | Bitwise OR | In-fix |
| ^ | Bitwise XOR | In-fix |
| ~ | Bitwise NOT | Prefix |
| << | Shift bits left | In-fix |
| >> | Shift bits right | In-fix |

## String operations

### Comparison operators

Strings are compatible with the comparison operators. Each characters has a Unicode value. When two strings have different lengths, the string which comes first in the dictionary is said to have the smaller value. So

```py
print("Slytherin" >= "Gryffindor")
```

would output True.

### Concatenation

The + operator can be used to merge two strings together. And the \* operator allows us to multiply a string, resulting in a repeating pattern.

Code: 
```py
first_half = "Bat"
second_half = "man"
full_name = first_half + second_half
print(full_name)
print(first_half * 3)
```

Output:
```
Batman
BatBatBat
```

### Search

The **in** keyword can be used to check if a particular substring exists in another string.

Code:
```py
random_string = "This is a random string"
print('of' in random_string)  # Check whether 'of' exists in randomString
print('random' in random_string)  # 'random' exists!
```

Output
```
False
True
```

## Grouping values 

In Python, the most popular way of storing multiple values together in a single variable is called a **list**. It is very similar to a string, since it is just a collection of values. However, the values can be of any type. 

### Making a list

All we have to do is enclose all the elements in square brackets and separate them with commas.

Code:
```py
my_list = [1, 2.5, "A string", True]
print(my_list)
```
Output:
```
[1, 2.5, 'A string', True]
```

Just like strings, lists can be indexed and sliced, and the **len** command works with them too.

Code:
```py
my_list = [1, 2.5, "A string", True]
print(my_list[2])
print(len(my_list))
```
Output:
```
A string
4
```

## What are conditional statements?

A conditional statement is a Boolean expression that, if **True**, executes a piece of code. They control the flow of the code and allow the computer to think. Hence, they are classified as **control structures**.

### Conditional statements in Python

To handle conditional statements, Python follows a particular convention:

```python
if conditional statement is True:
    # execute expression1
    pass
else:
    # execute expression2
    pass
```

There are three types of conditional statements in Python:

- if
- if-else
- if-elif-else

### The structure

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/178770347-5306d869-eb0d-4e90-8d3e-2c491a84b366.png"/>
</p>

The if statement is made by two parts:

1. The condition
2. The code to be executed

The colon (:) in the illustration above is necessary to specify the beginning of the if statement's code to be executed. However, the parentheses around the condition are optional. **The code to be executed is idented at least one tab to the right**.

## Indentation

Indentation is essential in Python. Statements with the same level of indentation belong to the same block of code. The convention of our indents must also be consistent throughout a block. So, if two spaces are used to make an indent, we must use two spaces for an indent in the same block.

### The flow of an if statement

An **if** statement runs like this:

**if** the **condition** holds **True**, execute the **code to be executed**. Otherwise, **skip** it and move on.

Example:

```python
num = 5

if (num == 5):  # The condition is true
    print("The number is equal to 5")  # The code is executed

if num > 5:  # The condtion is false
    print("The number is greater than 5")  # The code is not executed
```

Output:

```
The number is equal to 5
```

### Conditions with logical operators

Logical operators can be used to create more complex conditions in the **if** statement.

Example:

```python
num = 12

if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    # Only works when num is a multiple of 2, 3, and 4
    print("The number is a multiple of 2, 3, and 4")

if (num % 5 == 0 or num % 6 == 0):
    # Only works when num is either a multiple of 5 or 6
    print("The number is a multiple of 5 and/or 6")
```

In the first **if** statement, all the conditions have to be fulfilled since we are using the **and** operator. In the second one, the Boolean expression would be true if either or both of the clauses are satisfied because we are using the **or** operator.

If statements can be nested using proper indentation.

In a conditional statement, we can edit the values of our variables. Furthermore, we can create new variables.

The **if** statement is the foundation of conditional programming in Python.

### The if-else statement

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/178773988-7d1621a1-1dd5-43b1-888b-575e585fd924.png"/>
</p>

The **if-else** statement looks something like the image above. There's nothing too tricky going on here. If the **condition** turns out to be **False**, the code after the **else:** keyword is executed.

Note that the **else** keyword will be on the same indentation level as the **if** keyword.

Example:

```python
num = 60

if num <= 50:
    print("The number is less than or equal to 50")
else:
    print("The number is greater than 50")
```

Output:

```
The number is greater than 50
```

### Benefits of if-else

The code above could also be written with two **if** conditions. However, for the second **if**, we have to specify the condition again. This can be tricky when dealing with complex conditions. The **else** statement automatically handles all the situations when the **if** fails.

## Conditional expressions

Conditional expressions use the functionality of an **if-else** statement in a different way. It returns an output based on the condition we provide. It can be written in the following way:

```python
output_value1 if condition else output_value2
```

Hence, the previous code could be written as

```python
num = 60

output = "The number is less than or equal to 50" \
    if num <= 50 else "The number is greater than 50"

print(output)
```

Note that the backslash is only a line continuation character that can be used to split a single line into multiple lines.

## The if-elif-else statement

It allows us to create multiple conditions easily. The **elif** stands for **else if**, indicating that if the previous condition fails, try this one.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/178775595-60f61994-cdbe-4299-9384-e936f8b20683.png"/>
</p>

The **if** and **else** blocks will remain the same. The **elif** statement comes in between the two.

An important thing to keep in mind is that an **if-elif-else** or **if-elif** statement is not the same as multiple **if** statements. **if** statements act independently. In other words, if the conditions of two successive **if**s are **True**, both statements will be executed. On the other hand, in **if-elif-else**, when a condition evaluates to **True**, the rest of the statement's conditions are not evaluated.

Example:

```python
num = 10

if num > 5:
    print("The number is greater than 5")

if num % 2 == 0:
    print("The number is even")

if not num % 2 == 0:
    print("The number is odd")
```

Output:

```
The number is greater than 5
The number is even
```

```python
num = 10

if num > 5:
    print("The number is greater than 5")

elif num % 2 == 0:
    print("The number is even")

else:
    print("The number is odd and less than or equal to 5")
```

Output:

```
The number is greater than 5
```

## Functions

A function is a reusable set of operations.

Remember the **print()** and **len()** statements? Both always perform predefined tasks. It turns out they were functions all along!

### Why use functions?

Think of a function as a box which performs a task. We give it an input and it returns an output. The primary benefits of using functions are:

- Reusability: a function can be used over and over again. You do not have to write redundant code.
- Simplicity: functions are easy to use and make the code readable. We only need to know the inputs and the purpose of the function without focusing on the inner workings. 

An input is not even necessary. A function could perform its own computations to complete a task.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/178781768-88834257-600c-4cc4-8823-ef7862a151c6.png"/>
</p>

### Types of functions in Python

1. Built-in functions
2. User-defined functions

We've already seen some instance of built-in function such as **len()**, **min()**, and **print()**. The coolest feature, however, is that the language allows us to creat our own functions that perform the tasks we require.

### Function creation

In Python, a function can be _defined_ using the **def** keyword in the following format:

```py
def function_name (parameters):
    set of operations to be performed
    by the function
```

The **function name** is simply the name we'll use to identify the function.

The **parameters** of a function are the inputs for that function. They are optional. The body of the function contains the set of operations that the function will perform. This is always indented to the right.

### Function parameters

**Parameters** are a crucial part of the function structure. They are the means of passing data to the function. This data can be used by the function to perform a meaningful task.

When creating a function, we must define the number of parameters and their _names_. These names are only relevant to the function and won't affect variable names elsewhere in the code. Parameters are enclosed in parentheses and separated by commas.

The actual values/variables passed into the parameters are known as **arguments**.

#### Example

Let's define our own basic form of the **min()** function that simply prints the minimum. We'll name it **minimum()**:

```python
def minimum(first, second):
    if (first < second):
        print(first)
    else:
        print(second)


num1 = 10
num2 = 20

minimum(num1, num2)
```

Output:

```
10
```

Here, we are passing **num1** and **num2** to the function. The positions of the parameters are important. In the case above, the value of **num1** will be assigned to first as it was the first parameter. Similarly, the value of **num2** assigned to second.

If a function is called with lesser or more arguments than originally required, Python will throw an error.

A parameter can be any sort of data object; from a simple integer to a huge list.

## The return statement

To return something from a function, we must use the return keyword. Keep in mind that once the **return** statement is executed, the compiler ends the function. Any remaining lines of code after the return statement will not be executed.

Refactoring the **minimum()** method to reutnr the smaller value instead of printing it, we'll have the following:

```python
def minimum(first, second):
    if (first < second):
        return first
    return second


num1 = 10
num2 = 20

result = minimum(num1, num2)  # Storing the value returned by the function
print(result)
```

It is a good practice to define all our functions first and then begin the main code. Defining them first ensures that they can be used anywhere in the program safely.

## Function scope

The scope of a function means the extent to which the variables and other data items made inside the function are accessible in code.

In Python, the function scope is the function's body. Whenever a function runs, the program moves into the function scope. It moves back to the outer scope once the function has ended.

### Data Lifecycle

In Python, data created inside a function cannot be used from the outside unless it is returned by the function. Hence, when the function ends, the variables within it are realeased from memory and cannot be recovered.

The following code will result in an error:

```python
def func():
    name = "Stark"


func()
print(name)  # Accessing 'name' outside the function
```

As we can see, the **name** variable doesn't exist in the outer scope, and Python lets us know.

Similarly, the function cannot access data outside its scope unless the data is passed in as an argument.

### Altering data

When **mutable data** is passed to a function, the function can modify or alter it. These modifications will stay in effect outside the function scope as well. An example of mutable data is a list.

In the case of **immutable** data, the function can modify it, but the data will remain unchanged outside the function's scope. Examples: numbers, strings, etc.

## Built-in string functions

Python boasts a huge library of built-in functions. As we explore the language further, we'll discover many more of these functions.

### Strings

Functions that are properties of a particular entity are known as **methods**. These methods can be acessed using the dot (.) operator. The string data type has several methods associated with it. Let's look at some of them.

#### Search

An alternative for finding a substring using the **in** keyword is the **find()** method. It returns the first index at which a substring occurs in a string. If no instance of the substring is found, the method returns **-1** (this is a conventional value to represent a **None** or failure).

Suppose a **random_string**, **find()** can be used as follows:

```python
random_string.find(substring, start, end)
```

- **substring** is what we are searching for.
- **start** is the index from which we start searching in **random_string**.
- **end** is the index where we stop our search in **random_string**.

**start** and **end** are optional.

#### Replace

The **replace()** method can be used to replace a part of a string with another string. Here's the template we must use

```python
random_string.replace(substring_to_be_replaced, new_string)
```

The original string is not altered. Instead, a new string with the replaced substring is returned.

#### Changing the letter case

In Python, the letter case of a string can be easily changed using the **upper()** and **lower()** methods.

#### Joining strings

With **join()** method you can join multiple strings. Let's try it out:

```python
llist = ['a', 'b', 'c']
print('>>'.join(llist)) # joining strings with >>
print('<<'.join(llist)) # joining strings with <<
print(', '.join(llist)) # joining strings with comma and space
```

Output:

```
a>>b>>c
a<<b<<c
a, b, c
```

Over here, the **string.join(llist)** returns a single string, with the elements of **llist** separated by **string**. So, the join() method returns a new string with the given elements joined with the specified delimiter.

#### Formatting

The **format()** method can be used to format the specified value(s) and insert them in string's placeholder(s).

```python
string1 = "Learn Python {version} at {cname}".format(version = 3, cname = "Educative")
string2 = "Learn Python {0} at {1}".format(3, "Educative")
string3 = "Learn Python {} at {}".format(3, "Educative")

print(string1)
print(string2)
print(string3)
```

These three 'options' print the same thing. So the output is 

```
Learn Python 3 at Educative
Learn Python 3 at Educative
Learn Python 3 at Educative
```

The placeholders can be identified using named indexes **{cname}**, numbered indexes **{0}**, or even empty placeholders **{}**.

## Lambdas

A **lambda** is an anonymous function that returns some form of data. They are defined using the **lambda** keyword. Since they return data, it is a good practice to assign them to a variable.

### Syntax

The following syntax is used to create lambdas:

```
lambda parameters : expression
```

In the structure above, the parameters are optional.

Examples:

Below, we have a lambda that triples the value of the parameter and returns this new value.

```python
triple = lambda num : num * 3 # Assigning the lambda to a variable

print(triple(10)) # Calling the lambda and giving it a parameter
```

Output:

```
30
```

Here's a simple lambda that concatenates the first characters of three strings together:

```python
concat_strings = lambda a, b, c: a[0] + b[0] + c[0]

print(concat_strings("World", "Wide", "Web"))
```

Output:

```
WWW
```

**Limitation**: a lambda cannot have a multi-line expression. Hence, lambdas are perfect for short, single-line functions. Also, we can use conditional statements within lambdas:

```
my_func = lambda num: "High" if num > 50 else "Low"

print(my_func(60))
```

When using conditional statements in lambdas, the **if-else** pair is necessary.

Lambdas are really useful when a function requires another function as its argument.

## Functions as arguments

In Python, one function can become an argument for another function. This is useful in many cases.

Let's make a calculator function that requires the add, subtract, multiply, or divide function along with two numbers as arguments.

```python
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function


result = calculator(multiply, 10, 20)
print(result)
print(calculator(add, 10, 20))

```

Python automatically understands that the **multiply** argument is a function, and so everything works perfectly.

### Using lambdas

```python
def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function


# 10 and 20 are the arguments.
result = calculator(lambda n1, n2: n1 * n2, 10, 20)
# The lambda multiplies them.
print(result)

print(calculator(lambda n1, n2: n1 + n2, 10, 20))
```

#### More examples

The built-in **map()** function creates a **map object** using an existing list and a function as its parameters. The template for **map()** is:

```python
map(function, list)
```

The **function** will be applied, or _mapped_, to all the elements of the **list**.

Below, we'll use **map()** to double the values of an existing list:

```python
num_list = [0, 1, 2, 3, 4, 5]

double_list = map(lambda n: n * 2, num_list)

print(list(double_list))
```

Output:

```
[0, 2, 4, 6, 8, 10]
```

This creates a new list. The original list remains unchanged.

Another example is the **filter()** function. It requires a function and a list.

**filter()** _filters_ elements from a list if the elements satisfy the condition that is specified in the argument function.

The code below filters all the elements which are greater than 10.

```python
numList = [30, 2, -15, 17, 9, 100]

greater_than_10 = list(filter(lambda n: n > 10, numList))
print(greater_than_10)
```

Output:

```
[30, 17, 100]
```

The function returns a **filter object** which can be converted to a list using **list()**.  Just like **map()**, this method returns a new object without changing the original list.

## Recursion

Recursion is the process in which a function calls itself during its execution. Each recursive call takes the program one scope deeper into the function.

The recursive calls stop at the **base case**. The base case is a check used to indicate that there should be no further recursion.

### A simple example

Let's write a function which decrements a number recursively until the number becomes 0:

```python
def rec_count(number):
    print(number)
    # Base case
    if number == 0:
        return 0
    rec_count(number - 1)
    print(number)

rec_count(5)
```

Output

```
5
4
3
2
1
0
1
2
3
4
5
```

In each call, the value of **number** is printed. We then check whether the base case has been fulfilled. If not, we make a recursive call to the function with the current value decremented.

### Why use recursion?

It is a concept which many find difficult to grasp at first, but it has its advantages. For starters, it can significantly reduce the runtime of certain algorithms, which makes the code more efficient.

Recursion also allows us to easily solve many problems related to **graphs** and **trees** (will be treated later). It is also important in search algorithms.

However, some caution must be taken when using recursion. If we don't specify an appropriate base case or update our arguments as we recurse, the program will reach **infinite recursion** and crash.

### A complex example

The Fibonacci sequence is a popular series of numbers in mathematics, where every number is the sum of the two numbers before it. The first two terms in the series are 0 and 1:

```
0 1 1 2 3 5 8 13
```

Let's write a function which takes in a number, n, and returns the **nth** number in the Fibonacci sequence. It is important to note that for the following example, we will be trating all inputs **less than 1** as incorrect and therefore, our input will start from 1. So, if **n == 6**, the function will return 5.

First, we handle our base cases. We know that the first two values are always 0 and 1, so that is where we can stop our recursive calls. If **n** is larger than 2, then it will be the sum of the two values before it.
