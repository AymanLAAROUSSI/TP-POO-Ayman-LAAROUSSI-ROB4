import math
from classe import * 

def main():
    v1 = Vecteur(1, 2, 3)
    v2 = Vecteur(4, 5, 6)
    v3 = Vecteur(7, 8, 9)

    triangle = Triangle(v1, v2, v3)

    print("Coordonnées initiales du triangle:")
    triangle.afficher()

    triangle.tourner(math.pi / 2)
    print("\nCoordonnées du triangle après rotation de 90 degrés:")
    triangle.afficher()

    translation = Vecteur(1, 1, 1)
    triangle.deplacer(translation)
    print("\nCoordonnées du triangle après translation:")
    triangle.afficher()

if __name__ == "__main__": 
    main()

