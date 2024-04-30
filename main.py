import random
from paquet import Paquet
from joueur import Joueur


print('Bienvenue dans le rami!\n')

while True: # demande nombre joueurs
    try:
        nb_joueurs = int(input("* Combien de joueurs ? : "))
        if 2 <= nb_joueurs <= 6:
            break
        elif nb_joueurs > 6:
            print("Le rami se joue à 6 maximum")
        else:
            print("ERREUR : Vous devez entrer un nombre de joueurs")
    except ValueError:
        print("ERREUR : Vous devez entrer un nombre de joueurs")
        

liste_joueurs = [] # liste joueurs (objets de la classe Joueur)

for i in range(1, nb_joueurs + 1): # demande nom du joueur + attribution numéro
    nom = input("* Entrez le nom du joueur {} : ".format(i))
    num = i 
    joueur = Joueur(nom) # création objet joueur de la classe Joueur
    joueur.numero = num 
    liste_joueurs.append(joueur) # ajout joueur dans liste_joueurs

print('\nRECAPULATIF : Les joueurs sont :') # récapitulatif des joueurs
for i, joueur in enumerate(liste_joueurs, start=1):
    print("Joueur {0} : {1}".format(joueur.numero, joueur.nom))
print('\n' + '*' * 50) # séparateur visuel 

paquet = Paquet() # création paquet cartes
paquet.melanger() # mélange paquet
paquet.couper() # coupe paquet
print('\nLe paquet a été mélangé puis coupé!')

carte_as = input("\n* Voulez-vous que AS soit plus grand que ROI ? (O/N) : ") # choisir valeur carte AS 
while carte_as.upper() != "O" and carte_as.upper() != "N":
    print("\nERREUR: saisie incorrecte")
    carte_as = input("\n* Voulez-vous que AS soit plus grand que ROI ? (O/N) : ")
if carte_as.upper() == "O": 
    for carte in paquet.cartes:
        if carte.valeur == 'AS':
            carte.point = 14 # si oui à question, alors AS > ROI,
# pas besoin de else car par défaut AS vaut 1

distributions = paquet.distribuer(nb_joueurs, 13) # distribution 13 cartes à chaque joueur 
for i, joueur in enumerate(liste_joueurs):
    joueur.main = distributions[i] # les cartes des joueurs sont stockées dans l'attribut main de chaque objet joueur (qui est une liste)

talon = [paquet.piocher()] # création du talon (une liste) par l'ajout d'une carte de la pioche dans le talon
print(f"\nLa carte du dessus du talon est : {talon[-1]}") # affiche la carte du dessus du talon
print("\nLa partie peut commencer!")
input("\n* Appuyez sur la touche Entrer pour commencer")
print('\n' + '*' * 50) # séparateur pour l'esthétique 

indice_joueur = random.randint(0, len(liste_joueurs) - 1) # choix aléatoire du joueur qui commence la partie
compteur_passe = 0 # nombre passes successives(pour mettre fin partie)

while True:
    joueur = liste_joueurs[indice_joueur] # joueur qui joue
    print(f"\nC'est au tour du joueur {joueur.numero} : {joueur.nom}")
    input("\n* Entrer pour valider")
    print("\nNombre de passe actuellement: {}".format(compteur_passe))

    if len(paquet.cartes) == 0: # si paquet vide, former à nouveau le paquet à partir du talon 
        paquet.cartes = talon
        paquet.melanger()
        talon = [paquet.piocher()]
        pioche = paquet.piocher() # carte piochée par le joueur
        joueur.main.append(pioche) # ajout de la carte piochée à la main du joueur
    else:
        pioche = paquet.piocher() # carte piochée par le joueur
        joueur.main.append(pioche) # ajout de la carte piochée à la main du joueur
    print("\nVous avez pioché : {}".format(pioche))
    
    print("\nVoici vos cartes : ")
    joueur.trier() # le joueur va naturellement trier ses cartes dans la réalité, on ne lui demande donc pas
    for position, carte in enumerate(joueur.main, start=1):
        print(f"{position} : {carte}")
    
    cartes_choisies = joueur.combinaison() # récupération des cartes choisies par la méthode combinaision
    if len(cartes_choisies) == 0: # si la liste de cartes choisies est vide
        compteur_passe += 1 # incrémente de 1 le nombre de passes
    else:
        for carte in cartes_choisies: # ajout de chaque carte de la combinaison du joueur au talon
            talon.append(carte)
            compteur_passe = 0 # rénitialisation du compteur de passes
    
    print("\nVoici vos cartes après choix :")
    for position, carte in enumerate(joueur.main, start=1):
            print(f"{position} : {carte}")
    
    print(f"\nDessus du talon : {talon[-1]}") # affiche la carte du dessus du talon
    
    print('\nVeuillez rejeter une carte de votre main dans le talon')
    carte_rejetee = joueur.rejeter()
    talon.append(carte_rejetee)
    
    print(f"\nLa carte du dessus du talon est : {talon[-1]}") # affiche la carte du dessus du talon
    # Fin de la partie
    if len(joueur.main) == 0: # mettre fin au jeu si la main du joueur ne contient plus de carte
        print(f"\nLe joueur {joueur.numero} : {joueur.nom} a gagné! BRAVO!")
        print("\nFIN DE LA PARTIE")
        break # permet de stopper la boucle qui permet de passer à un autre joueur
    
    input("\n* Entrer pour terminer votre tour et passer au joueur suivant")
    print('\n' + '*' * 50) # séparateur pour l'esthétique 
    
    if compteur_passe == len(liste_joueurs): # si tous les joueurs ont passé
        print("\nAucun joueur n'a pu poser de combinaison. La partie est terminée!")
        joueur_gagnant = min(liste_joueurs, key=lambda joueur: len(joueur.main)) # C'est une fonction, mais à expliquer...
        print(f"\nLe joueur {joueur_gagnant.numero} : {joueur_gagnant.nom} a gagné avec la main la plus petite. BRAVO!")
        print("\nFIN DE LA PARTIE")
        break
    # et s'il y a égalité???
    indice_joueur = (indice_joueur + 1) % len(liste_joueurs) # permet de passer au joueur suivant en incrémentant l'indice de liste_joueurs de 1 et de revenir au premier joueur après le dernier joueur de la liste