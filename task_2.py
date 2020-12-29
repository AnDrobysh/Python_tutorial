input_string = input("введите строку")

input_string.lower()


# a, c = [], []
#
# for number in string:
#     c.append(number)
#
# a = c.copy()
#
# a.reverse()
#
# if c == a:
#     print("Это палиндорм")
# else:
#     print("Это не палиндорм")

def is_palindrome(string):
    if string == ''.join(reversed(string)):
        return 'palindrom'
    else:
        return 'not_palindrom'


print(is_palindrome(input_string))
