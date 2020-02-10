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
- We can keep adding values to the array as long as it is not full
- Lists in python are dynamic, so no need to create a new list every time you reach the limit
- Can add to the end of a list using list.append(variable)

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
- We can count the number of occurences of "x" in a list using the list.count(x) function
- Returns the amount of times "x" occurs in the list

```python
names = ["jared", "alan", "joe", "jared"]
count = names.count("jared")
print(count)
```
#### Output
```
2
```