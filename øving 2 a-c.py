
for x in range(5):
    
    try:
        gammel_verdi=float(input("skriv inn gammel verdi: "))
        ny_verdi= float(input("skriv inn ny verdi: "))
        resultat=(ny_verdi-gammel_verdi)
        if resultat<0:
            print("Verdien har sunket med: ")
            print(resultat*-1)
        elif resultat==0:
            print("verdien er uforandret")
        else:
            print("verdien har steget med: ")
            print(resultat)
    except ValueError:
        print("skriv kun nummer!")
    print()
    
