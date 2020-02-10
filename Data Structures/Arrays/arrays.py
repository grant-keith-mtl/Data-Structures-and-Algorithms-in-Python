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
