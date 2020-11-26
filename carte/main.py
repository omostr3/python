#Memorizzare il seme e il punteggio di due carte da poker. Dire quale delle carte vale di più.  Il valore di una carta da poker è dato in primo luogo dal punteggio e in caso di parità di punteggio dal seme.
#I punteggi in ordine decrescente sono {k,q,j,10,9,8,7,6,5,4,3,2,1}, i semi in ordine decrescente sono  {cuori, quadri, fiori, picche} per i semi memorizzare solo la lettera iniziale del seme.
valori=["1","2","3","4","5","6","7","8","9","j","q","k"]
semi=["p","f","q","c"]
valore=input("Inserire il valore della prima carta\n")
seme=input("Inserire l'iniziale del seme della prima carta\n")
valore1=input("Inserire il valore della seconda carta\n")
seme1=input("Inserire l'iniziale del seme della seconda carta\n")
if valore==valore1 and seme==seme1:
    print("Le carte sono uguali")
else:
    if valori.index(valore)>valori.index(valore1):
        print("La prima carta ha valore maggiore")
    elif valori.index(valore1)>valori.index(valore):
        print("La seconda carta ha valore maggiore")
    elif valori.index(valore1)==valori.index(valore):
        if semi.index(seme)>semi.index(seme1):
            print("La prima carta ha valore maggiore")
        elif semi.index(seme1)>semi.index(seme):
            print("La seconda carta ha valore maggiore")
        else:
            print("Le carte hanno valore uguale")