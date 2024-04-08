from carte import Carte
from random import shuffle, randrange
class Paquet:
   def __init__(self):
       self.cartes = []
       for couleur in Carte.couleurs_valides:
           for valeur in Carte.valeurs_valides:
               c = Carte(valeur, couleur)
               self.cartes.append(c)
       self.cartes.append(Carte('JOKER', 'JOKER'))
       self.cartes.append(Carte('JOKER', 'JOKER'))

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
       distribution = [[] for i in range(0, Njoueurs)]
       for j in range(0, Ncartes):
           for i in range(0, Njoueurs):
               carte = self.piocher()
               distribution[i].append(carte)
       return distribution