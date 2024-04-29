class Carte:
    couleurs_valides = ("TREFLE", "COEUR", "CARREAU", "PIQUE")
    valeurs_valides = tuple(list(range(1, 11)) + ["VALET", "DAME", "ROI"])

    def __init__(self, valeur, couleur, point):
        self.valeur = valeur
        self.couleur = couleur
        self.point = point # pour gérér condition valeurs consécutives
    
    def points(self): # inutile mais défini pendant le cours
        return Carte.valeurs_valides.index(self.valeur) + 1

    def modifier(self): # pour modifier valeur et couleur joker
        print("\nValeurs possibles : ")
        for numero, valeur in enumerate(Carte.valeurs_valides, start=1): # numéro : valeur 
            print(f"{numero} : {valeur}")
        try:
            nouvelle_valeur = int(input("\n* Entrez le numéro correspondant à la valeur du joker : ")) 
        except ValueError:
            print("ERREUR : saisie de la valeur incorrecte")
        if nouvelle_valeur > 13:
            print("ERREUR : saisie de la valeur incorrecte")
            nouvelle_valeur = int(input("\n* Entrez le numéro correspondant à la valeur du joker : "))
            
        print("\nCouleurs possibles : ")
        for numero, couleur in enumerate(Carte.couleurs_valides, start=1): # numéro : couleur
            print(f"{numero} : {couleur}")
        try:
            nouvelle_couleur = int(input("\n* Entrez le numéro correspondant à la couleur du joker : "))
        except ValueError:
            print("ERREUR : saisie de la couleur incorrecte")
        if nouvelle_couleur > 4:
            print("ERREUR : saisie de la couleur incorrecte")
            nouvelle_valeur = int(input("\n* Entrez le numéro correspondant à la couleur du joker : "))
        
        self.valeur = Carte.valeurs_valides[nouvelle_valeur-1] 
        self.couleur = Carte.couleurs_valides[nouvelle_couleur-1]
        self.point = Carte.valeurs_valides.index(self.valeur) + 1
        
        return self

    def __repr__(self): # manière dont les objets sont affichés
        return "Carte {0} de {1} (= {2})".format(self.valeur, self.couleur, self.point)
    