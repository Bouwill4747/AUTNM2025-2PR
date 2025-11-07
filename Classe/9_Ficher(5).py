#Fichier 4

import os


chemin = "C:/Users/Will/PycharmProjects/AUTNM2025-2PR/Classe/Data/"
fichier = "fichier.txt"

# print(chemin + fichier) pour tester que le chemin est correct

f = open(chemin+fichier,"r")

tabLigne = f.readlines()

a = tabLigne[1].split(",")

print(a[2])

f.close()