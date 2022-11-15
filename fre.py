from datetime import datetime as dt

class avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet

    def __str__(self):
        return f"Tittel: {self.tittel}, sted: {self.sted}, Starttidspunkt: {self.starttidspunkt}, Varighet: {self.varighet}"

class kategori:
    def __init__(self, id, navn, prioritet=1):
        self.id = id
        self.navn = navn
        self.prioritet = prioritet
    
    def __str__(self):
        return f"ID: {self.id}, Navn: {self.navn}, Prioritet: {self.prioritet}"

class sted:
    def __init__(self, id, navn, gateadresse, postnummer, poststed):
        self.id = id
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.poststed = poststed

    def __str__(self):
        return f"Tittel: {self.id}, Navn: {self.navn}, Gatedresse: {self.gateadresse}, Postnummer: {self.postnummer}, Poststed: {self.poststed} "

def nytt_sted():
    try:
        id = input("ID: ")
        navn = input("Navn: ")
        gateadresse = input("Gateadresse: ")
        poststed = input("Poststed:")
        while True:
            try:
                postnummer = int(input("Postnummer(4 tall)"))
                break
            except ValueError:
                print("Ugyldig postnummer. Prøv igjen.")
                p3 = sted(id, navn, gateadresse, postnummer, poststed)
        return p3
    except ValueError:
        print("Postnummer må skrives med tall.")

def postnummer_sjekk():
    while ValueError:
        try:
            return int(input("Postnummer(4 tall): "))
            break
        except ValueError:
            print("Postnummer må skrives med tall.")

def ny_kategori():
    try:
        
        navn = input("Navn: ")
        id = input("ID: ")
        while True:
            try:
                prioritet = int(input("Prioritet( 1,2 eller 3: "))
                break
            except ValueError:
                print("Ugyldig prioritet. Prøv igjen.")
        p2 = kategori(id, navn, prioritet)
        return p2
    except ValueError:
        print("Prioritet må skrives med tall.")

def prioritet_sjekk():
    while ValueError:
        try:
            return int(input("Prioritet (i tall): "))
            break
        except ValueError:
            print("Prioritet må skrives med tall.")

def ny_avtale():
    try:
        tittel = input("Tittel: ")
        sted = input("Sted: ")
        while True:
            try:
                starttidspunkt = dt.fromisoformat(input("Starttidspunkt (ÅÅÅÅ-MM-DD HH:MM:SS): "))
                varighet = int(input("Varighet (i minutter): "))
                break
            except ValueError:
                print("Ugyldig dato eller ugyldig varighet. Prøv igjen")
                p1 = avtale(tittel, sted, starttidspunkt, varighet)
        return p1
    except ValueError:
            print("Varigheten må skrives i tall")

def Dato_sjekk():
    while ValueError:
        try:
            return dt.fromisoformat(input("Starttidspunkt (ÅÅÅÅ-MM-DD HH:MM:SS):"))
            break
        except ValueError:
            print("Starttidspunkt må skrives på format (ÅÅÅÅ-MM-DD HH:MM:SS): ")

def varighet_sjekk():
    while ValueError:
        try:
            return int(input("Varigheten på avtalen(i minutter): "))
            break
        except ValueError:
            print("Avtalevarigheten må skrives med tall")

def printNyAvtale():
    x = 0
    index = 0
    while x == 0:
        NeiJA = input("Ønsker du å legge til en ny avtale?:")
        if NeiJA == "ja" or NeiJA =="Ja" or NeiJA == "JA":
            p2 = kategori(input("ID:"), input("Navn på kategori: "), prioritet_sjekk())
            p3 = sted(input("ID:"), input("Navn på sted: "), input("Gateadresse: "), postnummer_sjekk(), input("Poststed"))
            p1 = avtale(input("Tittel på avtale: "), input("Sted hvor avtalen skal foregå: "), Dato_sjekk(), varighet_sjekk())

            fil = "Øvinger/Øving10/Demofil.txt"
            with open(fil, "r") as fila:
                listeMedLinjer = fila.readlines()
                if len(listeMedLinjer) == 0:
                    index = 1
                else:
                    siste_index = (listeMedLinjer[-1])
                    riktig_index = siste_index.split(";")
                    index = int(riktig_index[0])
                    index = index + 1
            print(index, p2, p3, p1)
        else:
            x = 1

def NyAvtaleFil():
    x = 0
    index = 0
    while x == 0:
        JaNei = input("Ønsker du å legge til en ny avtale?:")
        if JaNei == "ja" or JaNei == "Ja" or JaNei== "JA":
            p2 = kategori(input("ID:"), input("Navn på kategori: "), prioritet_sjekk())
            p3 = sted(input("ID:"), input("Stedsnavn: "), input("Gateadresse: "), postnummer_sjekk(), input("Poststed: "))
            p1 = avtale(input("Tittel: "), input("Sted hvor avtalen skal foregå: "), Dato_sjekk(), varighet_sjekk())

            fil = "Øvinger/Øving10/Demofil.txt"
            with open(fil, "r") as fila:
                listeMedLinjer = fila.readlines()
                if len(listeMedLinjer) == 0:
                    index = 1
                else:
                    siste_index = (listeMedLinjer[-1])
                    riktig_index = siste_index.split(";")
                    index = int(riktig_index[0])
                    index = index + 1
                with open(fil, "a") as fila:
                    fila.write(f"\n{index}; Kategori: {p2}, Sted: {p3}, Avtale: {p1}")
                    fila.close()
        else:
            x = 1

