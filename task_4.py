a = [1, 2, 3, [2, 34, [12, {'DO': 1, 'THE': 2}, 19]], (1, 2, 3), "Kek"]


def make_lin(m_list):
    n_list = []
    for x in m_list:
        if isinstance(x, (list, tuple, dict)):
            if isinstance(x, (list, tuple)):
                n_list += make_lin(x)
            else:
                n_list += make_lin(x.items())
        else:
            n_list.append(x)
    return n_list


print(make_lin(a))


# a = [1, 2, 3, [2, 34, [12, {'DO': 1, 'THE': 2}, 19]], (1, 2, 3), "Kek"]
# # c = []
# #
# #
# # def pars(pars_list):
# #     for number in pars_list:
# #         if type(number) == int:
# #             pars_list.append(number)
# #             pars_list.remove(number)
# #         elif type(number) == str:
# #             pars_list.append(number)
# #             pars_list.remove(number)
# #         elif type(number) == float:
# #             pars_list.append(number)
# #             pars_list.remove(number)
# #         if type(number) == tuple:
# #             number_list = number
# #             pars_list.remove(number)
# #             for numbers_of_number_list in number_list:
# #                 pars_list.append(numbers_of_number_list)
# #                 pars(pars_list)
# #         elif type(number) == dict:
# #             number_list = number
# #             pars_list.remove(number)
# #             for numbers_of_number_list in number_list:
# #                 pars_list.append(numbers_of_number_list)
# #                 pars_list.append(number_list[numbers_of_number_list])
# #                 pars(pars_list)
# #         elif type(number) == pars_list:
# #             number_list = number
# #             pars_list.remove(number)
# #             for numbers_of_number_list in number_list:
# #                 pars_list.append(numbers_of_number_list)
# #                 pars(pars_list)
# #     return pars_list
# #
# #
# # pars(a)
# # print(a)
