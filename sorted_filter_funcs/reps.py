fruits = ['banana', 'apple', 'cherry', 'date']

def sort_by_len(el: str) -> int:
    return len(el)

# for fruit in fruits:
#     print(sort_by_len(fruit))

sorted_fruits = sorted(fruits, key=sort_by_len)


people = [
   {"name": "Mel", "age": 47},
   {"name": "Bob", "age": 21},
   {"name": "Ann", "age": 35}
]

def sort_by_age(person: dict) -> int:
    return person["age"]

sorted_people = sorted(people, key=sort_by_age)


more_people = [
   {"name": "Mel", "age": 18},
   {"name": "Bob", "age": 32},
   {"name": "Ann", "age": 25},
   {"name": "Kate", "age": 25},
   {"name": "Bill", "age": 18},
   {"name": "Lao", "age": 38},
]

def sort_by_age_name(person: dict) -> tuple[int, str]:
    return person["age"], person["name"]

sorted_people_by_name_age = sorted(more_people, key=sort_by_age_name)
# print(sorted_people_by_name_age)


def is_even(num: int) -> bool:
    return not num % 2

numbers = [1,2,3,3,4,4,5,6,7,7,8,9]

filtered_numbers = list(filter(is_even, numbers))
# print(filtered_numbers)


def is_older_than_21(person: dict) -> bool:
    return person["age"] > 21

filtered_people = list(filter(is_older_than_21, people))
print(filtered_people)