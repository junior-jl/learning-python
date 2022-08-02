# Data structures and algorithms in Python

A data structure is a way to storing and organizing data according to a certain format or structure.

## Data structures in Python

Python is equipped with several built-in data structures to help us efficiently handle large amounts of data.

The four primary built-in data structures offered in Python3 are:

- List
- Tuple
- Dictionary
- Set

### Lists

#### Structure

The list is perhaps the most commonly used data structure in Python. It allows us to store elements of different data types in one container.

The contents of a list are enclosed by square brackets, [ ].

Lists are _ordered_, like strings. Elements are stored linearly at a specific index.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180096114-8cc3dd64-ed28-4c20-96dd-ef090c80ab75.png"/>
</p>

A string was a collection of characters indexed in a linear fashion. A list is the same except that it can contain any type of data, even another list!

#### Creating a list

```python
jon_snow = ["Jon Snow", "Winterfell", 30]
print(jon_snow)

# Indexing
print(jon_snow[0])

# Length
print(len(jon_snow))

```

Output:

```
['Jon Snow', 'Winterfell', 30]
Jon Snow
3
```

The beauty of lists lies in the fact that we are not bound to one type of data. Lists are mutable, which further expands their functionality:

```python
jon_snow = ["Jon Snow", "Winterfell", 30]
print(jon_snow[2])
jon_snow[2] += 3
print(jon_snow[2])
```

#### Using range()

A range can further be converted into a list by using the list() casting.

```python
num_seq = range(0, 10)  # A sequence from 0 to 9
num_list = list(num_seq)  # The list() method casts the sequence into a list
print(num_list)

num_seq = range(3, 20, 3)  # A sequence from 3 to 19 with a step of 3
print(list(num_seq))
```

#### List-ception!

Here's an example of lists inside another list:

```python
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners)
```

Output:

```
[[2006, 'Italy'], [2010, 'Spain'], [2014, 'Germany'], [2018, 'France']]
```

##### Sequential indexing

To access the elements of a list or a string which exists inside another list, we can use the concept of sequential indexing.

```python
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[1])
print(world_cup_winners[1][1])  # Accessing 'Spain'
print(world_cup_winners[1][1][0])  # Accessing 'S'
```

#### Merging lists

The simplest way is to use the + operator like we did for strings:

```python
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
merged_list = part_A + part_B
print(merged_list)
```

Output:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Alternatively, we could use the **extend()** property of a list to add the elements of one list at the end of another.

```python
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)
```

#### Common list operations

##### Adding elements

The **append()** method can be used to add a new element at the end of a list.

```
a_list.append(newElement)
```

Example:

```python
num_list = []  # Empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)
```

In the code above, we create an empty list. This can always be done by simply using empty square brackets [ ].

To add an element at a particular index in the list, we can use the **inser()** method.

```
aList.insert(index, newElement)
```

If a value already exists at that index, the whole list from that value onwards will be shifted one step to the right:

```python
num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
print(num_list)
```

##### Removing elements

The counterpart of **append()** is **pop()**, which removes the last element from the list. We can store this popped element in a variable.

```python
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)
print(houses)
```

If we need to delete a particular value from a list, we can use the **remove()** method.

```
aList.remove(element_to_be_deleted)
```

```python
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
print(houses)
houses.remove("Ravenclaw")
print(houses)

# For nested lists
populations = [["Winterfell", 10000], ["King's Landing", 50000],
               ["Iron Islands", 5000]]
print(populations)
populations.remove(["King's Landing", 50000])
print(populations)
```

Output:

```
['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin', 'Ravenclaw']
['Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']
[['Winterfell', 10000], ["King's Landing", 50000], ['Iron Islands', 5000]]
[['Winterfell', 10000], ['Iron Islands', 5000]]
```

##### List slicing

It is used to obtain a portion of a list given the start and end indices. Slicing a list gives us a sublist:

```python
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0::2])
```

Output:

```
[3, 4, 5]
[1, 3, 5, 7]
```

##### Index search

With lists its really easy to access a value through its index. However, the opposite operation is also possible where we can find the index of a given value.

For this, we’ll use the **index()** method:

```python
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))  # It is at the 2nd index
```

Output : 2

If we just want to verify the existence of an element in a list, we can use the in operator:

```python
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print("London" in cities)
print("Moscow" not in cities)
```

Output:

```
True
True
```

##### List sort

A list can be sorted in ascending order using the **sort()** method. Sorting can be done alphabetically or numerically depending on the content of the list:

```python
num_list = [20, 40, 10, 50.4, 30, 100, 5]
num_list.sort()
print(num_list)
```

Output:

```
[5, 10, 20, 30, 40, 50.4, 100]
```

#### List comprehension

List comprehension is a technique that uses a for loop and a condition to create a new list from an existing one. The result is always a new list, so it's a good practice to assign list comprehension to a new variable.

##### Structure

```
[expression for loop if condition]
```

- The **expression** is an operation used to create elements in the new list.
- The **for** **loop** will iterate an existing list. The iterator will be used in the **expression**.
- New elements will only be added to the new list when the **if condition** is fulfilled. This component is optional.

Example:

Let's create a new list whose values are the doubles of the values of an existing list.

```python
nums = [10, 20, 30, 40, 50]
nums_double = []

for n in nums:
  nums_double.append(n * 2)
  
```

Let's break down the loop above into the three components of a list comprehension. The expression is equivalent to ** n \* 2** since it's used to create each value in the new list.

Our for loop is **for n in nums**, where **n** is the iterator.

An if condition doesn't exist in this case.

Converting...

```python
nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums]

```

We could add a condition:

```python
nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums if n % 4 == 0]

```

##### Using multiple lists

List comprehension can also be performed on more than one list. The number of for loops in the comprehension will correspond to the number of lists we're using.

Let's write a list comprehension which creates tuples out of the values in two lists when their sum is greater than 100. These tuples are the elemnents of the new list.

```python
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]
```

### Tuples

#### Structure

A tuple is very similar to a list, except for the fact that its contents cannot be changed. In other words, a tuple is **immutable**. However, it can contain mutable elements like a list. These elements can be altered.

The contents of a tuple are enclosed in parentheses, (). They are also ordered.


<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180579633-4eb93f46-e11d-4f45-9c10-244b48abe5bb.png"/>
</p>


#### Creating a tuple

Tuples can be created similar to lists. All the indexing and slicing operations apply to it as well:

```python
car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])
```

Output:

```
('Ford', 'Raptor', 2019, 'Red')
4
Raptor
(2019, 'Red')
```

#### Merging tuples

Tuples can be merged using the + operator.

