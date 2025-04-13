student = {
    "name": "Bob",
    "city": "Seoul"
}

for item in student.items():
    key, value = item
    
# for key in person.keys():
#     print(key)
# for value in person.values():
#     print(value)

person = {
    "name": "Bob",
    "city": "Seoul",
    "age": "28"
}

additional_person_info = {
    "job": "Product Owner",
    "married": True,
    "city": "Paris"
}

# person.update(additional_person_info)
person = person | additional_person_info
print(person)