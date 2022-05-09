from tkinter import TRUE

N = 0
N = int(input("Veuillez indiquer N : "))
tableau = []
reponse = False
i = 0

while (i <= N) :
    j = 0
    while (j <= N) :
        if (i^2 + j^2 == N ):
            reponse = True
        else :
            tableau.append(reponse)
        j = j + 1
    i = i + 1
print(reponse)
print(tableau)