"""
Question 1 - Variables utilisées

    Les variables utilisées sont :

        j1 → Nombre entier
        j2 → Nombre entier
        n  →  Nombre Entier
        scores_possibles → Tableau
        T  → Tableau 
        i  → Nombre entier


Question 2 - Instruction manquante :

    L'instruction manquante en ligne 2 est 
    j1 ← 0


Question 3 - Traitement + Valeurs successives :

    J1      J2

    15      00
    15      15
    15      30
    30      30
    40      30

Question 4 - Compléter l'algorithme :

    T ← ["A", "B", "B", "A", "A", "A"]
    j1 ← 0
    j2 ← 0
    n ← taille(T)
    scores_possibles ← [0,15,30,40]
    Pour i allant de 0 à n-2 :
        Si T[i] = "A":
            j1 ← j1+1
        Sinon
            j2 ← j2+1
        Fin Si
        Afficher scores_possibles[j1],scores_possibles[j2]
    Fin Pour
    Si scores_possibles[j1] = 40 : 
        Retourner "Joueur A gagnant"
    Sinon
        Retourner "Joueur B gagnant"
    Fin Si


Question 5 - Que se produit-il si on  entre le tableau T = ["B", "B", "A", "A", "A", "B", "A", "B", "A", "A"] 

    Le programme retournera une erreur, puisque l'on cherchera scores_possibles[6] pour le joueur A
    Or, cette valeur n'existe pas dans le tableau.


Question 6 - Modifier et compléter l'algorithme A afin qu'il affiche la succession des scores, en prenant en compte la notion d’avantage.

    T ← ["A", "B", "B", "A", "A", "A"]
    j1 ← 0
    j2 ← 0
    n ← taille(T)
    scores_possibles ← [0,15,30,40]
    Pour i allant de 0 à n-2 :
        Si T[i] = "A":
            j1 ← j1+1
        Sinon
            j2 ← j2+1
        Fin Si
        Afficher scores_possibles[j1],scores_possibles[j2]
    Fin Pour
    Si scores_possibles[j1] = 40 : 
        Retourner "Joueur A gagnant"
    Sinon
        Retourner "Joueur B gagnant"
    Fin Si
"""
def Tennis(T):

    j1 = 0
    j2 = 0
    n = len(T)
    scores_possibles = [0,15,30,40]
    Egalite = False
    Avantage = "Aucun"

    for i in range (0,n) :
        if T[i] == "A":
            j1 = j1+1
            if j1 <= 3 :
                print(scores_possibles[j1],scores_possibles[j2])

        elif T[i] == "B":
            j2 = j2+1
            if j2 <= 3 :
                print(scores_possibles[j1],scores_possibles[j2])

        if j2 >=3 and j1 >= 3 and j2 == (j1 + 1) :
            print("Avantage Joueur 2 \n")

        elif j2 >=3 and j1 >= 3 and j2 == (j2 + 1) :
            print("Avantage Joueur 1 \n")

        elif j1 == j2 :
            print("Egalité")
        
        if j1 > 3 and (j1 >= j2+2):
            return("Victoire du Joueur 1")
            

        if j2 > 3 and (j2 >= j1+2):
            return("Victoire du Joueur 2")
            
    
print(Tennis(["A","A","A","B","B","B","A","B","B","B"]))
