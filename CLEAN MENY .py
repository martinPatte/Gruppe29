# DAT120 øving 9_I osv 
# 1 Definerer først allemulige options fra oppgaven og definerer en meny 
from alt_3funksjon import Avtale, ny_avtale

def menu():
    print("[1] Lese inn avtaler fra fil")
    print("[2] Skrive avtalene til fil")
    print("[3] Skrive inn en ny avtale")
    print("[4] Skrive ut alle avtalene")
    print("[0] Avslutt")

menu()
option = int(input("Skriv inn valg her: "))

while option != 0:
    if option == 1:
        print("Alt 1 er valgt")
        

    elif option == 2:
        print("Alt 2 er valgt")
        
        
    elif option == 3:
        print("Alt 3 er valgt")
    
        
    elif option == 4:
        print("Alt 4 er valgt")
       
    

    else:
        print("Invalid option")

    print()
    menu()
    option = int(input("Skriv inn valg her: "))

print("ferdig")

# Alt 1 Lese avtaler fra en fil til ( i )
# Alt 2 Skrive avtalene til en fil ( h )
# Alt 3 Skrive inn en ny avtale ( f )
# Alt 4 Skrive ut alle avtalene ( )
# Alt 5 Avsluttet scriptet ( )