k = 0
a = 0


def funcsion(x):
    sum = 0
    k = 0
    while True:
        f = (((-1) ** k) * x ** (2 * k + 3)) / ((2 * k + 1) * (2 * k + 3))
        sum += f
        if abs(f) < 0.001:
            break
        k += 1
        return sum


x = a
while x <= 1:
    print(round(x, 3), "\t", funcsion(x))
    x += 0.1
