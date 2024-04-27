class Carte:
    couleurs_valides = ("TREFLE", "COEUR", "CARREAU", "PIQUE")
    valeurs_valides = tuple(list(range(1, 11)) + ["VALET", "DAME", "ROI"])

    def __init__(self, valeur, couleur, point):
        self.valeur = valeur
        self.couleur = couleur
        self.point = point
    
    def points(self):
        return Carte.valeurs_valides.index(self.valeur) + 1

    def __repr__(self): # méthode spéciale en Python utilisée pour définir la représentation "officielle" d'un objet. Pour pourvoir ensuite faire un print(c)
        return "Carte {0} de {1} (= {2})".format(self.valeur, self.couleur, self.point)