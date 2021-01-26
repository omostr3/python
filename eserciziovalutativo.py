a=0
while(a!=6):
  print("Inserire 1 per inserire una persona")
  print("Inserire 2 per stampare nome e cognome delle persone con età inferiore a 18 anni")
  print("Inserire 3 per stampare nome e cognome dei ragazzi più alti di 1.60")
  print("Inserire 4 per stampare il numero di persone con peso maggiore di 70kg")
  print("Inserire 5 per stampare il numero di persone più alte di 1.80 e con età inferiore a 25")
  print("Inserire 6 per terminare il programma")
  a=int(input())
  if(a==1):
    nome=input("Inserire il nome ")
    cognome=input("Inserire il cognome ")
    eta=input("Inserire l'età ")
    altezza=input("Inserire l'altezza in metri; es 1.84 ")
    peso=input("Inserire il peso ")
    f=open("file.txt","a")
    f.write(nome+" , "+cognome+" , "+eta+" , "+altezza+" , "+peso+"\n")
    f.close()
  elif(a==2):
    f=open("file.txt","r")
    for i in f:
      z=i.split(",")
      z[2]=int(z[2])
      if(z[2]<18):
       print("Nome: "+z[0]+" Cognome: "+z[1])
    f.close()
  elif(a==3):
    f=open("file.txt","r")
    for i in f:
      z=i.split(",")
      z[3]=float(z[3])
      if(z[3]>1.60):
        print("Nome: "+z[0]+" Cognome: "+z[1])
    f.close()
  elif(a==4):
    j=0
    f=open("file.txt","r")
    for i in f:
      z=i.split(",")
      z[4]=int(z[4])
      if(z[4]>70):
       j+=1
    print("Persone con peso maggiore di 70kg: "+i)
    f.close()
  elif(a==5):
    j=0
    f=open("file.txt","r")
    for i in f:
      z=i.split(",")
      z[3]=float(z[3])
      z[2]=int(z[2])
      if(z[3]>1.8 and z[2]<25):
       j+=1
    print("Persone più alte di 1.80 e età inferiore a 25: "+i)
    f.close()
  elif(a==6):
    print("Arrivederci")
 
