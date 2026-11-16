from datetime import datetime


class CompteBancaire:
    # Compteur de classe pour générer des IDs uniques
    _compteur_id = 1

    def __init__(self, solde_initial=0.0):
        self.id_compte = CompteBancaire._compteur_id
        CompteBancaire._compteur_id += 1

        self.__solde = solde_initial
        self.operations = []  # Liste pour stocker l'historique des opérations

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            # Enregistrement de l'opération avec horodatage
            self.operations.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": "Dépôt",
                "montant": montant
            })

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            # Enregistrement de l'opération avec horodatage
            self.operations.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": "Retrait",
                "montant": montant
            })

    def get_solde(self):
        return self.__solde

    def afficher_releve(self):
        print(f"--- Relevé du Compte n° {self.id_compte} ---")
        if not self.operations:
            print("Aucune opération effectuée.")
        for op in self.operations:
            print(f"  [{op['date']}] {op['type']} : +{op['montant']}€" if op[
                                                                              'type'] == "Dépôt" else f"  [{op['date']}] {op['type']} : -{op['montant']}€")
        print(f"  Solde actuel : {self.__solde}€\n")


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []  # Liste pour lier plusieurs comptes au client

    def ajouter_compte(self, compte):
        self.comptes.append(compte)

    def afficher(self):
        print(f"Client : {self.nom} (Nombre de comptes : {len(self.comptes)})")
        print("=" * 45)
        for compte in self.comptes:
            compte.afficher_releve()


# --- Test du programme ---
cli = Client("Yassir")

# Création de deux comptes pour le même client
compte1 = CompteBancaire(100.0)
compte2 = CompteBancaire(500.0)

# Association des comptes au client
cli.ajouter_compte(compte1)
cli.ajouter_compte(compte2)

# Opérations sur le premier compte
compte1.deposer(300)
compte1.retirer(50)

# Opérations sur le deuxième compte
compte2.retirer(120)

# Affichage des informations et des relevés
cli.afficher()