def Traitement(L):
    R = L[1] + L[2]
    S = L[0] + L[2]

    L[2] = L[0] + L[1]
    L[0] = R
    L[1] = S

    return (L)


def Ecart(L):

    min = L[0]
    max = L[0]

    for i in range (1,3):
        if L[i] < min :
            min = L[i]
        if L[i] > max :
            max = L[i]

    ecart = max - min
    return(ecart)


Liste = []
for i in range(1,4) :
    nbr = int(input("Veuillez entrer un nombre entier (" + str(i) + "/3) : "))
    Liste.append(nbr)
print("Liste innitiale" + str(Liste))

for t in range(1,11) :
    print("Tour " + str(t) + ": " + str(Traitement(Liste)) + " Ecart: " + str(Ecart(Liste)))
