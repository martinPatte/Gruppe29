# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:48:27 2022

@author: Martin
"""

#Lag en funksjon som lar brukeren skrive inn en ny avtale. 
#Funksjonen skal bruke input-
#funksjonen til å lese inn egenskapene til avtalen og skal sjekke at det brukeren 
#skriver er 
#gyldig, for eksempel at varighet er et tall. Funksjonen skal returnere et 
#avtale-objekt 

import datetime as dt

class Avtale:
    def __init__(avtale, sted, starttidspunkt, varighet):
        avtale.sted = sted
        avtale.starttidspunkt = starttidspunkt
        starttidspunkt = dt.datetime.now()
        avtale.varighet = int(varighet)

def ny_avtale(sted, starttidspunkt, varighet):
    objekt = Avtale(sted, starttidspunkt, varighet)
    return objekt
avtale = Avtale(input("sted hvor avtalen skjer: "),input("dato og tid avtalen skjer: "), int(input("Hvor lenge avtalen pågår i hele minutter: ")))
