from services.bibliotheque import Bibliotheque
from models.livres import Livre
from storage.data import livres, utilisateurs


ma_bibliotheque = Bibliotheque(livres, utilisateurs)

print("Bienvenue dans le système de gestion de la bibliothèque Nisco")
while True:
    print("\n" + "="*50)
    print("MENU PRINCIPAL")
    print("="*50)
    print("1 - Gestion des LIVRES")
    print("2 - Gestion des UTILISATEURS")
    print("3 - Quitter")

    choix_menu = input("\nTapez le numéro de votre choix: ")
    
    # ===== GESTION DES LIVRES =====
    if choix_menu == "1":
        while True:
            print("\n--- Gestion des Livres ---")
            print("1 - Ajouter un livre")
            print("2 - Rechercher un livre")
            print("3 - Supprimer un livre")
            print("4 - Afficher les livres")
            print("5 - Retour au menu principal")

            choix = input("Tapez le numéro de votre choix: ")
            
            if choix == "1":
                isbn = input("Entrez l'ISBN: ")
                titre = input("Entrez le titre: ")
                auteur = input("Entrez l'auteur: ")
                categorie = input("Entrez la catégorie: ")
                etat = input("Le livre est-il disponible? (o/n): ")

                etat = True if etat.lower() == "o" else False
                nouveau_livre = Livre(isbn, titre, auteur, categorie, etat)

                ma_bibliotheque.ajouter_livre(nouveau_livre)
                
            elif choix == "2":
                print("\nRechercher par:")
                print("a - ISBN")
                print("b - Titre")
                print("c - Auteur")
                print("d - Catégorie")
                type_recherche = ""
                while type_recherche not in ["a", "b", "c", "d"]:
                    type_recherche = input("Entrez a, b, c ou d: ").lower()
                
                terme_recherche = input("Entrez le terme de recherche: ")
                resultats = ma_bibliotheque.rechercher_livre(type_recherche, terme_recherche)
                
                if resultats:
                    print("\nRésultats de la recherche:")
                    for livre in resultats:
                        print(f"  {livre}")
                else:
                    print("Aucun résultat trouvé")

            elif choix == "3":
                isbn = input("Entrez l'ISBN du livre à supprimer: ")
                ma_bibliotheque.supprimer_livre(isbn)

            elif choix == "4":
                print("\nQue voulez-vous afficher?")
                print("a - La liste de tous les livres")
                print("b - La liste des livres disponibles")
                print("c - La liste des livres empruntés")
                sous_choix = ""
                while sous_choix not in ["a", "b", "c"]:
                    sous_choix = input("Entrez a, b ou c: ").lower()
                
                print("\nListe des livres:")
                livres_affiche = ma_bibliotheque.afficher_livres_choix(sous_choix)
                if livres_affiche:
                    for livre in livres_affiche:
                        print(f"  {livre}")
                else:
                    print("Aucun livre à afficher")
                    
            elif choix == "5":
                break

    # ===== GESTION DES UTILISATEURS (PARTIE 3) =====
    elif choix_menu == "2":
        while True:
            print("\n--- Gestion des Utilisateurs (PARTIE 3) ---")
            print("1 - Ajouter un utilisateur")
            print("2 - Afficher les informations d'un utilisateur")
            print("3 - Supprimer un utilisateur")
            print("4 - Afficher tous les utilisateurs")
            print("5 - Retour au menu principal")

            choix = input("Tapez le numéro de votre choix: ")
            
            if choix == "1":
                nom = input("Entrez le nom: ")
                prenom = input("Entrez le prénom: ")
                email = input("Entrez l'email: ")
                ma_bibliotheque.ajouter_utilisateur(nom, prenom, email)
                
            elif choix == "2":
                user_id = input("Entrez l'ID de l'utilisateur: ")
                ma_bibliotheque.afficher_utilisateur(user_id)
                
            elif choix == "3":
                user_id = input("Entrez l'ID de l'utilisateur à supprimer: ")
                ma_bibliotheque.supprimer_utilisateur(user_id)
                
            elif choix == "4":
                ma_bibliotheque.afficher_tous_utilisateurs()
                
            elif choix == "5":
                break

    # ===== QUITTER =====
    elif choix_menu == "3":
        print("Au revoir!")
        break
    
    else:
        print("Choix invalide, veuillez réessayer")
