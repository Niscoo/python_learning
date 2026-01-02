import datetime as dt

class Livre:
    def __init__(self, isbn, titre, auteur, categorie, etat_disponibilite):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.etat_disponibilite = etat_disponibilite

    def __str__(self):
        return f"- {self.titre} écrit par {self.auteur} (ISBN: {self.isbn}) etat: {self.etat_disponibilite}"