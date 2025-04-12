greeting = 'Hello, World'
count_o = 0
for char in greeting:
    if char == 'o':
        count_o += 1
print(count_o)

# # # #

students = ["Bob", 'Mob', 'Raf', 'Lil', 'Lib']
count_b = 0
for student in students:
    for char in student:
        if char.lower() == "b":
            count_b += 1
print(count_b)

# # # #

numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    if num == 8:
        break
    elif not num % 2:
        continue
    print(num) 

# # # #

range_list = list(range(0,10))
# print(range_list)
range_list_2 = list(range(1,10,2))

# # # #

for i in range(len(numbers)):
    numbers[i] += 1

# # # #

greeting = "Hello, world"

indexes = []
count = 0

for i in range(len(greeting)):
    if greeting[i] == "o":
        indexes.append(i)
        count += 1

# # # #

mult_table = list(range(1,10))
# mult_table = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(mult_table)):
    for y in range(len(mult_table)):
        print(mult_table[i] * mult_table[y], end=' ')
    print()
