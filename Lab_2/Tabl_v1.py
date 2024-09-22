from math import sin, log, log10, e
x = 3.0

while x <= 6:
    if x < 4:
        y = log(x + sin(x), 3)
    elif 4 <= x < 5:
        y = log10(e**x + 4)
    elif x >= 5:
        y = log(log10(x))
    print("x = ", x, "y = ", y)
    x = round(x + 0.2, 2)
