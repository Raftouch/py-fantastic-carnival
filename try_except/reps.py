def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)

try:
    print(find_average(numbers=[]))
except ZeroDivisionError:
    print("the list is empty")

print("End of code")