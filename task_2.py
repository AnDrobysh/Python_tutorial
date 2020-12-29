string = input("введите строку")

string.lower()

a, c = [], []

for number in string:
    c.append(number)

a = c.copy()

a.reverse()

if c == a:
    print("Это палиндорм")
else:
    print("Это не палиндорм")
