from CompteBancaire import CompteBancaire


class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0, taux_interet=0.0):
        # Initialisation des attributs de la classe parente (CompteBancaire)
        super().__init__(titulaire, solde_initial)
        # Taux d'intérêt annuel (ex: 0.05 pour 5%)
        self._taux_interet = taux_interet

    def calculer_interet(self):
        """Calcule et retourne les intérêts générés basés sur le solde actuel et le taux."""
        interet = self.solde * self._taux_interet
        return interet

    def appliquer_interet(self):
        """Optionnel : ajoute les intérêts directement au solde et enregistre l'opération."""
        interet = self.calculer_interet()
        if interet > 0:
            self.deposer(interet)  # Utilise la méthode deposer pour mettre à jour le solde et l'historique
        return interet


if __name__ == "__main__":
    # Test de la classe CompteEpargne
    compte_ep = CompteEpargne("Ali", 1000, 0.05)

    print(compte_ep)
    print("Intérêts calculés :", compte_ep.calculer_interet(), "€")

    # Simulation d'un dépôt d'intérêts
    compte_ep.appliquer_interet()
    print("Nouveau solde après intérêts :", compte_ep.solde, "€")

    # Affichage de l'historique (hérité de CompteBancaire si implémenté)
    if hasattr(compte_ep, "afficher_historique"):
        compte_ep.afficher_historique()