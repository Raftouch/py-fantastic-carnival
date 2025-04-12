def format_date(*, day: int, month: str) -> str:
    return f"The date is {day} of {month}"


print(format_date(day=12, month='April'))
print(format_date(month='May', day=6))


def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"


print(custom_greeting(name='John'))
print(custom_greeting(name='GF', greeting='Ciao'))