#### Nested tuples

Instead of merging two tuples, we can create a new tuple with tuples as its members.

```python
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)
```

Output:

```
(('Batman', 'Bruce Wayne'), ('Wonder Woman', 'Diana Prince'))
```

#### Search

We can check whether an element exists in a tuple by using the **in** operator as well.

The **index()** function can give us the index of a particular value:

```python
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo"))
```

Output: 3

#### Immutability

Since tuples are immutable, we can't add or delete elements from them. Furthermore, it isn't possible to append another tuple to an existing tuple.

### Dictionaries

#### Structure

It has a slightly more complex structure.

A **dictionary** stores **key-value** pairs, where each unique key is an **index** which holds the value associated with it.

Dictionaries are **unordered**. In Python, we must put the dictionary's content inside curly brackets, {}.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180580056-5ffc3f1a-6a14-4034-bf29-95ac2293a99f.png"/>
</p>

A key-value pair is written in the following format:

```
key:value
```

#### Creating a dictionary

Let's create an empty dictionary and a simple **phone_book** using the dictionary data structure.

```python
empty_dict = {} # Empty dictionary
print(empty_dict)

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book) 
```

Output:

```
{}
{'Ghostbusters': 44678, 'Batman': 468426, 'Cersei': 237734}
```

Note that since the dictionary is an unordered data structure, the order of the output will not necessarily match the order in which we wrote the entries. Key-value pairs are accessed in a random or unordered manner. 

The dictionary above could also be written in the same line. Dividing it into lines only increases readability.

#### The dict() constructor

Don't worry about the term constructor for now. Think of it as an operation which gives us a dictionary.

If our keys are simple strings without special characters, we can create entries in the constructor. In that case, values will be assigned to keys using the = operator. A popular practice is to create an empty dictionary and add entries later.

Let's refactor the example above to make it work with dict().

```python
empty_dict = dict()  # Empty dictionary
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book)
```

The **keys** and **values** can have any of the basic data types or structures we've studied. Two keys can have the same value. However, it is crucial that all keys are unique.

#### Accessing values

We can access a value by enclosing its key in square brackets [ ]. Alternatively, we can use the get() method as follows:

```
a_dictionary.get(key)
```

Let's build upon our previous example:

```python
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))
```

Output:

```
237734
44678
```

#### Dictionary operations

##### Adding/Updating entries

We can add entries in a dictionary by simply assigning a value to a key. Python automatically creates the entry. If a value already exists at this key, it will be updated:

```python
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

phone_book["Godzilla"] = 46394  # New entry
print(phone_book)

phone_book["Godzilla"] = 9000  # Updating entry
print(phone_book)
```

Output:

```
{'Ghostbusters': 44678, 'Batman': 468426, 'Cersei': 237734}
{'Ghostbusters': 44678, 'Batman': 468426, 'Godzilla': 46394, 'Cersei': 237734}
{'Ghostbusters': 44678, 'Batman': 468426, 'Godzilla': 9000, 'Cersei': 237734}
```

##### Removing entries

To delete an entry, we can use the **del** keyword.

```python
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

del phone_book["Batman"]
print(phone_book)
```

If we want to use the deleted value, the pop() or popitem() methods would work better:

```python
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

# Removes and returns the last inserted pair, as a tuple
# In Python versions before 3.7, popitem() removes and returns the random item
lastAdded = phone_book.popitem()
print(lastAdded)
```

Output:

```
{'Batman': 468426, 'Cersei': 237734, 'Ghostbusters': 44678}
{'Batman': 468426, 'Ghostbusters': 44678}
237734
('Ghostbusters', 44678)
```

##### Length of a dictionary

Similar to lists and tuples, we can calculate the length of a dictionary using **len()**:

```python
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(len(phone_book))
```

##### Checking key existence

The in keyword can be used to check if a key exists in a dictionary.

##### Copying contents

To copy the contents of one dictionary to another, we can use the **update()** operation.

```python
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)
```

##### Dictionary comprehension

It works very similar to list comprehensions. However, to iterate the dictionary, we'll use the **dict.items()** operation which turns a dictionary into a list of **(key, value)** tuples. Here's a simple example where the keys of the original dictionary are squared and '!' is appended to each string value:

```python
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)
```

Output:

```
{1: 'Gryffindor', 2: 'Slytherin', 3: 'Hufflepuff', 4: 'Ravenclaw'}
{16: 'Ravenclaw!', 1: 'Gryffindor!', 4: 'Slytherin!', 9: 'Hufflepuff!'}
```

### Sets

A set is an unordered collection of data items.

The data is not indexed, so we can't access elements using indices or get(). This is probably the simplest data structure in Python. We can think of it as a bag containing random items.


<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180581245-f7adef2e-09de-4275-90f0-460cdf5a2385.png"/>
</p>

Mutable data structures like lists or dictionaries can't be added to a set. However, adding a tuple is perfectly fine. A set is perfect when we simply need to keep track of the existence of items.

It doesn't allow duplicates, which means that we can convert another data structure to a set to remove any duplicates.

#### Creating a set

The contents of a set are encapsulated in curly brackets, {}. Like all data structures, the length of a set can be calculated using len().

#### The set() constructor

It is an alternate way of creating sets.

```python
empty_set = set()
print(empty_set)

random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)
```

Output:

```
set()
{1408, (True, False), 3.142, 'Educative'}
```

#### Adding elements

To add a single item, we can use the **add()** method. To add multiple items, we'd have to use **update()**.

The input for update() must be another set, list, tuple, or string.

```python
empty_set = set()
print(empty_set)

empty_set.add("hi")
print(empty_set)

empty_set.update([2, 3, 4, 5, 6], "hi")
print(empty_set)
```

Output:

```
set()
{'hi'}
{2, 3, 4, 5, 6, 'hi', 'i', 'h'}
```

#### Deleting elements

The **discard()** or **remove()** operations can be used to delete a particular item from a set.

```python
random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

random_set.discard(1408)
print(random_set)

random_set.remove((True, False))
print(random_set)
```

The **remove()** method generates an error if the item is not found, unlike the **discard()** method.

#### Iterating a set

The **for** loop can be used on unordered data structures like sets. However, we wouldn’t know the order in which the iterator moves meaning elements will be picked randomly.

In the example below, we’ll take the elements of a set and append them to a list if they are odd:

```python
odd_list = [1, 3, 5, 7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

print(unordered_set)

for num in unordered_set:
    if(not num % 2 == 0):
        odd_list.append(num)

print(odd_list)
```

Output:

```
{9, 10, 11, 12, 13, 14, 15, 16, 17}
[1, 3, 5, 7, 9, 11, 13, 15, 17]
```

