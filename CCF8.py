"""

Question 1 : 

    i   phrase[i]   ord(phrase[i])  ord(phrase[i]=32)   c

    /       /              /                /           0
    0
    1       a             97             False          0
    2       y             121            False          0
    3                     32             True           1
    4       b             98             False          1
    5                     32             True           2
    6       a             97             False          2


Question 2 :

    mystere("Bonne journée à tous") retournera 3
    Pour compter le nombre de mots dans la phrase, il faut ajouter 1 à la variable c.


Question 3 :

    Fonction majuscule(lettre)

        Debut
            code ← ord(lettre) 
            Si ord(lettre) > 96 et ord(lettre) < 123
                Retourner (chr(code+32))
            Sinon 
                Retourner(lettre)
            Fin Si
        Fin

"""

def Phrase(phrase_depart):
    phrase_arrivée = ""
    for elt in (phrase_depart):
        code = ord(elt)
        if code > 96 and code < 123 :
            phrase_arrivée += chr(code-32)
        else :
            phrase_arrivée += elt 
    return(phrase_arrivée)

print(Phrase("texte"))
