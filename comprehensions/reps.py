# squares = []
# for x in range(0,10):
#     squares.append(x ** 2)

squares = [x ** 2 for x in range(10)]


# even_squares = []
# for x in range(10):
#     if not x % 2:
#         even_squares.append(x ** 2)

even_squares = [x ** 2 for x in range(10) if not x % 2]

print(even_squares)