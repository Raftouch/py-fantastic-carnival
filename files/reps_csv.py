import csv

# rows = [['name', 'age', 'profession'], ['Bob', '28', 'Engineer'], ['Ann', '35', 'Dancer'], ['Max', '42', 'Teacher']]

# file = open("files/files/persons.csv", "w")

# csv_writer = csv.writer(file)
# csv_writer.writerows(rows)

# file.close()


# file = open("files/files/persons.csv", "r")

# csv_dict_reader = csv.DictReader(file)

# for row in csv_dict_reader:
#     print(row["name"], row["age"], row["profession"])

# file.close()


new_persons = [
    {"name": "John","age": "19","profession": "Student"},
    {"name": "Mary","age": "55","profession": "Actor"}
]

file = open("files/files/persons.csv", "a")

fileds = ["name", "age", "profession"]

csv_dict_writer = csv.DictWriter(file, fieldnames=fileds)
csv_dict_writer.writerows(new_persons)

file.close()

