def fibonacci(a):
    z = 1
    if a > 2:
        z = fibonacci(a-1) + fibonacci(a-2)
    return z


a = int(input('введите номер числа из последовательности Фибонначи'))


c = [1]
i = 1
x = 1

while i < a:
    c.insert(i, x)
    x = c[i] + c[i-1]
    i = i+1
    print(c)

print(fibonacci(a))
print(c[a-1])