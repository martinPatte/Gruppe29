# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:48:47 2022

@author: arne0
"""

#9.d
import datetime as dt

class Avtale:
    def __init__(avtale, sted, starttidspunkt, varighet):
        avtale.sted = sted
        avtale.starttidspunkt = starttidspunkt
        starttidspunkt = dt.datetime.now()
        avtale.varighet = int(varighet)
        
print(dt.datetime.now())


def liste_med_avtaler (avtale)