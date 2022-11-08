import uuid as ide
class kategori:
    def __init__(self,navn, prioritet):
        self.navn=navn
        self.prioritet=prioritet
    
    def __str__(self):
        return f"ID: ID'en er: {ide.uuid4()}; navn: {self.navn}; prioritet: {self.prioritet}"

def ny_Kategori_print():
    x=0
    index=0
    while x ==0:
        janei=input("ønsker du å legge til en kategori?: ")
        if janei=="ja":
            p1 = kategori(input("navn: "),input("prioritet: "))
            
            
            fila="Kategori.txt"
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

ny_Kategori_print()