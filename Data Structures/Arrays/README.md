# Arrays in Python

Array(List in Python): a collection of elements/values each identified by an array index or key
- index starts at zero
- because of the indexes: random access is possible
- can have as many dimensions as we want
- Dynamic array: when the size of the array is changing dynamically
- Applications: lookup tables/hashtables, heaps
```python
numbers = [1,2,3,4,5,6,7,8,9]
```

Multimdimensional Arrays: it can prove to be very important in mathematical computations (matrixes)
```python
numbers[][] #two dimensional array
#First parameter: row index
#Second parameter: column index
numbers = [[[1],[2],[3]],[[4],[5],[6]],[[7],[8],[9]]]
```
## Advantages
- We can use random access because of keys: getitem(int index) will return the value with the given key very fast
    - O(1) time complexity
- Very easy to implement and to use
- Very fast data structure
- we should use arrays in applications when we want to add items over and over again and we want to take items with given indexes ~ it will be fast

## Disadvantages
- We have to know the size of the array at compile-time: so it is not so dynamic of a data structure
- If it is full: we have to create a bigger array and have to copy the values one by one 
    - Reconstructing an array is O(N) operation
- It is not able to store items with different types, unless in python

## List Operations
### Append
- list.append('x')
- We can keep adding values to the array as long as it is not full
- Lists in python are dynamic, so no need to create a new list every time you reach the limit
- Can add to the end of a list using list.append(variable)
- Time Complexity: O(1)

```python
numbers = [6]
numbers.append[5]
print(numbers)
```
#### Output
```pythom
[6, 5]
```

### Count
- list.count('x')
- We can count the number of occurences of "x" in a list using the list.count(x) function
- Returns the amount of times "x" occurs in the list
- Time Complexity: O(n)
```python
names = ["jared", "alan", "joe", "jared"]
count = names.count("jared")
print(count)
```
#### Output
```
2
```

### Index
- list.index('x')
- Returns the index of 'x' in the list
- Time Complexity: O(n) 
    - Have to go through list until finding 'x'
```python
names = ["jared", "alan", "joe", "jared"]
index = names.index("alan")
print(index)
```
#### Output
```
1
```

### Insert
- list.insert('y','x')
- Inserts 'x' at location 'y'
- Time Complexity: O(n)
```python
names = ["jared", "alan", "joe", "jared"]
names.insert(2,"grant")
print(names[2])
```
#### Output
```
grant
```

### Pop
- list.pop(index)
- Removes and returns the item at the end of the list or at the optional index argument
- Time Complexity: O(n)
    - Has to iterate to end of list and then remove and return element
```python
names = ["jared", "alan", "joe", "jared"]
print(names.pop())
print(names)
```
#### Output
```
jared
['jared', 'alan', 'joe']
```

### Remove
- list.remove('x')
- Finds and removes the first occurence of x
- Time Complexity: O(n)
    - Needs to iterate and check each item in list
```python
names = ["jared", "alan", "joe", "jared"]
names.remove("jared")
print(names)
```
#### Output
```
['alan', 'joe', 'jared']
```

### Reverse
- list.reverse()
- Reverses the order of elements in a list
- Time Complexity: O(n)
```python
names = ["jared", "alan", "joe", "jared"]
names.reverse()
print(names)
```

### Sort
- list.sort()
- Sorts the list in ascending order of alphabet or numerically
- Time Complexity: O(n*logn)
```
names = ["jared", "alan", "joe", "jared"]
names.sort()
print(names)
```