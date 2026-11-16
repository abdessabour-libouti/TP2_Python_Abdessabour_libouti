class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial
        # Initialisation de la liste des opérations : chaque élément sera (montant, type)
        # Type : 1 pour dépôt, 0 pour retrait
        self._operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            # Ajout de l'opération dans l'historique : (montant, 1 pour dépôt)
            self._operations.append((montant, 1))
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            # Ajout de l'opération dans l'historique : (montant, 0 pour retrait)
            self._operations.append((montant, 0))
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        return self.__solde

    def __setattr__(self, nom, valeur):
        """Intercepte toute modification d'attribut pour protéger le solde."""
        # Empêche de modifier directement l'attribut privé du solde ou la propriété solde de l'extérieur
        if nom == "solde":
            raise AttributeError("Modification directe interdite ! Utilisez les méthodes deposer() ou retirer().")

        # Pour les autres attributs, on autorise l'affectation normale via super()
        super().__setattr__(nom, valeur)
    def afficher_historique(self):
        """Affiche l'historique des opérations sous forme de tableau ou de liste claire."""
        print(f"\n--- Historique des opérations pour {self._titulaire} ---")
        if not self._operations:
            print("Aucune opération effectuée.")
            return

        for index, (montant, type_op) in enumerate(self._operations, 1):
            libelle = "Dépôt" if type_op == 1 else "Retrait"
            print(f"Opération {index} : [{libelle}] - Montant : {montant} € (Code binaire : {type_op})")

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"


if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)
    compte.deposer(200)
    compte.retirer(150)

    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    # Affichage de l'historique des opérations
    compte.afficher_historique()

    # Ceci va déclencher une erreur (AttributeError) et bloquer la modification directe :
    try:
        compte.solde = 500
    except AttributeError as e:
        print("Erreur attrapée :", e)