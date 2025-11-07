#Fichier 6
import csv
import os


chemin = "C:/Users/Will/PycharmProjects/AUTNM2025-2PR/Classe/Data/"
fichier = "fichier.txt"

# print(chemin + fichier) pour tester que le chemin est correct
f = open(chemin+fichier,"r")

reader = csv.reader(f, delimiter=",")
matrice = []

for ligne in reader:
    matrice.append(ligne)

# for ligne in reader:
#     print(ligne)

print(matrice[2][1])