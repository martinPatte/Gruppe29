class avtale:
     def __init__(self,tittel, sted, tidspunkt, lengde):
         self.sted = sted
         self.tidspunkt = tidspunkt
         self.lengde=lengde
         self.tittel=tittel
    
     def __str__(self):
        return f"sted: {self.sted}; tidspunkt: {self.tidspunkt}; varighet: {self.lengde}"
open("demofile2.txt","r")  
       
def Redigere_avtale():
    searched = input("hvilken avtale skal fjernes") 
    with open("demofile2.txt","r+") as f: 
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if searched not in line:
                f.write(line)

            else:
                p1 = avtale(input("ny tittel: "),input("nytt sted hvor avtalen skjer: "),input("ny dato og tid avtalen skjer: "), input("Hvor lenge avtalen pågår i hele minutter: "))
                f.write(f"{searched}; {p1} \n")
        f.truncate() 
            
                       
        
Redigere_avtale()