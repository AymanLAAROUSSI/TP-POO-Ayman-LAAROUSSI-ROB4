import sys
from classe import Algebre

def main():
    if len(sys.argv) < 2:
        print("Veuillez fournir au moins un argument.")
        sys.exit(1)

    command = sys.argv[1]

    if command == "somme":
        if len(sys.argv) < 3:
            print("Veuillez fournir un nombre entier n.")
            sys.exit(1)
        n = int(sys.argv[2])
        algebre = Algebre(n)
        print("Somme des premiers", n, "entiers:", algebre.somme_premiers_entiers())
    elif command == "factorielle":
        if len(sys.argv) < 3:
            print("Veuillez fournir un nombre entier n.")
            sys.exit(1)
        n = int(sys.argv[2])
        algebre = Algebre(n)
        print("Factorielle de", n, ":", algebre.factorielle())
    else:
        print("Commande non reconnue.")


if __name__ == "__main__": 
    main()

