a = [1, 2, 3, [2, 34, [12, {'DO': 1, 'THE': 2}, 19]], (1, 2, 3), "Kek"]
c = []

def pars(a):
    b = []
    for number in a:
        if type(number) == int:
            a.append(number)
            a.remove(number)
        elif type(number) == str:
            a.append(number)
            a.remove(number)
        elif type(number) == float:
            a.append(number)
            a.remove(number)
        if type(number) == tuple:
            number_list = number
            a.remove(number)
            for numbers_of_number_list in number_list:
                a.append(numbers_of_number_list)
                pars(a)
        elif type(number) == dict:
            number_list = number
            a.remove(number)
            for numbers_of_number_list in number_list:
                a.append(numbers_of_number_list)
                a.append(number_list[numbers_of_number_list])
                pars(a)
        elif type(number) == list:
            number_list = number
            a.remove(number)
            for numbers_of_number_list in number_list:
                a.append(numbers_of_number_list)
                pars(a)
    return a

pars(a)
print(a)

