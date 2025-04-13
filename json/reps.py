import json

book = {
    'title': '1984',
    'author': 'George Orwell',
    'isbn': '978-0451524935',
    'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
    'count': 30,
    'genres': ["Romance", "History", "Psychology", "Adventure"]
}


json_stringified = json.dumps(book)
print(json_stringified)
# {"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", "count": 30, "genres": ["Romance", "History", "Psychology", "Adventure"]}

json_parsed = json.loads(json_stringified)
print(json_parsed)
print(type(json_parsed)) # dict