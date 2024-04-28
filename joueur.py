from carte import Carte

class Joueur:
    def __init__(self, nom='', point=0):
        self.nom = nom
        self.point = point  
        self.main = []

    def combinaison(self): # on aurait pu l'appeller chosir (verbe) car c'est une action...
        while True: 
            choix = input("\n* Entrez les numéros des cartes que vous souhaitez poser, séparés par des espaces, ou appuyez entrer si vous souhaitez ne rien poser : ")
            cartes_choisies = [] # pour stocker les cartes choisies
            # Traitement des entrées de l'utilisateur 
            try: # pas de littéral dans la saisie
                indices = [int(num) - 1 for num in choix.split()]  # pour traiter les entrées du joueur puis les stocker dans une liste d'indices de cartes
                print(indices) # test
                print(len(self.main)) # test
            except ValueError:
                print("ERREUR : saisie de carte incorrecte")
                continue # pour rester dans la boucle while et ne pas mettre fin à la partie
            
            if any(indice >= len(self.main) for indice in indices): # dans le cas ou une carte n'existe pas (la position de la carte est incorrecte)
                print("\nVous avez choisi un numéro de carte invalide")
                continue  # pour rester dans la boucle while et ne pas mettre fin à la partie
               
            for indice in sorted(indices, reverse=True): # ajout des cartes choisies dans cartes_choisies sans prendre en compte les conditions
                cartes_choisies.append(self.main[indice])
            
            for carte in cartes_choisies:
                if carte.valeur == "JOKER":
                    carte.modifier() # même si la combinaison est fausse, le joker garde la valeur et la couleur que vous avez choisi
            
            # Règles de combinaisons
            if len(cartes_choisies) >= 1 and len(cartes_choisies) <= 2: # condition 1: il faut au moins 3 cartes pour poser une combinaison
                print("\nVeuillez choisir au moins 3 cartes")
                cartes_choisies = []
            
            elif len(cartes_choisies) == 0: # pas de combinaison = passe (autorisé)
                print("\nVous n'avez rien poser, donc vous passez")
                break
            
            elif len([carte for carte in cartes_choisies if carte.valeur == "JOKER"]) >= 2: # condition 2: pas plus de 2 jokers dans son choix
                print("\nVous ne pouvez pas choisir plus de deux cartes Joker pour une combinaison")
                cartes_choisies = []
            
            elif len(set(carte.valeur for carte in cartes_choisies)) == 1 and len(set(carte.couleur for carte in cartes_choisies)) != 1: # condition 3.1: combinaison de même valeur + couleurs différentes
                for indice in sorted(indices, reverse=True):
                        del self.main[indice] # on retire les cartes choisies de la main du joueur
                print("\nCombinaison correcte: mêmes valeurs + couleurs différentes")
                break
            
            elif len(set(carte.couleur for carte in cartes_choisies)) == 1 and set(carte.point for carte in cartes_choisies) == set(range(min(carte.point for carte in cartes_choisies), max(carte.point for carte in cartes_choisies) + 1)): # condition 3.2: combinaison de même couleur + valeurs consécutives
                for indice in sorted(indices, reverse=True):
                        del self.main[indice] # on retire les cartes choisies de la main du joueur
                print("\nCombinaison correcte: même couleur + valeurs qui se suivent")
                break
            else:
                print("\nCombinaison incorrecte: Les valeurs des cartes ne se suivent pas ou n'ont pas une différence de 1") 
                cartes_choisies = []         
        
        cartes_choisies.sort(key=lambda carte: (carte.point)) # pour ordonner la liste cartes_choisies par point 
        print(f"Vous avez donc posé : {cartes_choisies}")
        return cartes_choisies
    
    def rejeter(self):
        while True:
            try: # pas de littéral dans la saisie
                choix = int(input("\n* Entrez le numéro de la carte que vous voulez rejeter : ")) 
            except ValueError:
                print("ERREUR : saisie de carte incorrecte")
                continue # pour rester dans la boucle while et ne pas mettre fin à la partie
                
            if choix > len(self.main) : # dans le cas ou une carte n'existe pas (la position de la carte est incorrecte)
                print("\nVous avez choisi un numéro de carte invalide")
                continue  # pour rester dans la boucle while et ne pas mettre fin à la partie
            else: 
                carte_rejetee = self.main[choix-1]
                del self.main[choix-1]
                break
            
        return carte_rejetee

    def trier(self):
        self.main.sort(key=lambda carte: (carte.couleur, carte.point))