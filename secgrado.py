#Risolviamo problemi di 2 grado
import math
a=input("Inserire il coefficiente di x^2: ")
b=input("Inserire il coefficiente di x: ")
c=input("Inserire il termine noto: ")
s = math.pow(b,2) - 4 * a * c
#calcolo delta

if a==0 and b==0 and c==0:
  print "L'eq e' 0"
elif a==0 and b==0:
  print "0 =", c
elif a==0 and c==0 or b==0 and c==0:
  print a, "=0"
else:
  s = math.pow(b,2) - 4 * a * c
  if s<=0:
    print "L'equazione e' inpossibile per delta minore o uguale a 0"
  else:
    sol1=-(float(b)+math.sqrt(s))/2.0
    sol2=-(float(b)-math.sqrt(s))/2.0
    print "x1 =", sol1
    print "x2 =", sol2
