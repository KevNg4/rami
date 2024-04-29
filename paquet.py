from carte import Carte # pour utiliser les tuples valeurs_valides et couleurs_valides
from random import shuffle, randrange # pour aléatoire

class Paquet:
   def __init__(self):
       self.cartes = [] # cartes du paquet
       for couleur in Carte.couleurs_valides: # boucle qui crée toutes les cartes possibles
           for valeur in Carte.valeurs_valides:
                point = Carte.valeurs_valides.index(valeur) + 1
                self.cartes.append(Carte(valeur, couleur, point)) # ajout à la liste des cartes du paquet
       joker = Carte('JOKER', 'JOKER', 0) # carte joker avec point=0
       self.cartes.append(joker) # ajout joker
       self.cartes.append(joker) # ajout joker

   def __repr__(self):
       return str(self.cartes) # la représentation de l'objet ne peut être une liste (d'où le str)

   def melanger(self):
       shuffle(self.cartes)

   def couper(self):
       nb_cartes = randrange(len(self.cartes))
       self.cartes = self.cartes[nb_cartes:] + self.cartes[:nb_cartes]

   def piocher(self):
       pioche = self.cartes[0]
       self.cartes = self.cartes[1:]
       return pioche

   def distribuer(self, Njoueurs, Ncartes):
       distribution = [[] for i in range(0, Njoueurs)] # listes dans une liste où chaque liste est la main d'un joueur
       for j in range(0, Ncartes):
           for i in range(0, Njoueurs):
               carte = self.piocher()
               distribution[i].append(carte)
       return distribution