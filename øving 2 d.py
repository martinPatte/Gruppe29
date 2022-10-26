alder=int(input("Hvor mange år er du?: "))
if alder<4:
    print("Du har gratis inngang")
elif 4<=alder<=16:
    print("Inngang koster 45kr")
elif 16<alder<67:
    x=input("Er du student? skriv ja eller nei: ")
    if x=="ja" and "Ja" : print("inngang koster 50kr")
    else: print ("inngang koster 90kr")
elif alder<0: print("Alder kan ikke være negativ")
else: print("inngang koster 50kr")
  
    
    
    

    
    
