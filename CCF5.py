'''
Temp float
M float
i int

temp = 6, 24.5, 28, 25, 32, 34.5, 31
M = 6, 24.5, 28, 28, 32, 34.5, 34.5
i = 

Cet algorithme permet de garder la température la plus haute
'''
'''
N = int(input("Nombre de jours : "))
Temp = float(input("Saisir une température : "))
M = Temp
B = Temp
jca = 0

for i in range (N - 1) :
    Temp = float(input("Saisir une température : "))
    if (Temp > M) : 
        M = Temp
    if (Temp < B) :
        B = Temp
    if (Temp > 38) :
        jca = jca + 1

print ("Température Max : ",M)
print ("Température Min : ",B)
print ("Nombre de jour de canicule : ",jca)
'''

N = int(input("Nombre de jours : "))
Temp = [25,34,38.5,39,32,34,40,33]
M = Temp[0]
B = Temp[0]
jca = 0

for i in range (N - 1) :
    
    if (Temp[i+1] > M) : 
        M = Temp[i+1]
    if (Temp[i+1] < B) :
        B = Temp[i+1]
    if (Temp[i+1] > 38) :
        jca = jca + 1
    i = i + 1

print ("Température Max : ",M)
print ("Température Min : ",B)
print ("Nombre de jour de canicule : ",jca)
