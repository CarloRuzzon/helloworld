# esecuzione condizionale

# A volte e' necessario eseguire certe
# istruzioni solo quando si verificano
# particolari condizioni

# Per effettuare scelte si usa il costrutto if-elif-else

# Es.
# siano (x, y) le coordinate
# di un punto nel piano
x = 3
y = 5

# stampa un messaggio diverso a seconda del quadrante
# di appartenenza del punto
if x>0 and y>0:
    print "Il punto si trova nel primo quadrante"

elif x<0 and y>0:
    print "Il punto si trova nel secondo quadrante"

elif x<0 and y<0:
    print "Il punto si trova nel terzo quadrante"

elif x>0 and y<0:
    print "Il punto si trova nel quarto quadrante"

else:
    print "Il punto si trova su un asse"
