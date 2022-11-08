#10i)
class Sted:
    def __init__(self, ID, navn, gateadresse, postnummer, poststed):
        self.ID = ID
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.poststed = poststed
    
    def __str__(self):
        return f"id: {self.ID}, navn: {self.navn}, adresse: {self.gateadresse} {self.postnummer} {self.poststed}"

def Kategori_fil():
    open("Sted.txt","a")

    x=0
    index=0
    while x ==0:
        janei=input("ønsker du å legge til et sted?: ")
        if janei=="ja":
            p1 = Sted(int(input("ID: ")),input("navn: "),input("gateadresse: "), int(input("postnummer: ")), input("poststed: "))
            
            
            fila="Sted.txt"
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
sted_liste=[]
def print_append_sted_fil():
    
    with open("Sted.txt","r") as fila:
        linje=fila.readline
        for linje in fila:
            print(linje)
            sted_liste.append(linje)
print_append_sted_fil()

#10k)