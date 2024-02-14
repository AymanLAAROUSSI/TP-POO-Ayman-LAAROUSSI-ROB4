import math

class Vecteur:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def additionner(self, autre_vecteur):
        return Vecteur(self.x + autre_vecteur.x, self.y + autre_vecteur.y, self.z + autre_vecteur.z)

    def calculer_norme(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def calculer_produit_scalaire(self, autre_vecteur):
        return self.x * autre_vecteur.x + self.y * autre_vecteur.y + self.z * autre_vecteur.z

    def tourner(self, alpha):
        new_x = self.x * math.cos(alpha) - self.y * math.sin(alpha)
        new_y = self.x * math.sin(alpha) + self.y * math.cos(alpha)
        return Vecteur(new_x, new_y, self.z)

    def afficher(self):
        print(f"({self.x}, {self.y}, {self.z})")


