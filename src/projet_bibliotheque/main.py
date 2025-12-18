from services.bibliotheque import Bibliotheque
from models.livres import Livre
from storage.data import livres, utilisateurs


ma_bibliotheque = Bibliotheque(livres, utilisateurs)

print("Bienvenue dans le système de gestion de la bibliothèque Nisco")
print("1 - Ajouter un livre")
print("2 - supprimer un livre")

choix = input ("Tapez le numéro de votre choix")
if choix == "1" :
    isbn = input("entrez isbn")
    titre = input("entrez titre")
    auteur = input("entrez auteur")
    categorie = input("entrez la catégorie")
    etat = input("le livre est il disponible? o pour oui n pour non")

    etat == True if etat == "o" else False
    nouveau_livre = Livre(isbn, titre, auteur, categorie, etat)

    ma_bibliotheque.ajouter_livre(nouveau_livre)
    mes_livres = ma_bibliotheque.get_livres()
    print("\nListe des livres après ajout :")
    for livre in mes_livres:
        print(livre)