from paquet import Paquet
from joueur import Joueur

print('Bienvenue dans le Rami!\n')

while True: # nombre de joueurs
    try:
        nb_joueurs = int(input("Combien de joueurs ? : "))
        if 2 <= nb_joueurs <= 6:
            break
        elif nb_joueurs > 6:
            print("Le rami se joue à 6 maximum")
        else:
            print("Erreur : Vous devez entrer un nombre de joueurs")
    except ValueError:
        print("Erreur : Vous devez entrer un nombre de joueurs")

liste_joueurs = [] # liste comportant les objets "joueur"

for i in range(1, nb_joueurs + 1): # demande nom du joueur et attribution du numéro
    nom = input("Entrez le nom du joueur {0}: ".format(i))
    num = i
    joueur = Joueur(nom)
    joueur.numero = num
    liste_joueurs.append(joueur)

print('\nLes joueurs sont :') # récapitulatif des joueurs
for i, joueur in enumerate(liste_joueurs, start=1):
    print("Joueur {0}: {1}".format(joueur.numero, joueur.nom))

paquet = Paquet()
paquet.melanger()
paquet.couper()
print('\nLe paquet a été mélangé puis coupé!')

distributions = paquet.distribuer(nb_joueurs, 13) # distribution
for i, joueur in enumerate(liste_joueurs):
    joueur.main = distributions[i]

talon = [paquet.piocher()]