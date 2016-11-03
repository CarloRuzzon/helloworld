#Risolviamo problemi di 2 grado
import math
a=input("Inserire il coefficiente di x^2: ")
b=input("Inserire il coefficiente di x: ")
c=input("Inserire il termine noto: ")
s = math.pow(b,2) - 4 * a * c
#calcolo delta

if b==0 and c==0:
  print "x = 0"
elif b==0:
  if c>0:
    print "x = +- radice quadrata di", -float(c)/float(a)
  elif c<0:
    print "x = +-", -float(c)/float(a)
elif c==0:
  print "l'equazione e' spuria" 
elif s<=0:
  print "L'equazione e' impossibile per delta minore o uguale a 0"
else:
  sol1=-(float(b)+math.sqrt(s))/2.0
  sol2=-(float(b)-math.sqrt(s))/2.0
  print "x1 =", sol1
  print "x2 =", sol2
