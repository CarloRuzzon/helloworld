#risolviamo le equazioni di 1 grado

a=input("Inserire il coefficiente di x: ")
b=input("Inserire il termine noto: ")
if a==0 and b==0:
  print "l'equazione non esiste."
elif b==0 : 
  print "x = 0"
elif a==0 :
  print "L'equazione e' impossibile,"
else:
  print "x =", -float(b)/float(a)
