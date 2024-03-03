from classe import *

import unittest

class TestMesMedias(unittest.TestCase):
    def setUp(self):
        self.MesMedias = MesMedias()
        self.livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", "1954", 1178, "Houghton Mifflin")
        self.cd = CD("Thriller", "Michael Jackson", "1982", "42 minutes", 9)
        self.dvd = DVD("Inception", "Christopher Nolan", "2010", "148 minutes")
        self.article = ArticleMag("Les bienfaits d'une alimentation équilibrée", "François Dupont", "2023", "Santé Magazine", "153", "19-22")

    def test_ajouter_media(self):
        self.MesMedias.ajouter_media(self.livre)
        self.assertEqual(len(self.MesMedias.medias), 1)
        self.assertEqual(self.MesMedias.medias[0].titre, "Le Seigneur des Anneaux")
        self.MesMedias.ajouter_media(self.cd)
        self.assertEqual(len(self.MesMedias.medias), 2)
        self.assertEqual(self.MesMedias.medias[1].auteur, "Michael Jackson")
        self.MesMedias.ajouter_media(self.dvd)
        self.assertEqual(len(self.MesMedias.medias), 3)
        self.assertEqual(self.MesMedias.medias[2].auteur, "Christopher Nolan")
        self.MesMedias.ajouter_media(self.article)
        self.assertEqual(len(self.MesMedias.medias), 4)
        self.assertEqual(self.MesMedias.medias[3].auteur, "François Dupont")

    def test_lister_medias_par_auteur(self):
        self.MesMedias.ajouter_media(self.livre)
        self.MesMedias.ajouter_media(self.cd)
        self.MesMedias.ajouter_media(self.livre)
        self.assertEqual(len(self.MesMedias.lister_medias_par_auteur("J.R.R. Tolkien")), 2)
        self.assertEqual(self.MesMedias.lister_medias_par_auteur("J.R.R. Tolkien")[0].titre, "Le Seigneur des Anneaux")

    def test_supprimer_media(self):
        self.MesMedias.ajouter_media(self.livre)
        self.MesMedias.ajouter_media(self.cd)
        self.MesMedias.supprimer_media("Le Seigneur des Anneaux", "J.R.R. Tolkien")
        self.assertEqual(len(self.MesMedias.medias), 1)
        self.assertEqual(self.MesMedias.medias[0].titre, "Thriller")

    def test_supprimer_medias_par_auteur(self):
        self.MesMedias.ajouter_media(self.livre)
        self.MesMedias.ajouter_media(self.cd)
        self.MesMedias.ajouter_media(self.livre)
        self.MesMedias.supprimer_medias_par_auteur("J.R.R. Tolkien")
        self.assertEqual(len(self.MesMedias.medias), 1)

    def test_noter_media_preté(self):
        self.MesMedias.ajouter_media(self.livre)
        self.MesMedias.noter_media_preté("Le Seigneur des Anneaux", "J.R.R. Tolkien", "Jean")
        self.assertTrue(self.livre.est_preté)

    def test_compter_medias_pretes(self):
        self.MesMedias.ajouter_media(self.livre)
        self.MesMedias.ajouter_media(self.cd)
        self.MesMedias.noter_media_preté("Le Seigneur des Anneaux", "J.R.R. Tolkien", "Jean")
        self.assertEqual(self.MesMedias.compter_medias_pretes(), 1)

def interface(MaMediatheque):
    while True:
        choix = input('\n(1) Ajouter un média à ma médiatheque\n(2) Retirer un média à ma médiatheque\n(3) Afficher ma médiatheque\n(4) Quitter\n\nEntrez un chiffre : ')
        
        #------Ajout d'un media------
        if choix == '1':
            choix = input("Voulez-vous ajouter un média ? (Oui/Non) ").lower()
            if choix == "oui":
                type_media = input("Quel type de média ? (Livre/CD/DVD/Article) ").lower()
                args = []
                if type_media == "livre":
                    print("Livre : titre, auteur, date_parution, nombre_pages, editeur")
                    for i in range(0, 5):
                        args.append(input(f"Entrez l'argument {i+1} : "))
                    media = Creer_media("livre", *args)
                    MaMediatheque.ajouter_media(media.creer())
                elif type_media == "cd":
                    print("CD : titre, auteur, date_parution, duree, nombre_morceaux")
                    for i in range(0, 5):
                        args.append(input(f"Entrez l'argument {i+1} : "))
                    media = Creer_media("cd", *args)
                    MaMediatheque.ajouter_media(media.creer())
                elif type_media == "dvd":
                    print("DVD : titre, auteur, date_parution, duree")
                    for i in range(0, 4):
                        args.append(input(f"Entrez l'argument {i+1} : "))
                    media = Creer_media("dvd", *args)
                    MaMediatheque.ajouter_media(media.creer())
                elif type_media == "article":
                    print("Article : titre, auteur, date_parution, nom_mag, numero_mag, intervalle_pages")
                    for i in range(0, 6):
                        args.append(input(f"Entrez l'argument {i+1} : "))
                    media = Creer_media("article", *args)
                    MaMediatheque.ajouter_media(media.creer())
                else:
                    print("Type de média invalide.")
            elif choix == "non":
                break
            else:
                print("Veuillez répondre par 'Oui' ou 'Non'.")

        #------Supression d'un media------
        elif choix == '2' :
            titresupr = input("Entrez le titre du média à supprimer : ")
            auteursupr = input("Entrez le nom de l'auteur du média à supprimer : ")
            MaMediatheque.supprimer_media(titresupr, auteursupr)

        #------Affichage des medias------
        elif choix == '3':
            for media in MaMediatheque.medias:
                print(media)
        
        elif choix == '4':
            return
        
        else :
            print("Veuillez entrez un chiffre correspondant aux différents choix")



def main() :
    print("(1) Test unitaires\n(2) Gestion des médias")
    choix = input("Entrez votre choix : ")
    if choix == "1":
        unittest.main(verbosity=2)
    elif choix == "2":
        MaMediatheque = MesMedias()
        interface(MaMediatheque);
    else:
        print("Choix invalide. Veuillez taper 1 ou 2.")
    
if __name__ == "__main__": 
    main()
