class Utilisateur:
    def __init__(self, identifiant, nom, prenom, email, livres_empruntes):
        self.identifiant = identifiant
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.livres_empruntes = livres_empruntes

    def __str__(self):
        return (
            f"- {self.prenom} {self.nom} "
            f"(ID: {self.identifiant}, "
            f"Livres empruntés: {len(self.livres_empruntes)})"
        )

    def emprunter_livre(self, isbn):
        if isbn not in self.livres_empruntes:
            self.livres_empruntes.append(isbn)
            print(f"Le livre {isbn} a été emprunté par {self.prenom} {self.nom}.")
        else:
            print(f"{self.prenom} {self.nom} a déjà emprunté le livre {isbn}.")

    def retourner_livre(self, isbn):
        if isbn in self.livres_empruntes:
            self.livres_empruntes.remove(isbn)
            print(f"Le livre {isbn} a été retourné par {self.prenom} {self.nom}.")
        else:
            print(f"{self.prenom} {self.nom} n'a pas emprunté le livre {isbn}.")