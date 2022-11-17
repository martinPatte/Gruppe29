from datetime import datetime as dt
def ny_avtale_med_kategori():
    class avtale:
        def __init__(self, tittel, sted, tidspunkt, lengde):
             
             self.sted = sted
             self.tidspunkt = tidspunkt
             self.lengde=lengde
             self.tittel= tittel
             self.kategori = selve_kategorien
        def __str__(self):
            return f"tittel: {self.tittel}; sted: {Sted(input('ID: '), input('navn: '), input('gateadresse: '), input('postnummer: '), input('poststed: '))}; tidspunkt: {self.tidspunkt}; varighet: {self.lengde}; kategorivalg:{self.kategori}"
    
        def append_kategori_fil(self):
            self.kategori.append(kategori_valg())
            
    class Sted:
        def __init__(self, ID, navn, gateadresse, postnummer, poststed):
            self.ID = ID
            self.navn = navn
            self.gateadresse = gateadresse
            self.postnummer = postnummer
            self.poststed = poststed
        
        def __str__(self):
            return f"id: {self.ID}, navn: {self.navn}, adresse: {self.gateadresse} {self.postnummer} {self.poststed}"
    
            
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
    kategori=[]
    
    
    selve_kategorien=[]
    def kategori_valg():
        janei="ja"
        while janei=="ja":
            janei = input("ønsker du å legge til en ny kategori til avtalen?: ")
            
            if janei=="ja":
                with open("Kategori.txt","r") as fila:
                    linje=fila.readline
                    for linje in fila:
                        kategori.append(linje)
                        print(linje)
                    print()
                    kategorien=(kategori[int(input("hvilke kategori Index skal hentes?: "))])
                    selve_kategorien.append(kategorien)
            else:
                janei!="ja"
            
    def ny_avtale_fil():      
          p1 = avtale(input("tittel: "),input("sted hvor avtalen skjer: "),Dato_check(), lengde_check())
          with open("demofile2.txt", 'a') as filen:
              filen.write(f"\n{index()};  {p1} ")
              filen.close()
          
    kategori_valg()
    ny_avtale_fil()
ny_avtale_med_kategori()