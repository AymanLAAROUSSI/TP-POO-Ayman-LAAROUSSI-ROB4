from classe import * 
import unittest
from classe import Carte, TasDeCartes, Joueur, Jeu

class TestCarte(unittest.TestCase):
    def test_creation_carte(self):
        carte = Carte("coeur", 10)
        self.assertEqual(carte.couleur, "coeur")
        self.assertEqual(carte.valeur, 10)

    def test_affichage_carte(self):
        carte = Carte("carreau", 14)
        self.assertEqual(str(carte), "As de carreau")

class TestTasDeCartes(unittest.TestCase):
    def setUp(self):
        self.tas = TasDeCartes()

    def test_ajout_cartes(self):
        self.tas.ajouter_cartes(Carte("pique", 8))
        self.assertEqual(len(self.tas.tas), 1)

    def test_melanger(self):
        self.tas.melanger()

    def test_retirer_premiere_carte(self):
        carte = Carte("coeur", 9)
        self.tas.ajouter_cartes(carte)
        self.assertEqual(self.tas.retirer_premiere_carte(), carte)

class TestJoueur(unittest.TestCase):
    def setUp(self):
        self.joueur = Joueur("Testeur")

    def test_piocher(self):
        carte = Carte("coeur", 10)  
        self.joueur.pioche.ajouter_cartes(carte)  
        self.assertEqual(len(self.joueur.pioche.tas), 1)
        carte_piochee = self.joueur.piocher()
        self.assertIsInstance(carte_piochee, Carte)
        self.assertEqual(len(self.joueur.pioche.tas), 0)

    def test_perdu(self):
        self.assertTrue(self.joueur.perdu())


class TestJeu(unittest.TestCase):
    def setUp(self):
        self.joueur1 = Joueur("Joueur 1")
        self.joueur2 = Joueur("Joueur 2")

        self.jeu = Jeu(self.joueur1, self.joueur2)

    def test_distribution(self):
        self.jeu.distribution()

        nb_cartes_joueur1 = len(self.joueur1.pioche.tas)
        nb_cartes_joueur2 = len(self.joueur2.pioche.tas)
        self.assertEqual(nb_cartes_joueur1, nb_cartes_joueur2)

        nb_cartes_total = nb_cartes_joueur1 + nb_cartes_joueur2
        self.assertEqual(nb_cartes_total, 52)

    def test_jouer_tour(self):
        cartes_joueur1 = [Carte("coeur", 10), Carte("carreau", 8), Carte("trefle", 14)]
        cartes_joueur2 = [Carte("pique", 9), Carte("carreau", 11), Carte("coeur", 12)]

        self.joueur1.pioche.ajouter_cartes(cartes_joueur1)
        self.joueur2.pioche.ajouter_cartes(cartes_joueur2)

        self.jeu.jouer_tour()
        self.assertEqual(len(self.joueur1.pioche.tas)+len(self.joueur1.defausse.tas), 4)
        self.assertEqual(len(self.joueur2.pioche.tas)+len(self.joueur2.defausse.tas), 2)

    def test_bataille(self):
        cartes_joueur1 = [Carte("coeur", 10), Carte("carreau", 8), Carte("trefle", 14)]
        cartes_joueur2 = [Carte("pique", 9), Carte("carreau", 11), Carte("coeur", 12)]

        self.joueur1.pioche.ajouter_cartes(cartes_joueur1)
        self.joueur2.pioche.ajouter_cartes(cartes_joueur2)

        self.jeu.bataille([], [])
        self.assertEqual(len(self.joueur1.pioche.tas)+len(self.joueur1.defausse.tas), 1)
        self.assertEqual(len(self.joueur2.pioche.tas)+len(self.joueur2.defausse.tas), 5)

def main():
    print("Tapez 1 pour les test unitaires")
    print("Tapez 2 pour lancer une partie")
    choix = input("Entrez votre choix : ")
    if choix == "1":
        unittest.main(verbosity=2)
    elif choix == "2":
        joueur1 = Joueur("Joueur 1")
        joueur2 = Joueur("Joueur 2")

        jeu_bataille = Jeu(joueur1, joueur2)
        jeu_bataille.jouer()
    else:
        print("Choix invalide. Veuillez taper 1 ou 2.")

if __name__ == "__main__": 
    main()
