#Fichier 2

import os

# dossier data
# . dossier actuel
# .. dossier parent
# lien absolut

chemin = "C:/Users/Will/PycharmProjects/AUTNM2025-2PR/Classe/dossier/"
fichier = "fichier.txt"

# Utlilisation de lien relatif
os.mkdir("../../../dossierTest")

# Utilisation de lien absolut
os.mkdir("C:/dossierTest")

