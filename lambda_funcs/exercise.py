people = [
   {"name": "Mel", "age": 18},
   {"name": "Bob", "age": 32},
   {"name": "Ann", "age": 25},
   {"name": "Kate", "age": 25},
   {"name": "Bill", "age": 18},
   {"name": "Lao", "age": 38},
]

min_element = min(people, key=lambda el: (el["age"], el["name"]))
print(min_element)