class Carte:
    couleurs_valides = ("TREFLE", "COEUR", "CARREAU", "PIQUE")
    valeurs_valides = tuple(list(range(1, 11)) + ["VALET", "DAME", "ROI"])

    def __init__(self, valeur, couleur, point):
        self.valeur = valeur
        self.couleur = couleur
        self.point = point # ajout de l'attribut point pour gérér la condition des valeurs consécutives
    
    def points(self): # inutile jusqu'à présent 
        return Carte.valeurs_valides.index(self.valeur) + 1

    def modifier(self): # même si c'est une action du joueur, c'est une action qui s'applique sur un objet de Carte
        for i, valeur in enumerate(Carte.valeurs_valides, start=1):
                    print(f"{i} : {valeur}")
        nouvelle_valeur = int(input("\n* Entrez la nouvelle valeur pour le Joker : "))

        for i, couleur in enumerate(Carte.couleurs_valides, start=1):
                            print(f"{i} : {couleur}")
        nouvelle_couleur = int(input("\n* Entrez la nouvelle couleur pour le Joker : "))

        self.valeur = Carte.valeurs_valides[nouvelle_valeur-1]
        self.couleur = Carte.couleurs_valides[nouvelle_couleur-1]
        self.point = Carte.valeurs_valides.index(self.valeur) + 1
        
        return self

    def __repr__(self): # méthode spéciale en Python utilisée pour définir la représentation "officielle" d'un objet. Pour pourvoir ensuite faire un print(c)
        return "Carte {0} de {1} (= {2})".format(self.valeur, self.couleur, self.point)
    