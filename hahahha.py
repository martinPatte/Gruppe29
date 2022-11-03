# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:59:43 2022

@author: Olive
"""

  print("Alt 1 er valgt")
  liste=[]
  def lesinn_avtaler():
     
      fil= open("demofile2.txt","r")
      linje=fil.readline
      for linje in fil:
          print(linje)
          liste.append(linje)
  lesinn_avtaler()