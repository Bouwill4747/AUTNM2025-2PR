# Document (nom, auteur, numero de pages)
class Document():
    pass



# Livres (ISBN, annee)
class Livre(Document):
    # Constructeur du livre
    pass



# Adhérant (nom , prenom, id)
# indentifiant unique...

class Adgerent():
    pass



# Emprunt (livre, adherent) metre identifiant du livre avec l'identifiant de l'adherent
class Emprunt():
    pass



# Bibliotheque :
# Liste de livre
# Liste d'aherents
# Liste d'emprunts
class Bibliotheque():
    pass



# Classe Menu
class Menu:
    pass


def afficherMenu():
    print("----------------------- Menu ----------------------------")
    print("---------------------------------------------------------")
    print("1 pour Ajouter un livre      ----------------------------")
    print("C pour continuer      -----------------------------------")
    print("Q pour quitter        -----------------------------------")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")



# Main

condition = True

while(condition):
    afficherMenu()
    reponse = input("Réponse : ")
    reponse = reponse.lower()
    if (reponse == "c"):
        condition = True
    elif (reponse == "q"):
        condition = False
    elif (reponse == "1"):
        # Code pour ajouter un livre
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        ISBN = input("ISBN : ")
        pass
    else:
        print("Seulement C et Q sont acceptés")
        condition = True