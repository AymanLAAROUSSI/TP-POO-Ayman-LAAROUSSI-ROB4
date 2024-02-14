import math
from classe import * 

def main():
    joueurs = [Joueur("Alice"), Joueur("Bob")]

    jeu = Jeu421(joueurs)
    for _ in range(3): 
        jeu.jouer_tour()

    jeu.afficher_points()

if __name__ == "__main__": 
    main()