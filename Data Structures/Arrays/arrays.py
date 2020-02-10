#One Dimensional Array
numbers = [10,20,30,40,50]

#Two Dimensional Array
numbers2 = [[[1],[2],[3]],[[4],[5],[6]],[[7],[8],[9]]]

#random indexing --> O(1); can get items if we know the index instantly
print(numbers[0])

#Works same for two dimensional
print(numbers2[0])
print(numbers2[0][2])

#Adding to the list
numbers.append(60)
print(numbers)

#Counting occurences of x in the list
names = ["jared", "alan", "joe", "jared"]
count = names.count("jared")
print(count)

#Checking index of 'x'
index = names.index("alan")
print(index)

#Inserting a new item
names = ["jared", "alan", "joe", "jared"]
names.insert(2,"grant")
print(names[2])

#Popping last element
names = ["jared", "alan", "joe", "jared"]
print(names.pop())
print(names)

#Removing an element 'x' within a list
names = ["jared", "alan", "joe", "jared"]
names.remove("jared")
print(names)

#Reversing the order of a list
names = ["jared", "alan", "joe", "jared"]
names.reverse()
print(names)

#Sorting names in alphabetical order
names = ["jared", "alan", "joe", "jared"]
names.sort()
print(names)