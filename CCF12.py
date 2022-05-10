from random import randint

def gen_liste_conf():
    liste_duree = []
    for i in range (0,6):
        n = randint(4,10)
        liste_duree.append(n*5)
    return (liste_duree)

def ecc(liste_duree):
    duree_cumul = []
    cumul = 0
    for i in range (0,len(liste_duree)):
        cumul += liste_duree[i]
        duree_cumul.append(cumul)
    return(duree_cumul)

d = gen_liste_conf()
print(ecc(d))    
