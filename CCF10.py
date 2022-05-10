def Verif_Mdp(mdp):
    Longueur = False
    Maj = False
    Chiffre = False
    Chaine_Alpha = "AZERTYUIOPQSDFGHJKLMWXCVBN"
    Chaine_Chiffre = "1234567890"

    if len(mdp) > 7 :
        Longueur = True

    for i in range (0,len(mdp)):
        if mdp[i] in Chaine_Alpha :
            Maj = True

    for j in range (0,len(mdp)):
        if mdp[j] in Chaine_Chiffre :
            Chiffre = True

    if Longueur == True and Maj == True and Chiffre == True :
        print(True)
    else :
        print(False)


Verif_Mdp("Salut121")    
