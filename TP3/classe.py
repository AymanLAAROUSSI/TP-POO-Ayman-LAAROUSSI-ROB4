# ---------- Media ----------

class Media:
    def __init__(self, titre, auteur, date_parution):
        self.titre = titre
        self.auteur = auteur
        self.date_parution = date_parution
        self.est_preté = False
        self.emprunteur = None

    def __str__(self):
        return f"{self.titre} - {self.auteur}"

    def preter(self, nom_emprunteur):
        self.est_preté = True
        self.emprunteur = nom_emprunteur

    def rendre(self):
        self.est_preté = False
        self.emprunteur = None

# ---------- Livre (Heritage : Media) ----------

class Livre(Media):
    def __init__(self, titre, auteur, date_parution, nombre_pages, editeur):
        super().__init__(titre, auteur, date_parution)
        self.nombre_pages = nombre_pages
        self.editeur = editeur

# ---------- CD (Heritage : Media) ----------

class CD(Media):
    def __init__(self, titre, auteur, date_parution, duree, nombre_morceaux):
        super().__init__(titre, auteur, date_parution)
        self.duree = duree
        self.nombre_morceaux = nombre_morceaux

# ---------- DVD (Heritage : Media) ----------

class DVD(Media):
    def __init__(self, titre, auteur, date_parution, duree):
        super().__init__(titre, auteur, date_parution)
        self.duree = duree

# ---------- Article de Magazine (Heritage : Media) ----------

class ArticleMag(Media):
    def __init__(self, titre, auteur, date_parution, nom_mag, numero_mag, intervalle_pages):
        super().__init__(titre, auteur, date_parution)
        self.nom_mag = nom_mag
        self.numero_mag = numero_mag
        self.intervalle_pages = intervalle_pages

# ---------- MesMedia ----------

class MesMedias:
    def __init__(self):
        self.medias = []

    def ajouter_media(self, media):
        self.medias.append(media)

    def lister_medias_par_auteur(self, auteur):
        return [media for media in self.medias if media.auteur == auteur]

    def supprimer_media(self, titre, auteur):
        self.medias = [media for media in self.medias if media.titre != titre or media.auteur != auteur]

    def supprimer_medias_par_auteur(self, auteur):
        self.medias = [media for media in self.medias if media.auteur != auteur]

    def noter_media_preté(self, titre, auteur, nom_emprunteur):
        for media in self.medias:
            if media.titre == titre and media.auteur == auteur:
                media.preter(nom_emprunteur)

    def compter_medias_pretes(self):
        return sum(1 for media in self.medias if media.est_preté)
    
# ---------- Creer un nouveau media ----------
   
class Creer_media:
    def __init__(self, type_media, *args):
        self.type_media = type_media
        self.args = args
    
    def creer(self) :
        if self.type_media == "livre" :
            return Livre(*self.args)          
        elif self.type_media == "cd" :
            return CD(*self.args)  
        elif self.type_media == "dvd" :
            return DVD(*self.args)  
        elif self.type_media == "article" :
            return ArticleMag(*self.args)
        else:
            print("Type de média ou le nombre d'arguments est invalide")
    