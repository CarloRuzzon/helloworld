#risolviamo le equazioni di 1 grado

a=input("Inserire il coefficiente di x: ")
b=input("Inserire il termine noto: ")
if b==0 : 
  print "x = 0"
elif a==0 :
  print "L'equazione e' impossibile"
else:
  print "Il risultato e'", -b/a
