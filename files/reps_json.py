import json

## WRITE FILE

# data = {"name": "Bob","age": "28","city": "Seoul"}

# file = open("files/files/data.json", "w")

# json.dump(data, file, indent=4)

# file.close()


## READ FILE

file = open("files/files/data.json", "r")

loaded_data = json.load(file)

file.close()

print(loaded_data)