#### Set theory operations

- Union
- Intersection
- Difference

##### Union

A union of two sets is the collection of all unique elements from both sets.


<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180581675-facb74a2-505f-4c48-979d-653b9ceb9b4b.png"/>
</p>

In Python, union can be performed using either the pipe operator \|, or the **union()** method.

```python
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))
```

Output:

```
{1, 2, 3, 4, 'a', 'd', 'c', 'b'}
{1, 2, 3, 4, 'a', 'd', 'c', 'b'}
{'a', 1, 2, 3, 4, 'd', 'c', 'b'}
```

##### Intersection

The intersection of two sets is the collection of unique elements which are common between them.

In Python, intersection can be performed using either the \& operator or the **intersection()** method.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180581806-b5d4ceed-3516-46fa-8fc8-0eeec540e245.png"/>
</p>

```python
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

print(set_A & set_B)
print(set_A.intersection(set_B))
print(set_B.intersection(set_A))
```

Output:

```
{2, 4}
{2, 4}
{2, 4}
```

##### Difference

The difference between two sets is the collection of all unique elements present in the first set but not in the second.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180581868-ec67c958-dff5-47d9-bb05-40f60974bef7.png"/>
</p>

          
In Python, the difference between two sets can be found using either the - operator or the **difference()** method.

```python
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}


print(set_A - set_B)
print(set_A.difference(set_B))

print(set_B - set_A)
print(set_B.difference(set_A))
```

Output:

```
{1, 3}
{1, 3}
{16, 8}
{16, 8}
```

### Data structure conversions

#### Explicit conversion

The template for explicitly converting from one data structure to another is as follows:

```
destination_structure_name(source_structure_object)
```

#### Converting to a list

We can converte a tuple, set, or dictionary to a list using the **list()** constructor. In the case of a dictionary, only the keys will be converted to a list.

```python
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_list = list(star_wars_tup)  # Converting from tuple
print(star_wars_list)

star_wars_list = list(star_wars_set)  # Converting from set
print(star_wars_list)

star_wars_list = list(star_wars_dict)  # Converting from dictionary
print(star_wars_list)
```

Output:

```
('Anakin', 'Darth Vader', 1000)
{1000, 'Anakin', 'Darth Vader'}
{1: 'Anakin', 2: 'Darth Vader', 3: 1000}
['Anakin', 'Darth Vader', 1000]
[1000, 'Anakin', 'Darth Vader']
[1, 2, 3]
```

We can also use the **dict.items()** method to convert a dictionary into an iterable of **(key, value)** tuples. This can further be cast into a list of tuples using **list()**:

```python
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_list = list(star_wars_dict.items())
print(star_wars_list)
```

Output:

```
{1: 'Anakin', 2: 'Darth Vader', 3: 1000}
[(1, 'Anakin'), (2, 'Darth Vader'), (3, 1000)]
```

#### Converting to a tuple

Any data structure can be converted to a tuple using the **tuple()** constructor. In the case of a dictionary, only the keys will be converted to a tuple.

```python
star_wars_list = ["Anakin", "Darth Vader", 1000]
print(star_wars_list)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_tup = tuple(star_wars_list)  # Converting from list
print(star_wars_tup)

star_wars_tup = tuple(star_wars_set)  # Converting from set
print(star_wars_tup)

star_wars_tup = tuple(star_wars_dict)  # Converting from dictionary
print(star_wars_tup)
```

Output:

```
['Anakin', 'Darth Vader', 1000]
{1000, 'Darth Vader', 'Anakin'}
{1: 'Anakin', 2: 'Darth Vader', 3: 1000}
('Anakin', 'Darth Vader', 1000)
(1000, 'Darth Vader', 'Anakin')
(1, 2, 3)
```

#### Converting to a set

The **set()** constructor can be used to create a set out of any other data structure. In the case of a dictionary, only the keys will be converted to a set.

#### Converting to a dictionary

**The dict()** constructor cannot be used in the same way as the others because it requires key-value pairs. Hence, the data must be stored in a format where **pairs** exist.

```python
star_wars_list = [[1,"Anakin"], [2,"Darth Vader"], [3, 1000]]
print (star_wars_list)
star_wars_tup = ((1, "Anakin"), (2, "Darth Vader"), (3, 1000))
print (star_wars_tup)
star_wars_set = {(1, "Anakin"), (2, "Darth Vader"), (3, 1000)}
print (star_wars_set)

star_wars_dict = dict(star_wars_list) # Converting from list
print(star_wars_dict)

star_wars_dict = dict(star_wars_tup) # Converting from tuple
print(star_wars_dict)

star_wars_dict = dict(star_wars_set) # Converting from set
print(star_wars_dict)
```

Output:

```
[[1, 'Anakin'], [2, 'Darth Vader'], [3, 1000]]
((1, 'Anakin'), (2, 'Darth Vader'), (3, 1000))
{(3, 1000), (2, 'Darth Vader'), (1, 'Anakin')}
{1: 'Anakin', 2: 'Darth Vader', 3: 1000}
{1: 'Anakin', 2: 'Darth Vader', 3: 1000}
{1: 'Anakin', 2: 'Darth Vader', 3: 1000}
```

## Stack

The data structure stack is very similar to a physical stack that you'd most likely be familiar with. The stack data structure allows us to place any programming artifact, variable or object on it.

### Stack operations

#### Push

The operation to insert elements in a stack is called **push**. When we push the book on a stack, we put the book on the previous _top_ element, which means that the new book becomes the _top_ element.

#### Pop

Popping is when we take the top book of the stack and put it down. This implies that when we remove an element from the stack, the stack follows the _First-in, Last out_ property. This means that the top element is removed when we perform the pop operation.

#### Peek

Another thing that we can do is view the top element of the stack so we can ask the data structure: "What's the top element?" and it can give that to us using the _peek_ operation.

Now we are going to create a stack class, and the constructor of the class is going to initialize a Python list.

```python
"""
Stack Data Structure.
"""
class Stack():
  def __init__(self):
    self.items = []
```

We are defining a class variable **items**, and assigning it to an empty list. **self.items** is created when we create a stack object so now let's create the **push** method.

```python
"""
Stack Data Structure
"""
class Stack():
  def __init__(self):
    self.items = []
  
  def push(self, item):
    self.items.append(item)
   
```

Implementing the pop method:

```python
"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
```

We also create a method called **get_stack()** that will return the **items** list.

```python
"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items
```

Another helpful method we could have is a method called **is_empty**. It will return whether or not the stack is empty.

```python
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
        
    def get_stack(self):
        return self.items
        
```

