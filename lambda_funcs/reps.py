# def sort_by_len(el: str) -> int:
#     return len(el)


# sort_by_len_lambda = lambda el: len(el)

# print(sort_by_len("apple"))
# print(sort_by_len_lambda("apple"))


fruits = ['banana', 'apple', 'cherry', 'date']

sorted_fruits = sorted(fruits, key=lambda el: len(el))
# print(sorted_fruits)

longest_word = max(fruits, key=lambda el: len(el))
print(longest_word)