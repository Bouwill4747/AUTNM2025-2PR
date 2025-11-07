#Fichier 2

import os

# dossier data
# . dossier actuel
# .. dossier parent
# lien absolut

chemin = "C:/Users/Will/PycharmProjects/AUTNM2025-2PR/Classe/dossier/"
fichier = "fichier.txt"

# Utilisation de lien relatif
# os.mkdir("./dossier")

# Utilisation de lien absolu
# print(chemin + fichier) test pour savoir si c compatible et si ca fonctionne

# os.mkdir(chemin)
cheminfichier = chemin + fichier
print(cheminfichier)
open(chemin + fichier, "x")

f.write("M, William, 1999 \n")

