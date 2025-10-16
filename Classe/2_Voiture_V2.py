# Constructeur
# Objectif: Encapsuler de la data
# Objectif : Ajouter du control au data et avoir de la cohérance
class Voiture:
    def __init__(self, p_marque, p_modele, p_annee, p_km): # constructeur : Méthode qui retourne un objet
        self.marque = p_marque
        self.modele = p_modele
        self.annee = p_annee # attribut publique
        self.__km = p_km # attribut proteced

    def __str__(self):
        return "((" + self.marque + "))"

    def get_km(self):
        return self.__km

    def set_km(self, km):
        if(km < 0):
            print("Erreur de km")
        elif (km < self.__km):
            print("Erreur : Km inferieur au km enregistrer")
        else:
            self.__km = km

# instantiation/création de l'objet dans la mémoire
v1 = Voiture("Volvo", "C90", 2020, 150000)

v1.set_km(2500)
v1.set_km(-2500)
v1.set_km(200000)

print(v1.get_km())
print(v1.__str__())