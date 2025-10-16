# Heritage : fabrique une nouvelle classe a partir de la class existante
# Class parent vs class enfant
# class enfant = classe parent  nouveau attributs et/ou nouvelle méthodes

# exemple : DATA / FAIRE
# Personne : nom, prenom, email / setNom() / envUnMail()
# Etudiant : Personne + numeroDA + Programme / sinscrireProgramme()
# Professeur : Personne + numeroEmployer + Departement / setDepartement()

# Un etudiant "est une" Personne = lien d'héritage

class Personne:
    def __init__(self, nom, prenom, mail): # Constructeur du Parent
        self.nom = nom
        self.prenom = prenom
        self.mail = mail

    def __str__(self):
        return "Personne : " + self.nom + "  " + self.prenom + "  " + self.mail

    def redigerMail(self):
        return "Personne " + self.prenom + ".... corps du mail"

class Etudiant(Personne):
    def __init__(self, personne, numDA, programme): # Constructeur de l'enfant
        super().__init__(personne.nom, personne.prenom, personne.mail) # Appel au contruscteur du parent PERSONNE
        self.numDA = numDA
        self.programme = programme

    def __str__(self):
        return "Etudiant : " + self.nom + "  " + self.prenom + "  " + self.mail + "  " + self.numDA + "  " + self.programme

    def redigerMail(self):
        return "Etudiant " + self.prenom + "...." + self.numDA + "....suite du mail"

class Professeur(Personne):
    def __init__(self, personne, numEmployer, departement):
        super().__init__(personne.nom, personne.prenom, personne.mail)
        self.numEmployer = numEmployer
        self.departement = departement

    def __str__(self):
        return "Professeur : " + self.nom + "  " + self.prenom + "  " + self.mail + "  " + self.numEmployer + "  " + self.departement

    def redigerMail(self):
        return "Professeur " + self.prenom + "...... du departenent " + self.departement