To finish, we have the peek operation which tells us the topmost element of the stack.

```python
"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items
       
```

#### Determine if brackets are balanced

A balanced set of brackets is one where the number and type of opening and closing brackets match and that is also properly nested within the string of brackets.

##### Examples of balanced brackets

- { }
- { } { }
- ( ( { [ ] } ) )

##### Examples of unbalanced brackets

- ( ( )
- { { { ) } ]
- `[ ] [ ]` ] ]

##### Algorithm



<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180617811-e33d4334-247c-4f9d-9a50-09b8cd13cce7.png"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180617819-52bcda5f-b882-4c7f-9738-36a888be90dd.png"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180617824-6413878e-f84d-4d2e-8bbe-3e811839fcf8.png"/>
</p>

- We iterate through the characters of the string.
- If we get an opening bracket, push it onto the stack.
- If we encounter a closing bracket, pop off an element from the stack and match it with the closing bracket. If it is an opening bracket and of the same type as the closing bracket, we conclude it is a successful match and move on. If it’s not, we will conclude that the set of brackets is not balanced.
- The stack will be empty at the end of iteration for a balanced example of brackets while we’ll be left with some elements in the stack for an unbalanced example.

###### Special case

Example: ) )

In the case described above we don't have an opening parenthesis, but we encounter a closing parenthesis. In this case, we immediately know that the string does not have a balanced usage of brackets.

Let's implement the algorithm in Python, starting with the **is_paren_balanced** function:

```python
def is_paren_balanced(paren_string):
  s = Stack()
  is_balanced = True
  index = 0
  
  while index < len(paren_string) and is_balanced:
    paren = paren_string[index]
    if paren in "([{":
      s.push(paren)
    else:
      if s.is_empty():
        is_balanced = False
        break
      else:
        top = s.pop()
        if not is_match(top, paren)
          is_balanced = False
          break
    index += 1
    
  if s.is_empty() and is_balanced:
    return True
  else:
    return False
    
```

Let's implement the **is_match** function now:

```python
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False
        
```        

#### Reverse string

In Python, you can reverse a string very easily. For example,

```python
input_str = "Educative"
print(input_str[::-1])
```

##### Implementation with stack

```python
from stack import Stack
def reverse_string(stack, input_str):
  for i in range(len(input_str)):
    stack.push(input_str[i])
  rev_str = ""
  while not stack.is_empty():
    rev_str += stack.pop()

  return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))
```

Output: `Welcome to Educative!`

I made a little modification in the code and it worked as well.

```python
from stack import Stack
def reverse_string(input_str):
  stack = Stack()
  for i in range(len(input_str)):
    stack.push(input_str[i])
  rev_str = ""
  while not stack.is_empty():
    rev_str += stack.pop()

  return rev_str

input_str = "!evitacudE ot emocleW"
print(reverse_string(input_str))
```

### Singly linked lists

We will go over the following different types of linked lists and implement them in Python:

1. Singly linked lists
2. Doubly linked lists
3. Circular linked lists

Below is a simple depiction of a singly linked list:

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180621233-8912fb42-8d41-4819-8339-68a199fc434c.png"/>
</p>

#### Structure

Every linked list consists of nodes. Every node has two components:

1. Data
2. Next

- The _data_ component allows a node in the linked list to store an element of data that can be of type string, character, number or any other type of object.
- The _next_ component in every node is a pointer that points from one node to another.
- The start of the linked list is referred to as the **head**. It is a pointer that points to the beginning of the linked list, so if we want to traverse the linked list to obtain or access an element of the linked list, we'll start from head and move along.
- The last component of a singly linked list is a notion of null. This null idea terminates the linked list. In Python, we call this **None**. The last node in a singly linked list points to a null object, and that tells you that it's the end of the linked list.

#### Arrays vs. linked lists

|                                                   | Arrays | Linked lists |
|:-------------------------------------------------:|:------:|:------------:|
| Insertion/deletion at the beginning given a value |  O(n)  |     O(1)     |
|                   Access element                  |  O(1)  |     O(n)     |
|                 Contiguous memory                 |   Yes  |      No      |

##### Insertion/deletion

The insertion/deletion operation is in O(n) operations for insertion/deletion of value at the beginning of the array. Now think if we are given an array and a value to insert at the beginning of an array. For insertion, we have to shift all the elements in the array to the right. Due to the shifting, the time complexity is O(n). The same is valid for deletion. 

Inserting a node at the head of a linked list given the head node is a constant-time operation as we need to change the orientation of a few pointers. If we are given the exact pointer after which we have to insert another node, it will be a constant-time operation.

##### Accessing elements

Accessing any element given an index in arrays is better than accessing nth elements in linked lists. It is a constant time operation to access elements in arrays. This is because arrays are contiguous. 

In a linked list, if we want to access an element, we need to start from the head pointer and traverse the entire linked list before we can get to it.

##### Contiguous memory

Arrays are contiguous in memory which allows the access time to be constant, whereas, in linked lists, you do not have the luxury of contiguous memory.

#### Implementation

Now let's go ahead and create our classes in Python:

- Node class
- LinkedList class

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    
```

##### Insertion

We'll implement the class methods to insert elements in a linked list:

1. append
2. prepend
3. insert_after_node

##### Append

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180624847-375ad82a-6337-40b7-9fef-0ab6bc5b5963.png"/>
</p>

The append method will insert an element at the end of the linked list.

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    
  def append(self, data):
    new_noed = Node(data)
    
```

###### Empty linked list case

For the append method, we also need to cater for the case if the linked list is empty.

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
     
```     

###### Non-empty linked list case

We have new_node that we create, and we want to append it to the linked list. We can start from the head pointer and then move through each of the nodes in the linked list unitl we get to the end, i.e., None. Once we arrive at the location that we want to insert the new_node at, we insert as shown below:

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node
    
```

##### print_list()

It is a class method, so it will take self as an argument and print out the entries of a linked list.

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def print_list(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data)
      cur_node = cur_node.next

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node
```

##### Prepend

The prepend method will insert an element at the beginning of the linked list.

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def print_list(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data)
      cur_node = cur_node.next

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def prepend(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node
```

