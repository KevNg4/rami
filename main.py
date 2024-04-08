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
joueur1, joueur2 = p1.distribuer(2, 3)
print("Voici la main du joueur 1 : {}".format(joueur1))
print("Voici la main du joueur 2 : {}".format(joueur2))

print("\nPaquet après distribution :")
print(p1)