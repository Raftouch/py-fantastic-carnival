from copy import deepcopy

my_dict = {'x': 1, 'y': 2}
another_dict = my_dict

another_dict['x'] = 100

# print(my_dict)


my_dict_2 = {'x': 1, 'y': 2}
another_dict_2 = my_dict_2.copy()

another_dict_2['x'] = 100

# print(my_dict_2)
# print(another_dict_2)


patient_data = {"heart_rate": [60,61,63,61]}

# patient_data_copy = patient_data.copy()
patient_data_copy = deepcopy(patient_data)

patient_data_copy["heart_rate"].append(64)

# print(patient_data)
# print(patient_data_copy)

def func(*, list: list[int]) -> None:
    # ...
    list.clear()


my_list = [1,2]

# func(list=my_list)
# print(my_list) # []
func(list=deepcopy(my_list))
# print(my_list) # [1,2]


lst = [2,3,4]

another_list = [i ** 2 for i in lst]
lst.extend(another_list)
# print(lst)


numbers = [1,2,3,4,5,6,7,8]

# for num in numbers:
#     if not num % 2:
#         numbers.remove(num)

odd_numbers = []
for num in numbers:
    if num % 2:
        odd_numbers.append(num)

# print(odd_numbers)


# def append_to_list(*, el: int, list: list = []) -> list:
#     list.append(el)
#     return list

# my_lst = append_to_list(el=1)
# print(my_lst) # [1]
# another_lst = append_to_list(el=2)
# print(another_lst) # [1, 2]


def append_to_list(*, el: int, list: list = None) -> list:
    if list is None:
        list = []

    list.append(el)
    return list

my_lst = append_to_list(el=1)
print(my_lst) # [1]
another_lst = append_to_list(el=2)
print(another_lst) # [2]


old_list = [3,1,2]

# new_list = old_list.sort()
# print(new_list) # None

new_list = sorted(old_list)
print(old_list)
print(new_list)
