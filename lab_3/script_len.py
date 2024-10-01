сount = 0
word = input("Введіть слово:")
word = list(word)
print(word)
for el in word:
    if ("a" <= el <= "z") or ("A" <= el <= "Z") or ("0" <= el <= "9"):
        сount += 1
print(сount, "букв та цифр знаходиться в даному рядку")
