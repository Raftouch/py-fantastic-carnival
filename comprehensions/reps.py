# squares = []
# for x in range(0,10):
#     squares.append(x ** 2)

squares = [x ** 2 for x in range(10)]


# even_squares = []
# for x in range(10):
#     if not x % 2:
#         even_squares.append(x ** 2)

even_squares = [x ** 2 for x in range(10) if not x % 2]


# numbers_w_labels = []
numbers = [1,2,3,4,5]

# for num in numbers:
#     if not num % 2:
#         num = 'even'
#         numbers_w_labels.append(num)
#     else:
#         num = 'odd'
#         numbers_w_labels.append(num)


numbers_w_labels = ['even' if not num % 2 else 'odd' for num in numbers]

square_dict = {x: x ** 2 for x in range(10)}


matrix = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]

# transpose_matrix = [
#     [1,4,7],
#     [2,5,8],
#     [3,6,9]
# ]

# transpose_matrix = []

# for i in range(len(matrix)):
#     transpose_row = []
#     for row in matrix:
#       transpose_row.append(row[i])
#     transpose_matrix.append(transpose_row)


transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose_matrix)

