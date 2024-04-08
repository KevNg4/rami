from paquet import Paquet

print('Bienvenue dans le Rami!\n')

nb_joueurs = int(input('Combien de joueurs ? : '))

paquet = Paquet()
paquet.melanger()
paquet.couper()
# Distribution
talon = [paquet.piocher()]