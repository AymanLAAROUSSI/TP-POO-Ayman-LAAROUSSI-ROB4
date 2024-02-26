import numpy as np
import random as rd

# ---------- Carte ----------

class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def __str__(self):
        valeurs_speciales = {11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As'}
        if self.valeur in valeurs_speciales:
            valeur = valeurs_speciales[self.valeur]
        else:
            valeur = str(self.valeur)
        return f"{valeur} de {self.couleur}"


# ---------- Tas de cartes ----------

class TasDeCartes:
    def __init__(self):
        self.tas = []

    def melanger(self): 
        rd.shuffle(self.tas)

    def ajouter_cartes(self, cartes): 
        if isinstance(cartes, list):
            self.tas.extend(cartes)
        else:
            self.tas.append(cartes)

    def retirer_premiere_carte(self): 
        if self.tas:
            return self.tas.pop(0)
        else:
            raise IndexError("Le tas est vide")

    def est_vide(self):
        return len(self.tas) == 0

# ---------- Joueur ----------

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.pioche = TasDeCartes()
        self.defausse = TasDeCartes()

    def piocher(self):
        if self.pioche.est_vide(): 
            self.reconstituer_pioche()
        return self.pioche.retirer_premiere_carte()

    def reconstituer_pioche(self):
        self.pioche.ajouter_cartes(self.defausse.tas)
        self.pioche.melanger()
        self.defausse.tas = []

    def perdu(self):
        return self.pioche.est_vide() and self.defausse.est_vide()

# ---------- Jeu ----------

class Jeu:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2

    def distribution(self):
        couleurs_possible = {"carreaux", "pique", "trefle", "coeur"}
        valeurs_possible = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14} # 14 : As, 11 : Valet, 12 : Dame, 13: Roi

        toutes_les_cartes = TasDeCartes()

        for valeur in valeurs_possible:
            for couleur in couleurs_possible:
                toutes_les_cartes.ajouter_cartes(Carte(couleur, valeur))

        toutes_les_cartes.melanger()

        moitie = len(toutes_les_cartes.tas) // 2
        self.joueur1.pioche.ajouter_cartes(toutes_les_cartes.tas[:moitie])
        self.joueur2.pioche.ajouter_cartes(toutes_les_cartes.tas[moitie:])

    def jouer_tour(self):
        print("-------------- DEBUT D'UN TOUR --------------")
        carte_joueur1 = self.joueur1.piocher()
        carte_joueur2 = self.joueur2.piocher()

        if carte_joueur1 is None or carte_joueur2 is None:
            return
        print("--- CA JOUE : ")
        print(f"    {self.joueur1.nom} joue {carte_joueur1}")
        print(f"    {self.joueur2.nom} joue {carte_joueur2}")

        if carte_joueur1.valeur > carte_joueur2.valeur:
            print(f"\n    {self.joueur1.nom} gagne ce tour !")
            self.joueur1.defausse.ajouter_cartes(carte_joueur1)
            self.joueur1.defausse.ajouter_cartes(carte_joueur2)
        elif carte_joueur1.valeur < carte_joueur2.valeur:
            print(f"\n    {self.joueur2.nom} gagne ce tour !")
            self.joueur2.defausse.ajouter_cartes(carte_joueur1)
            self.joueur2.defausse.ajouter_cartes(carte_joueur2)
        else:
            print("Égalité ! Bataille !")
            self.bataille([carte_joueur1], [carte_joueur2])

        print("--- L'HEURE DES COMPTES : ")
        print(f"    {self.joueur1.nom} a {len(self.joueur1.pioche.tas)+len(self.joueur1.defausse.tas)} cartes.")
        print(f"    {self.joueur2.nom} a {len(self.joueur2.pioche.tas)+len(self.joueur2.defausse.tas)} cartes.")
        print("")

    def bataille(self, cartes_joueur1, cartes_joueur2):
        if (len(self.joueur1.pioche.tas)+len(self.joueur1.defausse.tas))<3 :
            print(f"{self.joueur1.nom} n'a pas assez de cartes pour poursuivre la bataille !")
            return
        if (len(self.joueur2.pioche.tas)+len(self.joueur2.defausse.tas))<3 :
            print(f"{self.joueur2.nom} n'a pas assez de cartes pour poursuivre la bataille !")
            return

        cartes_joueur1.append(self.joueur1.piocher())
        cartes_joueur2.append(self.joueur2.piocher())

        carte_joueur1_visible = self.joueur1.piocher()
        carte_joueur2_visible = self.joueur2.piocher()

        cartes_joueur1.append(carte_joueur1_visible)
        cartes_joueur2.append(carte_joueur2_visible)

        print(f"    {self.joueur1.nom} pose {cartes_joueur1[1]} et joue {carte_joueur1_visible}")
        print(f"    {self.joueur2.nom} pose {cartes_joueur2[1]} et joue {carte_joueur2_visible}")

        if carte_joueur1_visible.valeur > carte_joueur2_visible.valeur:
            print(f"{self.joueur1.nom} remporte la bataille !")
            self.joueur1.defausse.ajouter_cartes(cartes_joueur1)
            self.joueur1.defausse.ajouter_cartes(cartes_joueur2)
        elif carte_joueur1_visible.valeur < carte_joueur2_visible.valeur:
            print(f"{self.joueur2.nom} remporte la bataille !")
            self.joueur2.defausse.ajouter_cartes(cartes_joueur1)
            self.joueur2.defausse.ajouter_cartes(cartes_joueur2)
        else:
            print("Égalité ! Nouvelle bataille !")
            self.bataille(cartes_joueur1, cartes_joueur2)

    def jouer(self):
        self.distribution()
        while not self.joueur1.perdu() and not self.joueur2.perdu():
            self.jouer_tour()
        if (len(self.joueur1.pioche.tas)+len(self.joueur1.defausse.tas))<(len(self.joueur2.pioche.tas)+len(self.joueur2.defausse.tas)) :
            print(f"{self.joueur2.nom} a gagné la partie !")
        else:
            print(f"{self.joueur1.nom} a gagné la partie !")