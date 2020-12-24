a = int(input('введите номер числа из последовательности Фибонначи'))


c = [1]
i = 1
x = 1

while i < a+1:
    c.insert(i, x)
    x = c[i] + c[i-1]
    i = i+1
    print(c)

print(c[a])