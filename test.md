#### Q1. What buit-in Python data type is commonly used to represent a queue?

- [ ] A. `dictionary`
- [ ] B. `set`
- [ ] C. `None`. You can only build a stack from scratch.
- [x] D. `list`

#### Q2. How does `defaultdict` work?

- [ ] A. `defaultdict` will automatically create a dictionary for you that has keys which are the integers 0-10.
- [ ] B. `defaultdict` forces a dictionary to only accept keys that are of the types specified when you created the `defaultdict` (such as string or integers).
- [x] C. If you try to access a key in a dictionary that doesn't exist, `defaultdict` will create a new key for you instead of throwing a `KeyError`.
- [ ] D. `defaultdict` stores a copy of a dictionary in memory that you can default to if the original gets unintentionally modified.

#### Q3. What is an abstract class?

- [ ] A. An abstract class is the name for any class from which you can instantiate an object.
- [ ] B. Abstract classes must be redefined any time an object is instantiated from them.
- [ ] C. Abstract classes must inherit from concrete classes.
- [x] D. An abstract class exists only so that other "concrete" classes can inherit from the abstract class.

#### Q4. What is key difference between a set and a list?

- [ ] A. A set is an ordered collection unique items. A list is an unordered collection of non-unique items.
- [ ] B. Elements can be retrieved from a list but they cannot be retrieved from a set.
- [ ] C. A set is an ordered collection of non-unique items. A list is an unordered collection of unique items.
- [x] D. A set is an unordered collection unique items. A list is an ordered collection of non-unique items.


#### Q5. Given the following three list, how would you create a new list that matches the desired output printed below?

```python
fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]

# Desired output
[('Apples', 5, 1.50),
('Oranges', 3, 2.25),
('Bananas', 4, 0.89)]
```

- [ ] A.

```python
output = []

fruit_tuple_0 = (first[0], quantities[0], price[0])
output.append(fruit_tuple)

fruit_tuple_1 = (first[1], quantities[1], price[1])
output.append(fruit_tuple)

fruit_tuple_2 = (first[2], quantities[2], price[2])
output.append(fruit_tuple)

return output
```

- [x] B.

```python
i = 0
output = []
for fruit in fruits:
    temp_qty = quantities[i]
    temp_price = prices[i]
    output.append((fruit, temp_qty, temp_price))
    i += 1
return output
```

- [ ] C.

```python
groceries = zip(fruits, quantities, prices)
return groceries

>>> [
('Apples', 5, 1.50),
('Oranges', 3, 2.25),
('Bananas', 4, 0.89)
]
```

- [ ] D.

```python
i = 0
output = []
for fruit in fruits:
    for qty in quantities:
        for price in prices:
            output.append((fruit, qty, price))
    i += 1
return output
```



#### Q6. Correct representation of doctest for function in Python

- [ ] A.

```python
def sum(a, b):
    # a = 1
    # b = 2
    # sum(a, b) = 3

    return a + b
```

- [ ] B.

```python
def sum(a, b):
    """
    a = 1
    b = 2
    sum(a, b) = 3
    """

    return a + b
```

- [x] C.

```python
def sum(a, b):
    """
    >>> a = 1
    >>> b = 2
    >>> sum(a, b)
    3
    """

    return a + b
```

- [ ] D.

```python
def sum(a, b):
    '''
    a = 1
    b = 2
    sum(a, b) = 3
    '''
    return a + b
```

#### Q7. Review the code below. What is the correct syntax for changing the price to 1.5?

```
fruit_info = {
'fruit': 'apple',
'count': 2,
'price': 3.5
}
```

- [x] A. `fruit_info ['price'] = 1.5`
- [ ] B. `my_list [3.5] = 1.5`
- [ ] C. `1.5 = fruit_info ['price]`
- [ ] D. `my_list['price'] == 1.5`

#### Q8. What is the correct syntax for defining an `__init__()` method that takes no parameters?

- [ ] A. 

```python
class __init__(self):
    pass
```

- [ ] B. 

```python
def __init__():
    pass
```

- [ ] C. 

```python
class __init__():
    pass
```

- [x] D. 

```python
def __init__(self):
    pass
```

#### Q9. Why would you use a decorator?

- [ ] A. A decorator is similar to a class and should be used if you are doing functional programming instead of object oriented programming.
- [ ] B. A decoratore is a visual indicator to someone reading your code that a portion of your code is critical and should not be changed.
- [x] C. You use the decorator to alter the functionality of a function without the without having to modify the functions code.
- [ ] D. An import statement is preceded by a decorator, pyhton knows to import the most recent version of whatever package or library is being imported.


#### Q10. What is the runtime complexity of searching for an item in a binary search tree?

- [ ] A. The runtime for searching in a binary search tree is O(1) because each node acts as a key, similar to a dictionary.
- [ ] B. The runtime for searching in a binary search tree is O(n!) because every node must be compared to every other node.
- [x] C. The runtime for searching in a binary search tree is generally O(h), where h is the height of the tree.
- [ ] D. The runtime for searching in a binary search tree is O(n) because every node in the tree must be visited.

