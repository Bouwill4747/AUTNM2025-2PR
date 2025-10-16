# déclaration de la classe
# le nom de la classe commmence avec une maj
# les attributs marque, modele, annee commence avec min
# Objectif: Regrouper de la data
class Voiture:
    marque = ""
    modele = ""
    année = ""

# instantiation/création de l'objet dans la mémoire
v1 = Voiture()
v1.marque = "Volvo"
v1.modele = "X4"
v1.année = 2020

v2 = Voiture()

print(v1)
print(type(v1))