from datetime import datetime as dt
#d)
class avtale:
     def __init__(self, tittel, sted, tidspunkt, lengde):
         self.sted = sted
         self.tidspunkt = tidspunkt
         self.lengde=lengde
         self.tittel= tittel
#e)
     def __str__(self):
        return f" tittel: {self.tittel}; sted: {self.sted}; tidspunkt: {self.tidspunkt}; varighet: {self.lengde}"

#f)
def ny_avtale():
    try:   
        tittel = input ("Tittel: ")
        sted = input ("Sted: ")
        while True:
            try:
                tidspunkt = dt.fromisoformat(input("Tidspunkt (ÅÅÅÅ-MM-DD HH:MM:SS): "))
                lengde = int(input("Lengde (i minutter): "))
                break
            except ValueError:
                print ("Ugyldig dato, eller ugyldig lengde. Prøv igjen")
                p1=avtale(tittel, sted, tidspunkt, lengde)
        return p1
    except ValueError:
        print("avtalelengden må skrives i tall")
#g)
def Dato_check():
    while ValueError:
        try:
            return dt.fromisoformat(input("Tidspunkt (ÅÅÅÅ-MM-DD HH:MM:SS): "))
            break
        except ValueError:
            print("tidspunkt må skrives på format (ÅÅÅÅ-MM-DD HH:MM:SS)")
        
def lengde_check():
    while ValueError:
        try:
            return int(input("lengden på møte: "))
            
            break
        except ValueError:
            print("avtalelengden må skrives med tall")

def ny_avtale_print():
    x=0
    index=0
    while x ==0:
        janei=input("ønsker du å legge til en avtale?: ")
        if janei=="ja":
            p1 = avtale(input("tittel: "),input("sted hvor avtalen skjer: "),Dato_check(), lengde_check())
            
            
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

            print(index,p1)
        else:
            x=1

#h)
def ny_avtale_fil():
    x=0
    index=0
    while x ==0:
        janei=input("ønsker du å legge til en avtale?: ")
        if janei=="ja":
            p1 = avtale(input("tittel: "),input("sted hvor avtalen skjer: "),Dato_check(), lengde_check())
            
            
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
                with open(fila, 'a') as filen:
                    filen.write(f"\n{index};  {p1} ")
                    filen.close()
        else:
            x=1



#i)
print("Alt 1 er valgt")
liste=[]
def lesinn_avtaler():
     
    fil= open("demofile2.txt","r")
    linje=fil.readline
    for linje in fil:
        
        liste.append(linje)



#j)
def dato_avtalesamling():
    searched = input("finn avtaler for denne datoen: ") 
    with open("demofile2.txt","r+") as f: 
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if searched not in line:
                f.write(line)

            else:
                print(line)
                f.write(line)
        f.truncate() 
            
#k)
def tittel_avtalesamling():
    searched = input("Tittelen til avtalen du vil finne: ") 
    with open("demofile2.txt","r+") as f: 
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if searched not in line:
                f.write(line)

            else:
                print(line)
                f.write(line)
        f.truncate() 

#valg4
def print_avtaler():
    fil= open("demofile2.txt","r")
    linje=fil.readline
    for linje in fil:
        print(linje)
#valg 5
def Fjerne_avtale():
    searched = input("hvilken avtale skal fjernes?: ") # every line containing the variable "searched" will be deleted
            
    with open("demofile2.txt","r+") as f: # open your file
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if searched not in line:
                f.write(line)
        f.truncate() 

#valg6                     
def Redigere_avtale():
    searched = input("hvilken avtale skal fjernes") 
    with open("demofile2.txt","r+") as f: 
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if searched not in line:
                f.write(line)

            else:
                p1 = avtale(input("ny tittel: "),input("nytt sted hvor avtalen skjer: "),input("ny dato og tid avtalen skjer: "), input("Hvor lenge avtalen pågår i hele minutter: "))
                f.write(f"{searched}; {p1} \n")
        f.truncate()   
#l, m, n)
def menu():
    print("[1] Lese inn avtaler fra fil")
    print("[2] Skrive avtalene til fil")
    print("[3] Skrive inn en ny avtale")
    print("[4] Skrive ut alle avtalene")
    print("[5] slett avtale")
    print("[6] rediger avtale")
    print("[0] Avslutt")

menu()
option = int(input("Skriv inn valg her: "))

while option != 0:
    if option == 1:
        print("Alt 1 er valgt")
        lesinn_avtaler()

    elif option == 2:
        print("Alt 2 er valgt")
        ny_avtale_fil()
        
    elif option == 3:
        print("Alt 3 er valgt")
        ny_avtale_fil()
        
    elif option == 4:
        print("Alt 4 er valgt")
        print_avtaler()
    
    elif option == 5:
        print("Alt 5 er valgt")
        Fjerne_avtale()
    elif option == 6:    
        print("Alt 6 er valgt")
        Redigere_avtale()
    else:
        print("Invalid option")

    print()
    menu()
    option = int(input("Skriv inn valg her: "))

print("ferdig")
#m)

