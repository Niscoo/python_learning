from models.livres import Livre
from models.utilisateurs import Utilisateur

class Bibliotheque:
    def __init__(self, livres, utilisateurs):
        self.livres = {}
        self.utilisateurs = {}
        self.next_user_id = 1
        
        for isbn in livres:  
            livre_data = livres[isbn]
            livre_obj = Livre(
                isbn=isbn, 
                titre=livre_data["titre"], 
                auteur=livre_data["auteur"], 
                categorie=livre_data["categorie"], 
                etat_disponibilite=livre_data["etat_disponibilite"]
            )
            self.livres[isbn] = livre_obj

        for user_id in utilisateurs:
            user_data = utilisateurs[user_id]
            utilisateur_obj = Utilisateur(
                identifiant=user_id,
                nom=user_data["nom"],
                prenom=user_data["prenom"],
                email=user_data["email"],
                livres_empruntes=user_data["livres_empruntes"]
            )
            self.utilisateurs[user_id] = utilisateur_obj
            # Extract numeric part to track next ID
            if user_id.startswith("U"):
                try:
                    num = int(user_id[1:])
                    if num >= self.next_user_id:
                        self.next_user_id = num + 1
                except ValueError:
                    pass

    def get_livres(self):
        return self.livres

    def afficher_livres_choix(self, choix):
        if choix == "a":
            return self.livres.values()
        elif choix == "b":
            return [livre for livre in self.livres.values() if livre.etat_disponibilite]
        elif choix == "c":
            return [livre for livre in self.livres.values() if not livre.etat_disponibilite]
        else:
            print("Choix invalide")
            return []

    def get_utilisateurs(self):
        return self.utilisateurs

    def ajouter_livre(self, livre):
        self.livres[livre.isbn] = livre
        
    def supprimer_livre(self, isbn):
        if isbn not in self.livres:
            print("Le livre n'existe pas")
        elif not self.livres[isbn].etat_disponibilite:
            print("suppression impossible, le livre est emprunté")
        else:
            self.livres.pop(isbn)
            print("Le livre a bien été supprimé")


    def rechercher_livre(self, type_recherche, terme_recherche): 
        resultats = []
        for livre in self.livres.values():
            if type_recherche == "a" and livre.isbn == terme_recherche:
                resultats.append(livre)
            elif type_recherche == "b" and terme_recherche.lower() in livre.titre.lower():
                resultats.append(livre)
            elif type_recherche == "c" and terme_recherche.lower() in livre.auteur.lower():
                resultats.append(livre)
            elif type_recherche == "d" and terme_recherche.lower() in livre.categorie.lower():
                resultats.append(livre)
        return resultats

    # PARTIE 3 - GESTION DES UTILISATEURS
    def ajouter_utilisateur(self, nom, prenom, email):
        """Ajoute un nouvel utilisateur avec un ID auto-généré."""
        user_id = f"U{str(self.next_user_id).zfill(3)}"
        self.next_user_id += 1
        
        utilisateur = Utilisateur(
            identifiant=user_id,
            nom=nom,
            prenom=prenom,
            email=email,
            livres_empruntes=[]
        )
        self.utilisateurs[user_id] = utilisateur
        print(f"✓ Utilisateur '{prenom} {nom}' ajouté avec l'ID: {user_id}")
        return user_id

    def supprimer_utilisateur(self, user_id):
        """Supprime un utilisateur si aucun emprunt actif."""
        if user_id not in self.utilisateurs:
            print(f"✗ Utilisateur {user_id} introuvable")
            return False
        
        utilisateur = self.utilisateurs[user_id]
        if utilisateur.livres_empruntes:
            print(f"✗ Suppression impossible: {utilisateur.prenom} {utilisateur.nom} a {len(utilisateur.livres_empruntes)} livre(s) en cours d'emprunt")
            return False
        
        nom_complet = f"{utilisateur.prenom} {utilisateur.nom}"
        del self.utilisateurs[user_id]
        print(f"✓ Utilisateur '{nom_complet}' supprimé avec succès")
        return True

    def afficher_utilisateur(self, user_id):
        """Affiche les infos d'un utilisateur avec ses livres empruntés."""
        if user_id not in self.utilisateurs:
            print(f"✗ Utilisateur {user_id} introuvable")
            return
        
        utilisateur = self.utilisateurs[user_id]
        print(f"\n{'='*50}")
        print(f"Informations de l'utilisateur: {utilisateur}")
        print(f"{'='*50}")
        print(f"Email: {utilisateur.email}")
        
        if utilisateur.livres_empruntes:
            print(f"\nLivres actuellement empruntés ({len(utilisateur.livres_empruntes)}):")
            for isbn in utilisateur.livres_empruntes:
                if isbn in self.livres:
                    print(f"  • {self.livres[isbn]}")
        else:
            print("\nAucun livre actuellement emprunté")
        
        print(f"{'='*50}\n")

    def afficher_tous_utilisateurs(self):
        """Affiche la liste de tous les utilisateurs."""
        if not self.utilisateurs:
            print("Aucun utilisateur enregistré")
            return
        
        print(f"\n{'='*50}")
        print("Liste de tous les utilisateurs:")
        print(f"{'='*50}")
        for user_id, utilisateur in self.utilisateurs.items():
            print(f"{user_id}: {utilisateur}")
        print(f"{'='*50}\n")