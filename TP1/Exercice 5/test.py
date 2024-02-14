from classe import * 

def main():
    joueurs = [Joueur("Joueur A"), Joueur("Joueur B")]

    jeu = Jeu421(joueurs)
    for i in range(3):  #3 tours 
        jeu.jouer_tour()
        print(f"Tour {i} :")
        jeu.afficher_points()

    print("Resultats : ")
    jeu.afficher_points()

if __name__ == "__main__": 
    main()

