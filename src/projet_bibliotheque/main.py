from services.bibliotheque import Bibliotheque
from models.livres import Livre
from storage.data import livres, utilisateurs


ma_bibliotheque = Bibliotheque(livres, utilisateurs)

while True:
    print("Bienvenue dans le système de gestion de la bibliothèque Nisco")
    print("1 - Ajouter un livre")
    print("2 - supprimer un livre")
    print("3 - afficher la liste des livres")

    choix = input ("Tapez le numéro de votre choix")
    
    if choix == "1" :
        isbn = input("entrez isbn")
        titre = input("entrez titre")
        auteur = input("entrez auteur")
        categorie = input("entrez la catégorie")
        etat = input("le livre est il disponible actuellement? o pour oui n pour non")

        etat == True if etat == "o" else False
        nouveau_livre = Livre(isbn, titre, auteur, categorie, etat)

        ma_bibliotheque.ajouter_livre(nouveau_livre)
        
    if choix == "2":
        isbn = input("Entrez isbn")
        ma_bibliotheque.supprimer_livre(isbn)

    if choix == "3":
        # mes_livres = [Livre]
        # mes_livres.append(livre for livre in ma_bibliotheque.get_livres())
        print("\nLa liste des livres :")
        print(livre for livre in ma_bibliotheque.get_livres())
        