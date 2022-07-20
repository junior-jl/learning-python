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
