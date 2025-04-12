# counter = 1
# while counter <= 5:
#     print(f"Counter is: {counter}")
#     counter += 1


# my_list = [0, 1, 2]
# while my_list:
#     element = my_list.pop()
#     print(f"element: {element}")
# print(my_list) # []


while True:
    answer = input("Enter a number: ")
    if answer == "quit":
        break
    print(f"You entered: {answer}")