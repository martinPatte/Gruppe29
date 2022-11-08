# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:35:03 2022

@author: Martin
"""

class avtale:
     def __init__(self, tittel, sted, tidspunkt, lengde):
         
         self.sted = sted
         self.tidspunkt = tidspunkt
         self.lengde=lengde
         self.tittel= tittel

     def __str__(self):
        return f" tittel: {self.tittel}; sted: {self.sted}; tidspunkt: {self.tidspunkt}; varighet: {self.lengde}"

class kategori:
    def __init__(self,ID, navn, prioritet):
        self.ID=ID
        self.navn=navn
        self.prioritet=prioritet
    def __str__(self):
        return f"ID: {self.ID}; navn: {self.navn}; prioritet: {self.prioritet}"


def kategorisering(ID,navn,prioritet):
    print(kategori(ID, navn, prioritet))
kategorisering(input("Hilken ID?: "),input("Hvilket navn?: "),input("Hvilket prioritet?: "))

