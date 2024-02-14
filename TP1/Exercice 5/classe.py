import random

class De:
    def __init__(self):
        self.valeur = 0

    def lancer(self):
        self.valeur = random.randint(1, 6)

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.points = 0

    def lancer_des(self, des):
        for de in des:
            de.lancer()

    def calculer_points(self, des):
        valeurs = [de.valeur for de in des]

        if valeurs == [4, 2, 1]:
            self.points += 10
        else :
            valeurs.sort()
            if valeurs.count(1) == 2:
                self.points += valeurs[2]
            elif valeurs[0] + 2 == valeurs[1] + 1 == valeurs[2]:
                self.points += 2
                
class Jeu421:
    def __init__(self, joueurs):
        self.joueurs = joueurs

    def jouer_tour(self):
        for joueur in self.joueurs:
            des = [De() for _ in range(3)]  # Crée trois dés pour ce joueur
            joueur.lancer_des(des)
            joueur.calculer_points(des)

    def afficher_points(self):
        for joueur in self.joueurs:
            print(f"Joueur {joueur.nom}: {joueur.points} points")

