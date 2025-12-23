from models.livres import Livre

class Bibliotheque:
    def __init__(self, livres, utilisateurs):
        self.livres = []
        self.utilisateurs = []
        
        for isbn in livres:  
            livre_data = livres[isbn]
            livre_obj = Livre(
                isbn=isbn, 
                titre=livre_data["titre"], 
                auteur=livre_data["auteur"], 
                categorie=livre_data["categorie"], 
                etat_disponibilite=livre_data["etat_disponibilite"]
            )
            self.livres.append(livre_obj)

        for utilisateur in utilisateurs:
            self.utilisateurs.append(utilisateur)

    def get_livres(self):
        return self.livres

    def get_utilisateurs(self):
        return self.utilisateurs

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        
    def supprimer_livre(self, isbn):
        print(livre.isbn for livre in self.livres)
        if isbn not in [livre.isbn for livre in self.livres]:
            print("le livre n'existe pas")
        elif (livre.isbn == isbn and livre.etat_disponibilite == False for livre in self.livres ) :
            print("le livre est actuellement emprunté, vous ne pouvez pas le supprimer")
        else :
            print("possible de supprimer")
            self.livres.pop(isbn) 
            print(f"le livre {isbn} a bien été supprimé")

    