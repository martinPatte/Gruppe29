#10.c
class Kategori:
    def __init__(self, ID, navn, prioritet=1):
        self.ID = ID
        self.navn = navn
        self.prioritet = prioritet
        
    def __str__(self):
        return f"id: {self.ID}, navn: {self.navn}, prioritet: {self.prioritet}"

#10.d
def kategorisering(ID, navn, prioritet):
    return(Kategori(ID, navn, prioritet))
#kategorisering(int(input("skriv inn id: ")),input("navn: "),input("prioritet: "))
#f)

def index():
    index =0
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
        return index
#e)    
def Kategori_fil():
    x=0
    while x ==0:
        janei=input("ønsker du å legge til en kategori?: ")
        if janei=="ja":
            p1 = Kategori(int(input("ID: ")),input("navn: "),int(input("prioritet: ")))
            index()
            with open("Kategori.txt", 'a') as filen:
                filen.write(f"\n{index};  {p1} ")
                filen.close()
        else:
            x=1
#f)
#Kategori_fil()
def les_kategori_fil():
    with open("Kategori.txt","r") as fila:
        linje=fila.readline
        for linje in fila:
            print(linje)
#les_kategori_fil()

#g)
class Sted:
    def __init__(self, ID, navn, gateadresse, postnummer, poststed):
        self.ID = ID
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.poststed = poststed
    
    def __str__(self):
        return f"id: {self.ID}, navn: {self.navn}, adresse: {self.gateadresse} {self.postnummer} {self.poststed}"
#h)
def Sted_fil():
    with open("Sted.txt","a") as filen:
        x=0
        while x ==0:
            janei=input("ønsker du å legge til et sted?: ")
            if janei=="ja":
                p1 = Sted(int(input("ID: ")),input("navn: "),input("gateadresse: "), int(input("postnummer: ")), input("poststed: "))
                filen.write(f"\n {p1} ")
                filen.close()
            else:
                x=1

#Sted_fil()
