import math
from classe import Vecteur

def main():
    v1 = Vecteur(1, 2, 3)
    v2 = Vecteur(4, 5, 6)
    

    v3 = v1.additionner(v2)
    print("Addition :", end=" ")
    v3.afficher()

    print("Norme de v1 :", v1.calculer_norme())

    produit_scalaire = v1.calculer_produit_scalaire(v2)
    print("Produit scalaire :", produit_scalaire)

    v4 = v1.tourner(math.pi / 2)
    print("Rotation de v1 :", end=" ")
    v4.afficher()


if __name__ == "__main__": 
    main()
