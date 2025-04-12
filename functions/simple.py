def nothing():
    pass


numbers_1 = [1,2,3,4,5,6,7,8,9,10]
numbers_2 = [5,6,7,8,9,10]


def calc_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


def count_vowels(text):
    VOWELS = "aeiouAEIOU"
    count = 0

    for letter in text:
        if letter in VOWELS:
            count += 1
    return count
