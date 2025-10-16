# Utilisation des classes : créer des objets

from Personne import Personne
from Personne import Etudiant, Professeur

p1 = Personne("Bourb", "Will", "will_b@gmail.com")
p2 = Personne("Babri", "Raouf", "raouf@gmail.com")

e1 = Etudiant(p1, "175", "Cybersécurité")

pf1 = Professeur(p1, "25", "Math")

print(p1)
print(p2)
print(e1)
print(pf1)

# Le poly morhpisme : plusieurs formes : comprtement similaire pour des objets de type différent
# a condition que ces objet partagent un parent commun

# moi en tant que personne et un écran somme des objetsPhysique
# attributs communs: coordonnées, poids,
# comportement commun :  deplacer, rotate,

# Methode polymorphe : a le meme nom que chez le parent et l'enfant
# mais :: le code est different d'une methode a l'autre

liste = [p1, p2, e1, pf1]

# compêrtement similaire
for x in liste:
    print(x.redigerMail())