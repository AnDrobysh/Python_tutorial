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
        return 'palindrome'
    else:
        return 'not_palindrome'


print(is_palindrome(input_string))
