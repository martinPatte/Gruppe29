import uuid as ide

    
class kategori:
    def __init__(self,navn, prioritet):
        self.navn=navn
        self.prioritet=prioritet
    
    def __str__(self):
        return f"ID: ID'en er: {ide.uuid4()}; navn: {self.navn}; prioritet: {self.prioritet}"

def Kategori_fil():
    open("Kategori.txt","a")

    x=0
    index=0
    while x ==0:
        janei=input("ønsker du å legge til en kategori?: ")
        if janei=="ja":
            p1 = kategori(input("navn"),input("prioritet"))
            
            
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
                with open(fila, 'a') as filen:
                    filen.write(f"\n{index};  {p1} ")
                    filen.close()
        else:
            x=1
#Kategori_fil()
def les_kategori_fil():
    with open("Kategori.txt","r") as fila:
        linje=fila.readline
        for linje in fila:
            print(linje)
les_kategori_fil()
    