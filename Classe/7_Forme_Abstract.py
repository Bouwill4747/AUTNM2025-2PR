import math
# Mettre en évidence le polymorphisme / heritage

class Forme:
    def __init__(self, couleur, nom):
        self.couleur = couleur
        self.nom = nom

    def __str__(self):
        return f"Forme {self.couleur} {self.nom}"

class Cercle(Forme):
    def __init__(self, Forme, rayon):
        super().__init__(Forme.couleur, Forme.nom)
        self.rayon = rayon

    def __str__(self):
        return f"Cercle {self.rayon} {self.couleur} {self.nom}"

    def calPerimetre(self):
        return f"Périmetre = {2 * math.pi * self.rayon}"

    def calSurface(self):
        return math.pi * (self.rayon ** 2)

class Rectangle(Forme):
    def __init__(self, Forme, longeur, largeur):
        super().__init__(Forme.couleur, Forme.nom)
        self.longeur = longeur
        self.largeur = largeur

    def __str__(self):
        return f"Rectangle {self.longeur} {self.largeur} {self.couleur} {self.nom}"

    def calPerimetre(self):
        return f"Perimetre = {(self.largeur * 2) + (self.longeur *2 )}"

    def calSurface(self):
        return self.largeur * self.longeur

forme1 = Cercle(Forme("Rouge","Bob"), 5)
forme2 = Rectangle(Forme("Bleu", "Alice"), 5, 10)
forme3 = Cercle(Forme("Vert","Gabe"), 3)
forme4 = Rectangle(Forme("Jaune", "Will"), 4, 8)
forme5 = Cercle(Forme("Rose","Val"), 6)
forme6 = Rectangle(Forme("Mauve", "Éric"), 7, 14)

liste = [forme1, forme2, forme3, forme4, forme5, forme6]
a = 0

for x in liste:
    a += x.calSurface()

class FenetreGraphique():
    def __init__(self, liste):
        self.liste = liste

print(f"Totale de tout les surface de les formes = {a}")
print("\n")
print(forme1)
print(forme1.calPerimetre())
print(forme1.calSurface())
print("\n")
print(forme2)
print(forme2.calPerimetre())
print(forme2.calSurface())

