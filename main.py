from carte import Carte
from paquet import Paquet

c = Carte("DAME", "PIQUE")
print(c.valeur)
print(c.couleur)
print(c.points())
print(c) # permi grâce à __repr__(self)

p1 = Paquet()
print("\nPaquet initial :")
print(p1)

print("\nPaquet après mélange :")
p1.melanger()
print(p1)

print("\nPaquet après coupe :")
p1.couper()
print(p1)

print("\nCarte piochée :")
print(p1.piocher())

print("\nPaquet après pioche :")
print(p1)

print("\nMains :")
joueur1, joueur2 = p1.distribuer(2, 13)
print("Voici la main du joueur 1 : {}".format(joueur1))
print("Voici la main du joueur 2 : {}".format(joueur2))

print("\nPaquet après distribution :")
print(p1)

talon = [p1.piocher()]
print('\nLe talon : ')
print(talon)

print("\nPaquet après formation du talon :")
print(p1)


nb_joueurs = int(input("Combien de joueurs ? : "))
liste_joueurs = [] # liste comportant les objets "joueur"
for i in range(1, nb_joueurs + 1): # demande nom du joueur et attribution du numéro
    nom = input("Entrez le nom du joueur {0}: ".format(i))
    num = i
    joueur = Joueur(nom)
    joueur.numero = num
    liste_joueurs.append(joueur)

paquet = Paquet()
paquet.melanger()
paquet.couper()
print('\nLe paquet a été mélangé puis coupé!')

distributions = paquet.distribuer(nb_joueurs, 13) # distribution
for i, joueur in enumerate(liste_joueurs):
    joueur.main = distributions[i]

talon = [paquet.piocher()]

print(type(talon[0]))