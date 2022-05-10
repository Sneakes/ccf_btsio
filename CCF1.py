tablo = []

for i in range (7):
    note=int(input('saisir')) 
    tablo.append(note)

coefficient = [3,3,2,2,1,2,1]
longtab = len(tablo) + len(coefficient)

moyennenondiv = tablo[0] * coefficient[0] + tablo[1] * coefficient[1] + tablo[2] * coefficient[2] + tablo[3] * coefficient[3] + tablo[4] * coefficient[4] +tablo[5] * coefficient[5] + tablo[6] * coefficient[6] 

moyenne = moyennenondiv / longtab

print("Vous avez" ,moyenne, "de moyenne")


if (moyenne >= 16 ) :
    print("Mention : Très Bien")
elif (moyenne >= 14) :
    print("Mention : Bien")
elif (moyenne >= 12) :
    print("Mention : Assez Bien")
elif (moyenne >= 10) :
    print("Mention : Passable")
else :
    print("Vous n'avez pas été reçu")
