'''
Les varibles utilisées sont :
- Test = Bool
- i = int
- Tableau = []
'''
import random

Tableau = []
gagne = 0
perdu = 0

def fonction_A (Tableau):
    Test = True
    somme = 0
    for i in range (0,4) :
        if (Tableau[i] == 1):
            Test = False
        somme = Tableau[i] + somme
        if (Tableau[0] + Tableau[1] + Tableau[2] + Tableau[3] + Tableau[4] <= 18):
            Test = False
    return Test

def fonction_tirage() :
    for i in range (5): 
        Tableau.append(random.randint(1,6))

for i in range (100):
    fonction_tirage()

    if (fonction_A(Tableau) == False) :
        perdu = perdu + 1
    else :
        gagne = gagne + 1
    

print ("Vous avez perdu ",perdu,"parties")
print ("Vous avez gagné ",gagne,"parties")
