from models.livres import Livre

class Bibliotheque:
    def __init__(self, livres, utilisateurs):
        self.livres = {}
        self.utilisateurs = {}
        
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

        # for utilisateur in utilisateurs:
        #     return

    def get_livres(self):
        return self.livres

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


