class avtale:
    def __init__(self, tittel, sted, tidspunkt=0, lengde=0):
        self.tittel = tittel
        self.sted = sted
        self.tidspunkt = tidspunkt
        self.lengde=lengde

    def __str__(self):
        return f"{self.tittel};{self.sted};{self.tidspunkt};{self.lengde}"
    

def lagre_avtaler(avtaleliste):
    with open("avtaler.txt", "w", encoding="UTF8") as fila:
        for avtale in avtaleliste:
            fila.writelines(str(avtale))
     
            
a = avtale("a", "b")
b = avtale("c", "d")

avtaleliste = [a, b]

lagre_avtaler(avtaleliste)
