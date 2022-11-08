import uuid as ide
class avtale:
     def __init__(self, tittel, sted, tidspunkt, lengde):
         
         self.sted = sted
         self.tidspunkt = tidspunkt
         self.lengde=lengde
         self.tittel= tittel

     def __str__(self):
        return f" tittel: {self.tittel}; sted: {self.sted}; tidspunkt: {self.tidspunkt}; varighet: {self.lengde}"

class kategori:
    def __init__(self,navn, prioritet):
        self.navn=navn
        self.prioritet=prioritet
    
    def __str__(self):
        return f"ID: ID'en er: {ide.uuid4()}; navn: {self.navn}; prioritet: {self.prioritet}"


def kategorisering(navn, prioritet):
    print(kategori(navn, prioritet))
kategorisering(input("navn:"),input("prioritet"))