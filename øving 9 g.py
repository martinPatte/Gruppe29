def avtaler():
    class avtale:
      def __init__(self, sted, tidspunkt, lengde):
        self.sted = sted
        self.tidspunkt = tidspunkt
        self.lengde=lengde
    
      def __str__(self):
        return f"  {self.sted} {self.tidspunkt} {self.lengde}"
    
    x=0
    index=0
    while x ==0:
        janei=input("ønsker du å legge til en avtale?: ")
        if janei=="ja":
            p1 = avtale(input("sted hvor avtalen skjer: "),input("dato og tid avtalen skjer: "), input("Hvor lenge avtalen pågår i hele minutter: "))
            overskrift=input("legg til overskrift: ")
            index+=1
            print()
            print(index,overskrift,p1)
            print()
            x=0
        else:
            x=1
      
avtaler()   

        