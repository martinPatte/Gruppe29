# DAT120 øving 9_I osv 
# 1 Definerer først allemulige options fra oppgaven og definerer en meny 
from alt_3funksjon import Avtale, ny_avtale

def menu():
    print("[1] Lese inn avtaler fra fil")
    print("[2] Skrive avtalene til fil")
    print("[3] Skrive inn en ny avtale")
    print("[4] Skrive ut alle avtalene")
    print("[5] Slette en avtale")
    print("[0] Avslutt")

menu()
option = int(input("Skriv inn valg her: "))

while option != 0:
    if option == 1:
        print("Alt 2 er valgt")
        liste=[]
        def lesinn_avtaler():
           
            fil= open("demofile2.txt","r")
            linje=fil.readline
            for linje in fil:
                print(linje)
                liste.append(linje)
        lesinn_avtaler()


    elif option == 2:
        print("Alt 2 er valgt")
        class per:
             def __init__(self, sted, tidspunkt, lengde):
                 self.sted = sted
                 self.tidspunkt = tidspunkt
                 self.lengde=lengde
            
             def __str__(self):
                return f"sted: {self.sted}; tidspunkt: {self.tidspunkt}; varighet: {self.lengde}"
        def perolav():    
            x=0
            index=0
            while x ==0:
                janei=input("ønsker du å legge til en avtale?: ")
                if janei=="ja":
                    p1 = per(input("sted hvor avtalen skjer: "),input("dato og tid avtalen skjer: "), input("Hvor lenge avtalen pågår i hele minutter: "))
                    overskrift=input("legg til overskrift: ")
                    
                    fila="demofile2.txt"
                    with open(fila, 'r') as filen:
                        list_of_lines = filen.readlines()
                        if len(list_of_lines)==0:
                            index=1
                        else:
                            
                            siste_index=(list_of_lines[-1])
                            selve_index = siste_index.split(";")
                            index=int(selve_index[0])
                            index=index+1
                    print()
                    print(index,overskrift,p1)
                    print()
                    x=0
                    f = open("demofile2.txt", "a")
                    f.write(f"\n {index}; {overskrift}; {p1} ")
                    f.close()
               
        
                else:
                    x=1
        perolav()
        
    elif option == 3:
        perolav()
        
        
    elif option == 4:
        print("Alt 4 er valgt")
        def print_avtaler():
            fil= open("demofile2.txt","r")
            linje=fil.readline
            for linje in fil:
                print(linje)

        print_avtaler()
    
    elif option == 5:
        print("Alt 5 er valgt")
        def Fjerne_avtale():
            searched = input("hvilken avtale skal fjernes?: ") # every line containing the variable "searched" will be deleted
            
            with open("demofile2.txt","r+") as f: # open your file
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if searched not in line:
                        f.write(line)
                f.truncate() 
        Fjerne_avtale()

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



