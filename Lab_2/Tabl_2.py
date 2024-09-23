x = 0.0
while x <= 1:
    suma = 0
    k = 0
    while True:
        f = (((-1) ** k) * x ** (2 * k + 3)) / ((2 * k + 1) * (2 * k + 3))
        suma += f
        if abs(f) < 0.001:
            break
        k += 1
    print("x =", round(x, 3), "\t", "y =", round(suma, 4))
    x += 0.1