##### Insert after node

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180625067-dfe1fcdb-b32e-433b-8d93-cbd6c6388d11.png"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/180625073-f7a55f99-f26d-4bba-baed-30d6b90cd4d8.png"/>
</p>

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def print_list(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data)
      cur_node = cur_node.next

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def prepend(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node
  
  def insert_after_node(self, prev_node, data):
    if not prev_node:
      print("Previous node does not exist.")
      return
    new_node = Node(data)

    new_node.next = prev_node.next
    prev_node.next = new_node
```

##### Deletion by value

To solve this problem, we need to handle two cases:

1. Node to be deleted is head
2. Node to be deleted is not head

###### Case of deleting head

```python
def delete_node(self, key):
  
  cur_node = self.head

  if cur_node and cur_node.data == key:
    self.head = cur_node.next 
    cur_node = None
    return
```

###### Case of deleting node other than the head

For example, to delete Node B:

1. previous node of Node B will point to the next node of Node B
2. delete node B

```py
def delete_node(self, key):
  
  cur_node = self.head

  if cur_node and cur_node.data == key:
    self.head = cur_node.next 
    cur_node = None
    return
  
  prev = None
  while cur_node and cur_node.data != key:
    prev = cur_node
    cur_node = cur_node.next 

  if cur_node is None:
    return 
  
  prev.next = cur_node.next
  cur_node = None
```

##### Deleting by position

We need to consider two cases:

1. Node to be deleted is at position 0
2. Node to be deleted is not at position 0

The overall logic will stay the same as in the previous lesson except that we'll change the code a bit to cater to position rather than a key.

```python
def delete_node_at_pos(self, pos):
  if self.head:
    cur_node = self.head
    if pos == 0:
      self.head = cur_node.next
      cur_node = None
      return

    prev = None
    count = 0
    while cur_node and count != pos:
        prev = cur_node 
        cur_node = cur_node.next
        count += 1

    if cur_node is None:
        return 

    prev.next = cur_node.next
    cur_node = None
    
```

##### Length

###### Iterative implementation

```py
def len_iterative(self):
  count = 0
  cur_node = self.head
  while cur_node:
    count += 1
    cur_node = cur_node.next
  return count
  
```

###### Recursive implementation

```py
def len_recursive(self, node):
  if node is None:
    return 0
  return 1 + self.len_recursive(node.next)
```

If we want to calculate the length of the whole linked list, we have to pass the start of the linked list as the node.

#### Node swap

One way to solve this is by iterating the linked list and keeping track of certain pieces of information that are going to be helpful.

We can start from the first node, i.e., the head node of the linked list and keep track of both the previous and the current node.

There are two cases that we'll have to cater for:

1. Node 1 and Node 2 are not head nodes
2. Either node 1 or node 2 is a head node.

```python
def swap_nodes(self, key_1, key_2):

  if key_1 == key_2:
    return 

  prev_1 = None 
  curr_1 = self.head 
  while curr_1 and curr_1.data != key_1:
    prev_1 = curr_1 
    curr_1 = curr_1.next

  prev_2 = None 
  curr_2 = self.head 
  while curr_2 and curr_2.data != key_2:
    prev_2 = curr_2 
    curr_2 = curr_2.next

  if not curr_1 or not curr_2:
    return 

  if prev_1:
    prev_1.next = curr_2
  else:
    self.head = curr_2

  if prev_2:
      prev_2.next = curr_1
  else:
      self.head = curr_1

  curr_1.next, curr_2.next = curr_2.next, curr_1.next
```

The last line swaps the **next** of **curr_1** and the **next** of **curr_2** using Python shorthand.

#### Reverse

##### Iterative implementation

The key idea is reversing the orientation of the arrows. 

```py
def reverse_iterative(self):
  prev = None
  cur = self.head
  while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
  self.head = prev
  
```  

##### Recursive implementation

```py
def reverse_recursive(self):

  def _reverse_recursive(cur, prev):
    if not cur:
      return prev

    nxt = cur.next
    cur.next = prev
    prev = cur 
    cur = nxt 
    return _reverse_recursive(cur, prev)

  self.head = _reverse_recursive(cur=self.head, prev=None)
```

The crux of any recursive solution is as follows:

- We implement the base case.
- We agree to solve the simplest problem, which in this case is to reverse just one pair of nodes.
- We defer the remaining problem to a recursive call, which is the reversal of the rest of the linked list.

#### Merge two sorted linked lists

To solve this problem, we'll use two pointers (p and q) which will each initially point to the head node of each linked list. There will be another pointer, s, that will point to the smaller value of data of the nodes that p and q are pointing to. Once s points to the smaller value of the data of nodes that p and q point to, p or q will move on to the next node in their respective linked list. If s and p point to the same node, p moves forward; otherwise q moves forward. The final merged linked list will be made from the nodes that s keeps pointing to.

```py
def merge_sorted(self, llist):

  p = self.head 
  q = llist.head
  s = None

  if not p:
      return q
  if not q:
      return p

  if p and q:
      if p.data <= q.data:
          s = p 
          p = s.next
      else:
          s = q
          q = s.next
      new_head = s 
  while p and q:
      if p.data <= q.data:
          s.next = p 
          s = p 
          p = s.next
      else:
          s.next = q
          s = q
          q = s.next
  if not p:
      s.next = q 
  if not q:
      s.next = p

  self.head = new_head     
  return self.head
```

#### Remove duplicates

```py
def remove_duplicates(self):
  cur = self.head
  prev = None
  dup_values = dict()

  while cur:
    if cur.data in dup_values:
      # Remove node:
      prev.next = cur.next
      cur = None
    else:
      # Have not encountered element before.
      dup_values[cur.data] = 1
      prev = cur
    cur = prev.next
    
```

#### Nth-to-last node

If N equals 2, we want to get the second to last node from the linked list.

##### Solution 1

1. Calculate the length of the linked list
2. Count down from the total length until n is reached.

```py
def print_nth_from_last(self, n):
  total_len = self.len_iterative()
  
  cur = self.head 
  while cur:
    if total_len == n:
      print(cur.data)
      return cur.data
    total_len -= 1
    cur = cur.next
  if cur is None:
    return  
```

##### Solution 2

There will be a total of two pointers, p and q:

- p will point to the head node.
- q will point n nodes beyond head node.
- we'll move these pointers along with the linked list one node at a time. When q reach None, we check where p is pointing, as that is the node we want.

```python
def print_nth_from_last(self, n):
    p = self.head
    q = self.head

    if n > 0:
        count = 0
        while q:
            count += 1
            if(count>=n):
                break
            q = q.next
            
        if not q:
            print(str(n) + " is greater than the number of nodes in list.")
            return

        while p and q.next:
            p = p.next
            q = q.next
        return p.data
    else:
        return None
```

I implemented a third solution that might take more time, but it works:

```py
self.reverse_recursive()
i = self.head
c = 1
while c is not n:
  i = i.next
  c += 1
if i:
  self.reverse_recursive()
  return i.data
else:
  self.reverse_recursive()
  return None
```

#### Count occurrences

##### Iterative implementation

```py
def count_occurences_iterative(self, data):
  count = 0
  cur = self.head
  while cur:
      if cur.data == data:
          count += 1
      cur = cur.next
  return count 
```

##### Recursive implementation

```py
def count_occurences_recursive(self, node, data):
  if not node:
      return 0 
  if node.data == data:
      return 1 + self.count_occurences_recursive(node.next, data)
  else:
      return self.count_occurences_recursive(node.next, data)
      
```      

#### Rotate

To solve this problem, we make use of two pointers p and q. p points to the pivot node while q points to the end of the linked list. Once the pointers are rightly positioned, we update the last element, and instead of making it point to None, we make it point to the head of the linked list. After this step we achive a circular linked list. Now we have to fix the end of the linked list. THerefore, we update the head of the linked list, which will be the next element after the pivot node, as the pivot node has to be the last node. Finally, we sett **p.next** to **None**, which breaks up the circular linked list and makes **p** the last element of our rotated linked list.

```py
def rotate(self, k):
  if self.head and self.head.next:
    p = self.head 
    q = self.head 
    prev = None
    count = 0
    
    while p and count < k:
        prev = p
        p = p.next 
        q = q.next 
        count += 1
    p = prev
    while q:
        prev = q 
        q = q.next 
    q = prev 

    q.next = self.head 
    self.head = p.next 
    p.next = None
    
```    

#### Is palindrome

Check if the data held at each of the nodes in the linked list can be read forward from the head or backward from the tail to generate the same content.

##### Solution 1

```python
def is_palindrome(self):
  # Solution 1:
  s = ""
  p = self.head
  while p:
    s += p.data
    p = p.next
  return s == s[::-1]
```

##### Solution 2

We could solve this problem using a 'stack'.

```py
def is_palindrome(self):
  # Solution 2:
  p = self.head
  s = []
  while p:
    s.append(p.data)
    p = p.next
  p = self.head
  while p:
    data = s.pop()
    if p.data != data:
      return False
    p = p.next
  return True
```

##### Solution 3

Using two pointers.

```py
def is_palindrome(self):
  if self.head:
    p = self.head 
    q = self.head 
    prev = []
    
    i = 0
    while q:
      prev.append(q)
      q = q.next
      i += 1
    q = prev[i-1]

    count = 1

    while count <= i//2 + 1:
      if prev[-count].data != p.data:
        return False
      p = p.next
      count += 1
    return True
  else:
    return True
```

### Circular linked lists

#### Introduction and Insertion

Circular linked list: same principle as the singly linked list, except for the fact that the next of the tail node is the head node instead of null.

<p align="center">
  <img src = "https://user-images.githubusercontent.com/69206952/181852445-f0a3ab9f-189c-4846-acd0-9cd3cd63cf21.png"/>
</p>

```py
class Node:
    def __init__(self, data):
      self.data = data
      self.next = None


class CircularLinkedList:
    def __init__(self):
      self.head = None 

    def prepend(self, data):
      pass

    def append(self, data):
      pass

    def print_list(self):
      pass
      
```      

##### append

Appending to a circular linked list implies inserting the new node after the node that was previously pointing to the head of the linked list.

```py
def append(self, data):
  if not self.head:
      self.head = Node(data)
      self.head.next = self.head
  else:
      new_node = Node(data)
      cur = self.head
      while cur.next != self.head:
          cur = cur.next
      cur.next = new_node
      new_node.next = self.head
      
```

##### print_list

```py
def print_list(self):
  cur = self.head 

  while cur:
      print(cur.data)
      cur = cur.next
      if cur == self.head:
          break
          
```

##### prepend

```py
def prepend(self, data):
  new_node = Node(data)
  cur = self.head 
  new_node.next = self.head

  if not self.head:
      new_node.next = new_node
  else:
      while cur.next != self.head:
          cur = cur.next
      cur.next = new_node
  self.head = new_node
  
```

#### Remove node

It is assumed that there are no duplicates. This is because the code that we will write will only be responsible for removing the first occurrence of the key provided to be deleted.

```py
def remove(self, key):
  if self.head:
    if self.head.data == key:
      cur = self.head 
      while cur.next != self.head:
        cur = cur.next 
      if self.head == self.head.next:
        self.head = None
      else:
        cur.next = self.head.next
        self.head = self.head.next
    else:
      cur = self.head 
      prev = None 
      while cur.next != self.head:
        prev = cur 
        cur = cur.next
        if cur.data == key:
          prev.next = cur.next 
          cur = cur.next
```

#### Split linked list into two halves

<p align="center">
  <img src = "https://user-images.githubusercontent.com/69206952/181853322-32658d96-8013-4dfc-bda0-375b9e73948d.png"/>
</p>

To approach this problem, we'll find the length of the circular linked list and calculate the midpoint. Once that is done, we'll split the linked list around the midpoint.

##### \_\_len\_\_()

```py
def __len__(self):
  cur = self.head
  count = 0
  while cur:
    count += 1
    cur = cur.next
    if cur == self.head:
      break
  return count
  
```

The \_\_len\_\_ method has been defined with underscores before and after the len keyword so that it overrides the len method to operate on a circular linked list.

##### Implementation

```py
def split_list(self):
    size = len(self)    

    if size == 0:
        return None
    if size == 1:
        return self.head

    mid = size//2
    count = 0

    prev = None
    cur = self.head

    while cur and count < mid:
        count += 1
        prev = cur
        cur = cur.next
    prev.next = self.head 

    split_cllist = CircularLinkedList()
    while cur.next != self.head:
        split_cllist.append(cur.data)
        cur = cur.next
    split_cllist.append(cur.data)

    self.print_list()
    print("\n")
    split_cllist.print_list()
    
```    

#### Josephus problem

Josephus problem is related to this concept. In this problem, people are standing in one circle waiting to be executed. Following points list the specifications of Josephus problem:

- The counting out begins at a specified point in a circle and continues around the circle in a fixed direction.

- In each step, a certain number of people are skipped and the next person is executed.

For example, if we have n people, and k-1 people are skipped every time, it means that the kth person is executed. Here, k is the step-size.

To solve this problem, we will tweak the remove method from one of the previous lessons so that we can remove nodes by passing the node itself instead of a key. To avoid confusion, we’ll use the code from remove and paste it in a new method called remove_node with some minor modifications.

```py
def josephus_circle(self, step):
  cur = self.head 

  length = len(self)
  while length > 1:
    count = 1 
    while count != step:
      cur = cur.next 
      count += 1
    print("KILL:" + str(cur.data))
    self.remove_node(cur)
    cur = cur.next
    length -= 1
    
```    

### Doubly linked lists

<p align="center">
  <img src = "https://user-images.githubusercontent.com/69206952/181935593-2d7a47f2-f6dc-471e-9b7a-b8b8459f853f.png"/>
</p>

The doubly linked list is very similar to the singly linked list, except for the difference of the previous pointer. In a doubly linked list, a node is made up of the following components:

- Data
- Next
- Prev

The prev of the head node points to NULL while the next of the tail node also points to NULL.

Let's go ahead and implement the doubly linked list in Python:

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        pass

    def prepend(self, data):
        pass

    def print_list(self):
        pass
```

#### Append and prepend

##### append

```py
def append(self, data):
  if self.head is None:
    new_node = Node(data)
    self.head = new_node
  else:
    new_node = Node(data)
    cur = self.head
    while cur.next:
      cur = cur.next
    cur.next = new_node
    new_node.prev = cur
    
```

##### print_list

```py
def print_list(self):
  cur = self.head
  while cur:
    print(cur.data)
    cur = cur.next
```

##### prepend

```py
def prepend(self, data):
  if self.head is None:
    new_node = Node(data)
    self.head = new_node
  else:
    new_node = Node(data)
    self.head.prev = new_node
    new_node.next = self.head
    self.head = new_node
    
```    

#### Add node before/after

The general approach to solve this problem would be to traverse the doubly linked list and look for the key that we have to insert the new node after or before. Once we get to the node whose value matches the input key, we update the pointers to make room for the new node and insert the new node according to the position specified.

##### Add node after

There are two cases:

1. the node that we have to insert after the new node is the last node in the DLL (doubly linked list), so that the next of that node is NULL.
2. the node that we have to insert after the new node is not the last node in the DLL.

```py
def add_after_node(self, key, data):
  cur = self.head
  while cur:
    if cur.next is None and cur.data == key:
      self.append(data)
      return
    elif cur.data == key:
      new_node = Node(data)
      nxt = cur.next 
      cur.next = new_node
      new_node.next = nxt
      new_node.prev = cur 
      nxt.prev = new_node
      return
    cur = cur.next
    
```

##### Add node before

Two scenarios:

1. We have to insert a new node before the head node.
2. We have to insert a new node before a node that is NOT the head node.

```py
def add_before_node(self, key, data):
  cur = self.head 
  while cur:
    if cur.prev is None and cur.data == key:
      self.prepend(data)
      return
    elif cur.data == key:
      new_node = Node(data)
      prev = cur.prev
      prev.next = new_node
      cur.prev = new_node
      new_node.next = cur
      new_node.prev = prev
      return 
    cur = cur.next
    
```    

#### Delete node

##### Case 1: deleting the only node present

```py
def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None 
                    self.head = None
                    return
            cur = cur.next
            
```            

##### Case 2: deleting head node

```py
def delete(self, key):
  cur = self.head
  while cur:
    if cur.data == key and cur == self.head:
      # Case 1:
      if not cur.next:
        cur = None 
        self.head = None
        return

      # Case 2:
      else:
        nxt = cur.next
        cur.next = None 
        nxt.prev = None
        cur = None
        self.head = nxt
        return 
    cur = cur.next
    
```

##### Case 3: deleting node other than head where cur.next is not None

```py
def delete(self, key):
  cur = self.head
  while cur:
    if cur.data == key and cur == self.head:
      # Case 1:
      if not cur.next:
        cur = None 
        self.head = None
        return

      # Case 2:
      else:
        nxt = cur.next
        cur.next = None 
        nxt.prev = None
        cur = None
        self.head = nxt
        return 

    elif cur.data == key:
      # Case 3:
      if cur.next:
          nxt = cur.next 
          prev = cur.prev
          prev.next = nxt
          nxt.prev = prev
          cur.next = None 
          cur.prev = None
          cur = None
          return
    cur = cur.next 
```

##### Case 4: deleting node other than head where cur.next is None

```py
def delete(self, key):
  cur = self.head
  while cur:
    if cur.data == key and cur == self.head:
      # Case 1:
      if not cur.next:
        cur = None 
        self.head = None
        return

      # Case 2:
      else:
        nxt = cur.next
        cur.next = None 
        nxt.prev = None
        cur = None
        self.head = nxt
        return 

    elif cur.data == key:
      # Case 3:
      if cur.next:
          nxt = cur.next 
          prev = cur.prev
          prev.next = nxt
          nxt.prev = prev
          cur.next = None 
          cur.prev = None
          cur = None
          return

        # Case 4:
      else:
          prev = cur.prev 
          prev.next = None 
          cur.prev = None 
          cur = None 
          return 
    cur = cur.next
```

#### Reverse

```py
def reverse(self):
  tmp = None
  cur = self.head
  while cur:
    tmp = cur.prev
    cur.prev = cur.next
    cur.next = tmp
    cur = cur.prev
  if tmp:
    self.head = tmp.prev
    
```    

## Arrays

### Array advance game

In this game, you are given an array of non-negative integers. For example: 

```
[3,3,1,0,2,0,1]
```

Each number in the array represents the maximum you can advance in the array.

#### Algorithm

##### Greedy approach

Let's try the _greedy_ approach in which we always advance the maximum we can at every index.

For the array `[2,4,1,1,0,2,3]` it doesn't work.

So, let's look at the algorithm which will solve the problem:

- Iterate through each entry in an array A.
- Track the furthest we can reach from entry (A[i] + i).
- If for some i, we don't reach the end and that is the furthest we can reach, then we can't reach the last index. Otherwise, the end is reached.
- i: index processed. Furthest possible to advance from i: A[i] + i

```py
def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))
```

### Arbitrary precision increment

In this lesson, we will be considering the following:

Given: An array of non-negative digits that represent a decimal integer.

Problem: Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.

#### Algorithm

For an array A,

1. Add 1 to the rightmost digit.
2. Propagate carry throughout the array.

In Python, you can solve the problem with just one line. But this approach will not be asked in an interview. 

```py
A = [1, 4, 9]
s = ''.join(map(str, A))
 print(int(s) + 1)
```

Let's implement the algorithm:

```py
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A
    
```    

### Two sum problem

Given an array of integers, return True or False if the array has two numbers that add up to a specific target. You may assume that each input would have exactly one solution. We investigate three different approaches to solving this problem.

#### Solution 1

A brute-force approach that takes O($n^2$) time to solve with O(1) space where we loop through the array and create all possible pairings of elements.

```py
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_brute_force(A, target):
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[i] + A[j] == target:
        print(A[i], A[j])
        return True
  return False

```

#### Solution 2

A slightly better approach time-wise, taking O(n) time, but worse from a space standpoint, with space complexity of O(n).

```py
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hash_table(A, target):
  ht = dict()
  for i in range(len(A)):
    if A[i] in ht:
      print(ht[A[i]], A[i])
      return True
    else:
      ht[target - A[i]] = A[i]
  return False

```

#### Solution 3

This approach has a time complexity of O(n) and a constant space complexity O(1).

```py
# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum(A, target):
  i = 0
  j = len(A) - 1
  while i < j:
    if A[i] + A[j] == target:
      print(A[i], A[j])
      return True
    elif A[i] + A[j] < target:
      i += 1
    else:
      j -= 1
  return False
```

### Optimal task assignment

In this lesson, we will be solving the following problem:

Assign tasks to workers so that the time it takes to complete all the tasks is minimized given a count of workers and an array where each element indicates the duration of a task.

We wish to determine the optimal way in which to assign tasks to some workers. Each worker must work on exactly two tasks. Tasks are independent of each other, and each task takes a certain amount of time.

In the greedy approach, we’ll focus on the following rule:

- Pair the longest task with the shortest one.

The time complexity for the algorithm will be O(nlogn) due to sorting.

```py
A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i])
```

The ~i is the bitwise complement operator which puts a negative sign in front of i and subtracts 1 from it.

#### Intersection of two sorted arrays

Given two sorted arrays, A and B, determine their intersection. What elements are common to A and B?

There is a one-line solution to this problem in Python that will also work in the event when the arrays are not sorted.

```py
print(set(A).intersection(B))
```

However, since we are aware that the arrays A and B are sorted, we can use this to our advantage and solve the problem in a way that leverages this and gives us a slightly better runtime.

```py
def intersect_sorted_array(A, B):
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection
    
```    

### Binary Trees

It is a tree dta structure in which each node has at most two children, which are referred to as left child and right child.

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/182461295-3044f83b-a27c-4d34-9694-47a3d756a2f2.png"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/182461461-6ec6a4fc-81a0-4480-abb0-2280233cf3d9.png"/>
</p>

#### Depth of a node

The length of the path from a node, n, to the root node. The depth node of the root node is 0.

#### Height of a tree

The length of the path from n to its deepest descendant. The height of the tree itself is the height of the root node, and the height of leaf nodes is always 0.

#### Types of binary trees

##### Complete binary tree

In a complete binary tree, every level except possibly the last, is completely filled and all nodes in the last level are as far left as possible.

##### Full binary tree

A full binary tree (sometimes referred to as a proper or plane binary tree) is a tree in which every node has either 0 or 2 children.

##### Implementation

To implement a binary tree in Python, we will first implement the Node class.

```py
class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
```

In the code above, we have defined the Node class with a new style of defining classes in Python. The Node class has three attributes:

1. self.value
2. self.left
3. self.right

Implementing the BinaryTree class:

```py
class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
```

#### Traversal algorithms

##### Tree traversal

It is the process of visiting each node in a tree data structure, exactly once. Unlike linked lists or one-dimensional arrays that are canonically traversed in linear order, trees may be traversed in multiple ways. They may be traversed in depth-first or breadth-first order.

There are three common ways to traverse a tree in depth-first order:

1. In-order
2. Pre-order
3. Post-order

###### Pre-order traversal

Algorithm:

1. Check if the current node is empty/null.
2. Display the data part of the root (or current node).
3. Traverse the left subtree by recursively calling the pre-order method.
4. Traverse the right subtree by recursively calling the pre-order method.

```py
def preorder_print(self, start, traversal):
  """Root->Left->Right"""
  if start:
    traversal += (str(start.value) + "-")
    traversal = self.preorder_print(start.left, traversal)
    traversal = self.preorder_print(start.right, traversal)
  return traversal
```

###### In-order traversal

1. Check if the current node is empty/null.
2. Traverse the left subtree by recursively calling the in-order method.
3. Display the data part of the root (or current node).
4. Traverse the right subtree by recursively calling the in-order method.

```py
def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
        
```

###### Post-order traversal

1. Check if the current node is empty/null.
2. Traverse the left subtree by recursively calling the in-order method.
3. Traverse the right subtree by recursively calling the in-order method.
4. Display the data part of the root (or current node).

```py
def postorder_print(self, start, traversal):
  """Left->Right->Root"""
  if start:
    traversal = self.postorder_print(start.left, traversal)
    traversal = self.postorder_print(start.right, traversal)
    traversal += (str(start.value) + "-")
  return traversal
  
```

###### Helper method

Below is the implementation of all the tree traversal methods within the BinaryTree class. Additionally, there is a helper method `print_tree(self, traversal_type)` which will invoke the specified method according to traversal_type.

```py
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-5-2-6-7-3-1
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

# Set up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
#print(tree.print_tree("postorder"))
```

##### Level-order traversal

<p align="center">
  <img src="https://user-images.githubusercontent.com/69206952/182469779-c4fe1df1-d203-44dd-a91f-b7bf2b756edb.png"/>
</p>

To do a level-order traversal of a binary tree, we require a queue.

```py
class Queue(object):
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    if not self.is_empty():
      return self.items.pop()

  def is_empty(self):
    return len(self.items) == 0

  def peek(self):
    if not self.is_empty():
      return self.items[-1].value

  def __len__(self):
    return self.size()

  def size(self):
    return len(self.items)
    
```    

Now that we have successfully implemented the Queue class, let's go ahead and implement level-order traversal:

```py
def levelorder_print(self, start):
  if start is None:
    return 

  queue = Queue()
  queue.enqueue(start)

  traversal = ""
  while len(queue) > 0:
    traversal += str(queue.peek()) + "-"
    node = queue.dequeue()

    if node.left:
      queue.enqueue(node.left)
    if node.right:
      queue.enqueue(node.right)

  return traversal
```

##### Reverse level-order traversal

We will need the Stack class:

```py
class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s
```

Now that we are done with the implementation of Stack class, let's discuss `reverse_levelorder_print`:

```py
def reverse_levelorder_print(self, start):
  if start is None:
    return 

  queue = Queue()
  stack = Stack()
  queue.enqueue(start)


  traversal = ""
  while len(queue) > 0:
    node = queue.dequeue()

    stack.push(node)

    if node.right:
      queue.enqueue(node.right)
    if node.left:
      queue.enqueue(node.left)
  
  while len(stack) > 0:
    node = stack.pop()
    traversal += str(node.value) + "-"

  return traversal
```

##### Height of tree

The height of a tree is the height of its root node.

###### Height of a node

The height of a node is the number of edges on the longest path between that node and a leaf.
