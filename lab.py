from carte import Carte
from paquet import Paquet
from joueur import Joueur

paquet = Paquet()
paquet.melanger()
paquet.couper()
talon = [paquet.piocher()]
joueur = Joueur()

""" joueur.main = paquet.distribuer(1, 13)[0] # distribution
print(joueur.main) """



""" print("\nVoici vos cartes : ")
joueur.trier()
for position, carte in enumerate(joueur.main, start=1):
    print(f"{position} : {carte}") """

""" for carte in joueur.main:
    if carte.valeur == "JOKER":
        indice = int(input(""))
        carte = joueur.main[indice-1]
        
        for i, valeur in enumerate(Carte.valeurs_valides, start=1):
                    print(f"{i} : {valeur}")
        nouvelle_valeur = int(input("Entrez la nouvelle valeur pour le Joker : "))

        for i, couleur in enumerate(Carte.couleurs_valides, start=1):
                            print(f"{i} : {couleur}")
        nouvelle_couleur = int(input("Entrez la nouvelle couleur pour le Joker : "))

        carte.valeur = Carte.valeurs_valides[nouvelle_valeur-1]
        carte.couleur = Carte.couleurs_valides[nouvelle_couleur-1]
        carte.point = Carte.valeurs_valides.index(carte.valeur) + 1

        print("\nVoici vos cartes : ")
        for position, carte in enumerate(joueur.main, start=1):
            print(f"{position} : {carte}")

print("Fin du test") """

""" joueur.combinaison() """

print("fin")
