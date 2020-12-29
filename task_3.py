def fibonacci(sequential_number):
    z = 1
    if sequential_number > 2:
        z = fibonacci(sequential_number - 1) + fibonacci(sequential_number - 2)
    return z


a = int(input('введите номер числа из последовательности Фибонначи'))


x, i, c = 1, 1, [1]

while i < a:
    c.insert(i, x)
    x = c[i] + c[i-1]
    i = i+1
    print(c)

print(fibonacci(a))
print(c[a-1])
