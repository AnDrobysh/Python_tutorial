a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

if len(a) > len(b):
    for number in a:
        if b.count(number) != 0:
            b.remove(number)
            c.append(number)
else:
    for number in b:
        if a.count(number) != 0:
            a.remove(number)
            c.append(number)

print(c)

