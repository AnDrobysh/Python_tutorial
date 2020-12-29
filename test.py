# # a = [1, 2, 333, 333, 4]
# # a.remove(2)
# # print(a)
# #
# #
# # c = [(1, 2, 3), 4]
# # b = []
# # i = 0
# # ii = 0
# # for number in a:
# #     while type(number) != str and type(number) != int and type(number) != float:
# #         elements = number
# #         if type(number) == list:
# #             a.remove(number)
# #             if i < len(elements):
# #                 a.append(elements[1])
# #                 print(a)
# #         elif type(number) == tuple:
# #             if i < len(elements):
# #                 a.append(elements[i])
# #                 ii = ii + 1
# #             else:
# #                 a.remove(number)
# #                 print(a)
# #         elif type(number) == dict:
# #             for dic in elements:
# #                 var_in_list = elements.popitem()
# #                 a.append(var_in_list[1])
# #                 a.append(var_in_list[2])
# #
# #         else:
# #             a.append(number)
# # print(a)
#
# print(type({'DO': 1, 'THE': 2}))

a = [1, 2, 3, 4, 5, 6]
b = []

for number in a:
    b.append(number)
    el = number
    a.remove(el)

