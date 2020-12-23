string = input("введите строку")

string.lower()

c = []
a = []

for number in string:
    c.append(number)

a = c
a.reverse()


if c == a:
    print("Это палиндорм")
else:
    print("Не палиндорм")