'''
A-1)
11 * 3 + 1 = 34
34 / 2 = 17
17 * 3 + 1 = 52
52 / 2 = 26
26 / 2 = 13
13 * 3 + 1 = 40
40 / 2 = 20
20 / 2 = 10
10 / 2 = 5
5 * 3 + 1 = 16
16 / 2 = 8
8 / 2 = 4
4 / 2 = 2
2 / 2 = 1 

La suite d'entier du vol n°11 est : 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

Sa durée de vol est de 14

Son altitude maximal est de 52

A-2)
La première ligne de cet algorithme sert à faire un test pour savoir si le nombre est pair

L'algorithme affichera 46 si n=15

L'algorithme affichera 24 si n=48
'''

numerovol = int(input("Veuillez indiquer le numéro du vol : "))
numero = numerovol
tablo = []
tour = 1
durealt = 0
altmax = 0


while (numero != 1) :
    if (numero % 2 == 0) :
        numero = numero / 2
        tablo.append(numero)
        if (numerovol <= numero) :
            durealt = durealt + 1
        if (altmax < numero) :
            altmax = numero

    else :
        numero = numero * 3 + 1
        tablo.append(numero)
        if (numerovol <= numero) :
            durealt = durealt + 1
        if (altmax < numero) :
            altmax = numero

print ("La suite est : ",tablo)
print ("La durée de vol est de :",len(tablo))
print ("La durée de vol en altitude est de :",durealt)
print ("L'altitude maximale est de :",altmax)