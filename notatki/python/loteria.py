from random import randint


lista_u = []
lista_c = []

while True:
    choice = input(" 1. WYBIERZ SWOJE LICZBY \n 2. LOSOWE LICZBY \n 3. WYJDZ \n TWOJ WYBOR: ")
    match choice:
        case "1":
            while len(lista_u) <6:
                try:
                    tempvar = int(input(" PODAJ LICZBE MIEDZY 1 i 49: "))
                    if tempvar not in lista_u and tempvar<=49 and tempvar>=1:
                        lista_u.append(tempvar)
                    else: raise ValueError
                except ValueError:
                    print(" NIEODPOWIEDNI WYBOR")
            print(lista_u)

        case "2":
            pass
        case "3":
            break
        case _: print(" NIEODPOWIEDNI WYBOR")

