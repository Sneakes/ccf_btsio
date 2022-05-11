def compte1(tab) :
    cumul = 0
    for i in range(24):
        if (tab[i] == 1):
            cumul = cumul +1
    return cumul

def fin(tab1, tab2):
    
    if ( compte1(tab1) == 0):
        return 2
    elif ( compte1(tab2) == 0):
        return 1
    else :
        return 0
    
def Mystere() :
    tab = [0]*24
    for i in range (6):
        print("emplacementdu bateau numéro" , i,"?")
        j = int(input("emplacement:"))
        if j>23:
            print( " impossible à placer, voyons! Il faut recommencer!")
            j = int(input("Nouvel emplacement:"))
        while (tab[j] != 0):
            print("emplacement deja pris")
            j = int(input("emplacemenent:"))
            if j>23:
                print( " impossible à placer, voyons! Il faut recommencer!")
                j = int(input("Nouvel emplacement:"))
        tab[j] = 1
    print(tab)
    return tab


        
            
    
#autre algo de partie:
print ( " joueur 1")
tab1 = Mystere()
print ( " joueur 2")
tab2 = Mystere()
gagnant = 0 
joueur=1

while(gagnant == 0) :
    if joueur==1:
        attaque=int(input("Joueur1, saisiir l'emplacement à attaquer : " ))
        if tab2[attaque] ==1:
            print("Coulé!")
            tab2[attaque]=2
        else:
            print( "Dans l'eau !")
        joueur = 2
        attaque=int(input("Joueur1, saisiir l'emplacement à attaquer : " ))
        if tab1[attaque] ==1:
            print("Coulé!")
            tab1[attaque]=2
        else:
            print( "Dans l'eau !")
        joueur=1
        gagnant=fin(tab1, tab2)
print("Le gagnant est : ", gagnant)
