def leno(spisok):
    '''Рахунок кількості букв та чмсел в рядку'''
    kil = 0
    for el in spisok:
        if ("a" <= el <= "z") or ("A" <= el <= "Z") or ("0" <= el <= "9"):
            kil += 1
    print("Кількість букв та цифр в даному рядку =", kil)


while True:
    word = list(input("Введіть слово: "))
    if len(word) == 0:
        break
    leno(word)
