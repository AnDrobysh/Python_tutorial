a = [1, 2, 3, [2, 34, [12, {'DO': 1, 'THE': 2}, 19]], (1, 2, 3), "Kek"]

b = []

# for number in a:
#     print(number, type(number))
for number in a:
    # if type(number) == int:
    #     b.append(number)
    # elif type(number) == str:
    #     b.append(number)
    # elif type(number) == float:
    #     b.append(number)
    if type(number) == tuple:
        number_list = number
        a.remove(number)
        for numbers_of_number_list in number_list:
            a.append(numbers_of_number_list)
    elif type(number) == dict:
        number_list = number
        a.remove(number)
        for numbers_of_number_list in number_list:
            a.append(numbers_of_number_list)
            a.append(number_list[numbers_of_number_list])
    elif type(number) == list:
        number_list = number
        a.remove(number)
        for numbers_of_number_list in number_list:
            a.append(numbers_of_number_list)

print(a)
for number in a:
    print(type(number))






