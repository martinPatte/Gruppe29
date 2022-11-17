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
Sted_fil()
sted_liste=[]
def print_append_sted_fil():
    
    with open("Sted.txt","r") as fila:
        linje=fila.readline
        for linje in fila:
            print(linje)
            sted_liste.append(linje)
print_append_sted_fil()

