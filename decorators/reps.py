def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

# --> if return None
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before")
#         func(*args, **kwargs)
#         print("After")
#     return wrapper

@my_decorator
# def say_hello(*, name: str) -> None:
#     print(f"Hello, {name}")
def add_numbers(*, a: int, b: int) -> int:
    print("Adding numbers ...")
    return a + b


# my_decorator(say_hello)()

# say_hello(name="Bob")
result = add_numbers(a=2, b=3)
print(result)