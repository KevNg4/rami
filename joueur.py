class Joueur:
    def __init__(self, nom='', numero=0):
        self.nom = nom
        self.numero = numero  # si besoin
        self.main = []

    def combinaison (self):
        choix = input("Entrez les numéros des cartes que vous souhaitez poser, séparés par des espaces, ou appuyez entrer si vous souhaitez ne rien poser : ") # Demander au joueur de choisir des cartes à poser
        
        indices = [int(num) - 1 for num in choix.split()] # pour traiter les entrées du joueur puis les stocker dans une liste d'indices de cartes
        
        cartes_choisies = [] # pour stocker les cartes choisies
        
        for indice in sorted(indices, reverse=True):
                cartes_choisies.append(self.main[indice])
                del self.main[indice]

        if len(cartes_choisies) >= 3: # condition 1: il faut au moins 3 cartes dans la combinaison   
            # insérer code=> condition 2: interdiction de chosir 2 jokers  
            if len(set(carte.valeur for carte in cartes_choisies)) == 1: # condition 3.1: combinaison de même valeur + couleurs différentes
                if len(set(carte.couleur for carte in cartes_choisies)) != 1 :
                    print("Combinaison correcte: mêmes valeurs + couleurs différentes")
            else:
                if len(set(carte.couleur for carte in cartes_choisies)) == 1: # condition 3.2: combinaison de même couleur + valeurs consécutives
                    valeurs = sorted(carte.valeur for carte in cartes_choisies)
                    if set(valeurs) == set(range(min(valeurs), max(valeurs) + 1)):
                        print("Combinaison correcte: même couleur + valeurs qui se suivent")
                    else: # else condition 3.2
                        print("Combinaison incorrecte: Les valeurs des cartes ne se suivent pas ou n'ont pas une différence de 1") 
                        cartes_choisies = []
        
        else: # else condition 1
            print("Veuillez choisir au moins 3 cartes")     
            cartes_choisies = [] 

        return cartes_choisies


