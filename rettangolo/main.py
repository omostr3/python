base=int(input("Inserire la lunghezza della base\n"))
altezza=int(input("Inserire la lunghezza dell'altezza\n"))

spazio=" "
for i in range(altezza):
    if i == 0 or i == altezza-1:
         print(base*'*')
    else:
         print('*' + spazio*(base-2) +'*')


