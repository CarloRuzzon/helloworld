#sfera o cubo?
import math
scelta=input("Premere 1 per scegliere il cubo e 2 per la sfera: ")
if scelta == 1:

  lato=input("Inserire il lato del cubo: ")
  volumel= lato * lato *lato
  print "Il volume del cubo e'", volumel

elif scelta==2:

  raggio=input("Inserire il raggio della sfera: ")
  volumes= 4.0/3.0 * math.pi * r * r * r
  print "Il volume della sfera e'", volumes