print("Alternativ 1 er valgt")
liste = []
def LesInnAvtaler():
    fil = open("Øvinger/Øving10/Demofil.txt", "r")
    linje = fil.readline
    for linje in fil:
        liste.append(linje)
        print(liste)

def AvtalesamlingSted():
    søk = input("Stedet til avtalen du vil finne er: ")
    with open("Øvinger/Øving10/Demofil.txt", "r+") as fila:
        ny_fil = fila.readlines()
        fila.seek(0)
        for linje in ny_fil:
            if søk not in linje:
                fila.write(linje)
            else:
                print(linje)
                fila.write(linje)
        fila.truncate(),

def AvtalesamlingDato():
    søk = input("finn avtaler på denne datoen: ")
    with open("Øvinger/Øving10/Demofil.txt", "r+") as fila:
        ny_fil = fila.readlines()
        fila.seek(0)
        for linje in ny_fil:
            if søk not in linje:
                fila.write(linje)
            else:
                print(linje)
                fila.write(linje)
        fila.truncate()

def AvtalesamlingTittel():
    søk = input("Tittelen til avtalen du vil finne er:")
    with open("Øvinger/Øving10/Demofil.txt", "r+") as fila:
        ny_fil = fila.readlines()
        fila.seek(0)
        for linje in ny_fil:
            if søk not in linje:
                fila.write(linje)
            else:
                print(linje)
                fila.write(linje)
        fila.truncate()

def PrintAvtaler():
    fil = open("Øvinger/Øving10/Demofil.txt", "r")
    linje = fil.readline
    for linje in fil:
        print(linje)

def FjernAvtale():
    søk = input("Hvilken avtale skal fjernes?: ")
    with open("Øvinger/Øving10/Demofil.txt", "r+") as fila:
        ny_fil = fila.readlines()
        fila.seek(0)
        for linje in ny_fil:
            if søk not in linje:
                fila.write(linje)
        fila.truncate()

def RedigereAvtale():
    søk = input("Hvilken avtale skal fjernes?: ")
    with open("Øvinger/Øving10/Demofil.txt", "r+") as fila:
        ny_fil = fila.readlines()
        fila.seek(0)
        for linje in ny_fil:
            if søk not in linje:
                fila.write(linje)
            else:
                p1 = avtale(input("Tittel: "), input("Sted hvor avtalen skal foregå: "), Dato_sjekk(), varighet_sjekk())
                fila.write(f"{søk}; {p1} \n")
        fila.truncate()

def Kategoriavtale():
    x = 0
    index = []
    while x == 0:
        JaNei = input("Ønsker du å legge til en ny kategori?:")
        if JaNei == "ja" or JaNei == "Ja" or JaNei== "JA":
            p2 = kategori(input("ID:"), input("Navn på kategori: "), prioritet_sjekk())
            
            fil = "Øving10/Demofil.txt"
            with open(fil, "r") as fila:
                listeMedLinjer = fila.readlines()
                if len(listeMedLinjer) == 0:
                    index = 1
                else:
                    siste_index = (listeMedLinjer[-1])
                    riktig_index = siste_index.split(";")
                    index = int(riktig_index[0])
                    index = index + 1
                with open(fil, "a") as fila:
                    fila.write(f"\n{index}; Kategori: {p2}")
                    fila.close()
        else:
            x = 1

    print(p2)





def Meny():
    print("[1] Lese inn avtaler fra fila")
    print("[2] Skrive avtalene til fila")
    print("[3] Skrive inn en ny avtale")
    print("[4] Skrive ut alle avtalene")
    print("[5] Slett avtale")
    print("[6] Rediger avtale")
    print("[7] Finn avtaler som foregår på bestemt valgt sted")
    print("[8] Legg til kategori i systemet")
    print("[9] Legg til sted i systemet")
    print("[10] Legg til kategori i avtale")
    print("[0] Avslutt")

Meny()
alternativ = int(input("Skriv inn alternativ her:"))
while alternativ != 0:
    if alternativ == 1:
        print("Alternativ 1 er valgt")
        LesInnAvtaler()
    elif alternativ == 2:
        print("Alternativ 2 er valgt")
        NyAvtaleFil()
    elif alternativ == 3:
        print("Alternativ 3 er valgt")
        NyAvtaleFil()
    elif alternativ == 4:
        print("Alternativ 4 er valgt")
        PrintAvtaler()
    elif alternativ == 5:
        print("Alternativ 5 er valgt")
        FjernAvtale()
    elif alternativ == 6:
        print("Alternativ 6 er valgt")
        RedigereAvtale()
    elif alternativ == 7:
        print("Alternativ 7 er valgt")
        AvtalesamlingSted()
    elif alternativ == 8:
        print("Alternativ 8 er valgt")
        ny_kategori()
    elif alternativ == 10:
        print("Alternativ 10 er valgt")
        Kategoriavtale()
   
    else:
        print("Ugyldig alternativ")
    
    print()
    Meny()
    alternativ = int(input("Skriv inn alternativ her: "))

print("Ferdig")