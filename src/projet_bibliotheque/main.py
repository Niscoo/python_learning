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
    
        
        
    if choix == "2":
        isbn = input("entrez isbn")
        ma_bibliotheque.supprimer_livre(isbn)

    if choix == "3":
        mes_livres = ma_bibliotheque.get_livres()
        print("\nLa liste des livres :")
        for livre in mes_livres:
            print(livre)
        