### 1 ###

def add_all(*args):
    # print(type(args)) # tuple
    sum = 0
    for num in args:
        sum += num
    return sum


values = [1,2,3,4]
other_values = [5,6,7,8]
# print(add_all(*values, *other_values))


### 2 ###

def introduce(**kwargs):
    # print(type(kwargs)) # dict
    for item in kwargs.items():
        print(item)
# introduce(greeting="hello",name="Bob")

person = {
    "name": "Bob",
    "city": "Seoul",
    "age": "28"
}
# introduce(**person)


### 3 ###

def func_with_all_arguments(x: int, y: int, *args, value: int = 8, **kwargs):
    print(x,y)
    print(args)
    print(value)
    print(kwargs)

# func_with_all_arguments(1,2,3,4,5,**person)


### 4 ###

def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True

    return (old_dict, is_modified)


product = {'id': 1, 'name': 'Phone', 'price': 99.99}

# structure = modify_dict(old_dict=product, in_stock=True)

product, was_modified = modify_dict(old_dict=product, in_stock=True)

print(product)
print(was_modified)