

class avtale:
     def __init__(self, sted, tidspunkt, lengde):
         self.sted = sted
         self.tidspunkt = tidspunkt
         self.lengde=lengde
    
     def __str__(self):
        return f"sted: {self.sted}; tidspunkt: {self.tidspunkt}; varighet: {self.lengde}"
def avtaler():    
    x=0
    index=0
    while x ==0:
        janei=input("ønsker du å legge til en avtale?: ")
        if janei=="ja":
            p1 = avtale(input("sted hvor avtalen skjer: "),input("dato og tid avtalen skjer: "), input("Hvor lenge avtalen pågår i hele minutter: "))
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
      
avtaler()   
