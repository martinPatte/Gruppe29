# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 08:39:01 2022

@author: arne0
"""

#9.d
import datetime as dt

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
        
        
    def __str__(self):
        return f"tittel:{self.tittel}; sted: {self.sted}; tidspunkt: {self.starttidspunkt}; varighet: {self.varighet}"
    

def ny_avtale():
    try:   
        tittel = input ("Tittel: ")
        sted = input ("Sted: ")
        while True:
            try:
                tidspunkt = dt.fromisoformat(input("Tidspunkt (ÅÅÅÅ-MM-DD HH:MM:SS): "))
                lengde = int(input("Lengde (i minutter): "))
                break
            except ValueError:
                print ("Ugyldig dato, eller ugyldig lengde. Prøv igjen")
        return Avtale(tittel, sted, tidspunkt, lengde)
    except ValueError:
        print("avtalelengden må skrives i tall")
        
        
def indeksering(avtaleliste, overskrift = "overskrift"):
    #janei=input("ønsker du å legge til en avtale?: ")
    for index, avtale in enumerate(avtaleliste):
        print(index,avtale)
        
def les_avtale(avtale_liste):
    open("fila.txt", 'r') as filen:
        list_of_lines = filen.readlines()
        if len(list_of_lines)==0:
            index=1
        
   ################# 
    


            
        
            

if __name__=="__main__":
    l = []
    l1 = Avtale("Fest", "Hjemme", "03-03-2022 10:00:00", 120)
    l2 = Avtale("Jobb", "Hjemme", "04-04-2021 10:00:00", 120)
    l3 = Avtale("Whatever", "Hjemme", "03-03-2022 10:00:00", 120)
    l.append(l1)
    l.append(l2)
    l.append(l3)
    indeksering(l)
    
    
    #avtaler()