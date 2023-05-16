from random import randint

def el_printer(lista):  #nie jest to potrzebne ale wyniki sa czyteleniejsze i mniej linijek zajmuje
    for i in lista:
        print( i ,end=" ")
    print("")


while True:
    lista_u =[]
    lista_c =[]
    punkty = 0
    choice = input("1. WYBIERZ SWOJE LICZBY \n2. LOSOWE LICZBY \n3. WYJDZ \nTWOJ WYBOR: ")
    match choice:
        case "1":
            while len(lista_u) <6:
                try:
                    tempvar = int(input("PODAJ LICZBE MIEDZY 1 i 49: "))
                    if tempvar not in lista_u and tempvar<=49 and tempvar>=1:
                        lista_u.append(tempvar)
                    else: raise ValueError
                except ValueError:
                    print("NIEODPOWIEDNI WYBOR")
            el_printer(lista_u)
        case "2":
            while len(lista_u) <6:
                tempvar = randint(1,49)
                if tempvar not in lista_u:
                    lista_u.append(tempvar)
            el_printer(lista_u)
        case "3":
            break
        case _: print("NIEODPOWIEDNI WYBOR")
    if len(lista_u) > 0:
        while len(lista_c) <6:
            tempvar = randint(1,6)
            if tempvar not in lista_c:
                lista_c.append(tempvar)
        el_printer(lista_c)
        for i in lista_u:
            for j in lista_c:
                if i == j: punkty+=1
        if punkty <= 3:
            print("PRZEGRANA")
        elif punkty == 4:
            print("WYGRANA I STOPNIA")
        elif punkty == 5:
            print("WYGRANA II STOPNIA")
        else:
            print("WYGRANA III STOPNIA")
        
        


