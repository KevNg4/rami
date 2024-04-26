import random
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

liste_joueurs = [] # liste comportant tous les joueurs (objets de la classe Joueur)

for i in range(1, nb_joueurs + 1): # demande le nom du joueur et attribution du numéro (dans le cas où on en aurait besoin)
    nom = input("Entrez le nom du joueur {} : ".format(i))
    num = i 
    joueur = Joueur(nom) # création d'un objet joueur de la classe Joueur
    joueur.numero = num 
    liste_joueurs.append(joueur) # ajour du joueur dans la liste

print('\nLes joueurs sont :') # récapitulatif des joueurs
for i, joueur in enumerate(liste_joueurs, start=1):
    print("Joueur {0} : {1}".format(joueur.numero, joueur.nom))

paquet = Paquet() # création d'un paquet de cartes
paquet.melanger() # on mélange le paquet
paquet.couper() # on coupe le paquet
print('\nLe paquet a été mélangé puis coupé!')

distributions = paquet.distribuer(nb_joueurs, 13) # distribution de 13 cartes à chaque joueur 
for i, joueur in enumerate(liste_joueurs):
    joueur.main = distributions[i] # les cartes des joueurs sont stockées dans l'attribut main de chaque objet joueur (qui est une liste)

talon = [paquet.piocher()] # création du talon (une liste) par l'ajout d'une carte de la pioche dans le talon
print(talon)

indice_joueur = random.randint(0, len(liste_joueurs) - 1) # choix aléatoire du joueur qui commence la partie
compteur_passe = 0 # nombre de passes successives
while True:
    joueur = liste_joueurs[indice_joueur] # joueur qui joue
    print(f"\nC'est au tour du joueur {joueur.numero} : {joueur.nom}")
    print("\nNombre de passe actuellement: {}".format(compteur_passe))

    pioche = paquet.piocher() # carte piochée par le joueur
    joueur.main.append(pioche) # ajout de la carte piochée à la main du joueur
    print("\nVous avez piocher : {}".format(pioche))
    
    print("\nVoici vos cartes : ")
    print(joueur.main)
    
    cartes_choisies = joueur.combinaison() # récupération des cartes choisies par la méthode combinaision
    if len(cartes_choisies) == 0: # si la liste de cartes choisies est vide
        compteur_passe += 1 # incrémente de 1 le nombre de passes
    else:
        for carte in cartes_choisies: # ajout de chaque carte de la combinaison du joueur au talon
            talon.append(carte)
            compteur_passe = 0 # rénitialisation du compteur de passes
    
    print("\nVoici vos cartes après la pose de combinaison ")
    print(joueur.main)
    
    # insérer code=> rejetter une carte
    
    print("\nTalon après choix et rejet : ")
    print(talon)
    
    if len(joueur.main) == 0: # mettre fin au jeu si la main du joueur ne contient plus de carte
        print(f"\nLe joueur {joueur.numero} : {joueur.nom} a gagné! BRAVO!")
        print("\nFIN DE LA PARTIE")
        break # permet de stopper la boucle qui permet de passer à un autre joueur
    
    if compteur_passe == len(liste_joueurs): # si tous les joueurs ont passé
        print("\nAucun joueur n'a pu poser de combinaison. La partie est terminée!")
        joueur_gagnant = min(liste_joueurs, key=lambda joueur: len(joueur.main)) # à expliquer
        print(f"\nLe joueur {joueur_gagnant.numero} : {joueur_gagnant.nom} a gagné avec la main la plus petite. BRAVO!")
        print("\nFIN DE LA PARTIE")
        break
    # et s'il y a égalité???


# pioche obligatoire
""" print("\nMain du joueur AVANT pioche : ")
print(liste_joueurs[0].main)
liste_joueurs[0].main.append(paquet.piocher())
print("\nMain du joueur APRES pioche : ")
print(liste_joueurs[0].main)


for carte in liste_joueurs[0].combinaison():
    talon.append(carte)

print("\nMain du joueur après choix : ")
print(liste_joueurs[0].main)
print("\nTalon après choix : ")
print(talon) """


# choix combinaison
# check combinaison ok
