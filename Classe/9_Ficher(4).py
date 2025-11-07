#Fichier 4

import os


chemin = "C:/Users/Will/PycharmProjects/AUTNM2025-2PR/Classe/Data/"
fichier = "fichier.txt"

# print(chemin + fichier) pour tester que le chemin est correct

f = open(chemin+fichier,"r")
# contenu = f.read()
# print(contenu)
# f.close()

tabLigne = []

while True:
    ligne = f.readline()
    print(ligne)
    if ligne == "":
        break
    tabLigne.append(ligne)

print(tabLigne,"\n")
print(len(tabLigne))

f.close()