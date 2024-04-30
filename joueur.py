from carte import Carte

class Joueur:
    def __init__(self, nom='', numero=0):
        self.nom = nom
        self.numero = numero 
        self.main = []

    def combinaison(self): # choix combinaison avec règles (NB: on aurait pu l'appeller chosir (verbe) car c'est une action...)
        while True: 
            choix = input("\n* Entrez les numéros des cartes que vous souhaitez poser, séparés par des espaces, ou appuyez entrer si vous souhaitez ne rien poser : ")
            cartes_choisies = [] # stockage cartes choisies
            # Traitement des entrées de l'utilisateur 
            try: # empêcher string
                indices = [int(num) - 1 for num in choix.split()]  # conversion entrées en liste d'indices
            except ValueError: # si pas des entiers par exemple
                print("ERREUR : saisie des cartes incorrecte")
                continue # pour rester dans la boucle while et pas mettre fin à la partie
            
            if any(indice >= len(self.main) for indice in indices): # empêcher indice de carte non existant
                print("\nVous avez choisi un numéro de carte invalide")
                continue  # pour rester dans la boucle while et ne pas mettre fin à la partie
               
            for indice in sorted(indices, reverse=True): # ajout cartes choisies dans cartes_choisies sans prendre en compte les règles
                cartes_choisies.append(self.main[indice])
            
            for carte in cartes_choisies: # si une carte choisie est un joker=> choisir valeur et couleur
                if carte.valeur == "JOKER":
                    carte.modifier() # NB: même si la combinaison est fausse, le joker garde la valeur et la couleur choisies (transformation définitive)
            # Règles de combinaisons
            if len(cartes_choisies) >= 1 and len(cartes_choisies) <= 2: # condition 1: au moins 3 cartes pour poser une combinaison
                print("\nVeuillez choisir au moins 3 cartes")
                cartes_choisies = [] # enlever les cartes choisies
            
            elif len(cartes_choisies) == 0: # pas de combinaison = passe (autorisé)
                print("\nVous n'avez rien posé, donc vous passez")
                break
            
            elif len([carte for carte in cartes_choisies if carte.valeur == "JOKER"]) >= 2: # condition 2: pas plus de 2 jokers dans son choix
                print("\nVous ne pouvez pas choisir plus de deux cartes Joker pour une combinaison")
                cartes_choisies = [] # enlever les cartes choisies
            
            elif len(set(carte.valeur for carte in cartes_choisies)) == 1 and len(set(carte.couleur for carte in cartes_choisies)) != 1: # condition 3.1: combinaison valeur idem + couleurs différentes
                for indice in sorted(indices, reverse=True):
                        del self.main[indice] # retrait cartes choisies de la main du joueur
                print("\nCombinaison correcte: mêmes valeurs + couleurs différentes")
                break
            
            elif len(set(carte.couleur for carte in cartes_choisies)) == 1 and set(carte.point for carte in cartes_choisies) == set(range(min(carte.point for carte in cartes_choisies), max(carte.point for carte in cartes_choisies) + 1)): # condition 3.2: couleurs idem + valeurs consécutives
                for indice in sorted(indices, reverse=True):
                        del self.main[indice] # retrait cartes choisies de la main du joueur
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
            try: # pas de string dans la saisie
                choix = int(input("\n* Entrez le numéro de la carte que vous voulez rejeter : ")) 
            except ValueError:
                print("ERREUR : saisie de carte incorrecte")
                continue # pour rester dans la boucle while et ne pas mettre fin à la partie
                
            if choix > len(self.main) : # empêcher indice de carte non existant
                print("\nVous avez choisi un numéro de carte invalide")
                continue  # pour rester dans la boucle while et ne pas mettre fin à la partie
            else: 
                carte_rejetee = self.main[choix-1]
                del self.main[choix-1] # retrait carte de la main
                break
            
        return carte_rejetee

    def trier(self): #trier par couleur et par valeur 
        self.main.sort(key=lambda carte: (carte.couleur, carte.point))