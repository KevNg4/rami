from paquet import Paquet
from joueur import Joueur

print('Bienvenue dans le Rami!\n')

while True:
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

joueurs = [Joueur() for i in range(nb_joueurs)]

paquet = Paquet()
paquet.melanger()
paquet.couper()
# Distribution
talon = [paquet.piocher()]