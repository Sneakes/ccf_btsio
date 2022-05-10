import math
nb=17
# derniere question
for a in range (1,nb):
    for b in range (1,nb):
        if(float(math.sqrt(a*a+b*b)).is_integer()):
            c=a**2+b**2
            print(a,b,math.sqrt(c))
# 3 question
for a in range (1,nb):
    for b in range (1,nb):
        for c in range (1,nb):
            if a<b<c:
                print(a,b,c)
n=0
for a in range (1,nb):
    for b in range (1,nb):
        for c in range (1,nb):
            if a<b<c:
                n=n+1
                print(n)
