import datetime as dt


class avtale:
     def __init__(self, tittel, sted, tidspunkt, lengde):
         self.sted = sted
         self.tidspunkt = tidspunkt
         self.lengde=lengde
         self.tittel= tittel
     def __str__(self):
        return f" tittel: {self.tittel}; sted: {self.sted}; tidspunkt: {self.tidspunkt}; varighet: {self.lengde}"
def avtaler():    
    x=0
    index=0
    while x ==0:
        janei=input("ønsker du å legge til en avtale?: ")
        if janei=="ja":
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
                        return avtale(tittel, sted, tidspunkt, lengde)
            except ValueError:
                print("avtalelengden må skrives i tall")
            
            
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
                        print(index,p1)
                        print()
                        x=0
                        f = open("demofile2.txt", "a")
                        f.write(f"\n{index};  {p1} ")
                        f.close()
        else:
            x=1
    
avtaler()