N = 0
N = int(input("Veuillez indiquer N : "))
tableau = []
tableaurep = []
reponse = False
i = 0
b = 0


for N in range (101) :
    for i in range(N) :
        j = 0
        for j in range (N) :
            if (i**2 + j**2 == N ):
                print("Combinaison pour",N,":",i**2+j**2)
                reponse = True
            j = j + 1
        i = i + 1
   
    

    if (reponse == False):
        tableaurep.append(N)

    reponse = False
    N = N + 1

print(reponse)
print(tableaurep)
