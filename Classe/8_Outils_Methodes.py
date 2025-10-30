# Varible de classe(commune) vs instance (specifique a chaque objet)

# Methode d'instance : agiseent sur l'instance
# Methode de classe : agissent sur la classe elle meme
# Methode statique : n'agit ni sur la classe ni sur l'instance

class Outils:
    compteur1 = 0
    def __init__(self, c):
        Outils.compteur1 += 1 # incrementer le compteur variable de classe
        self.compteur2 = c # variable d'instance ou attribut

    # Methode d"instance : Agissent sur l'objet (instance self)
    def methode(self):
        print(self.compteur2)

    @classmethod
    def getcompte(self):
        return Outils.compteur1

    @staticmethod # agit ni sur la classe ni sur objet
    def bonjour():
        print("Methode independante...")


o1 = Outils(5)
o2 = Outils(4)
o3 = Outils(7)
o4 = Outils(9)

o3.compteur1 += 1 # modifie pour tous les objets de la classe (variable de classe)
o3.compteur2 += 1 # modifie pour seulement l'objet o3 de la classe (variable instance)

print(o3.getcompte())

o3.getcompte()
Outils.getcompte() # Methode de classe

str.islower("hi") # Methode relié a la classe ()
"hi".islower() # Methode