def gjennomsnitt(total,antall):
    gjennomsnitt= total/antall
    return gjennomsnitt
fil= open("C:/Users/Martin/Documents/UIS-1. år/DAT-120/Øving/liste.txt",'r')

resultat=0
gammelt_resultat=0
teller=0
for linje in fil:
    teller+=1
    ny_verdi=float(linje)
    resultat=ny_verdi+gammelt_resultat
    gammelt_resultat=resultat
print(f"gjennomsnittsverdien til målingen var {gjennomsnitt(resultat,teller)}")

def maksverdi():
    fil= open("C:/Users/Martin/Documents/UIS-1. år/DAT-120/Øving/liste.txt",'r')

    a=0
    for linje in fil:
        x=float(linje)
        if x > a:
            a=x
        else: x=a
    return x
print((f"maksimalverdien til målingen var {maksverdi()}"))

Jevla fitteoppgave
