# x = 42
# y = x

# print(id(x), id(y), x, y)
# y += 1
# print(id(x), id(y), x, y)

my_list = [1,2,3]
another_list = my_list

# print(id(my_list), id(another_list), my_list, another_list)
# another_list.append(4)
# print(id(my_list), id(another_list), my_list, another_list)

x = None
y = None

# print(x is y) # True

list1 = [1,2,3]
list2 = list1

# print(list1 is list2) # True

list3 = [1,2,3]
list4 = [1,2,3]

print(list3 is list4) # False
print(list3 == list4) # True