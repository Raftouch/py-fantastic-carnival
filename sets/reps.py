# my_set = {1,2,3,4,5}

# my_set = set()

# for i in range(5):
#     my_set.add(i)

# print(my_set)

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

# print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7}
# print(set1.intersection(set2)) # {3, 4, 5}  

squares = {x ** 2 for x in range(10)}
# print(squares)

numbers = [1,2,3,3,4,4,5,6,7,7,8,9]
unique_numbers = list(set(numbers))
print(unique_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

