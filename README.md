## Projet UE - POO en python : le rami
**Règles du jeu**

Il se joue avec un jeu de 52 cartes et les jokers, à partir de 2 joueurs. 
L’ordre des cartes est classique, avec la particularité que l’as peut être soit en premier, avant le 2, soit en dernier, après le roi.
On distribue à chaque joueur 13 cartes et on retourne la première carte du talon à côté de la
pioche.

Les joueurs doivent alors chacun réaliser des combinaisons d’au moins 3 cartes avec leur jeu, soit
des suites (cartes se suivant dans la même couleur), soit des collections (cartes identiques mais de
couleurs différentes, par exemple 3 valets : pique, cœur, trèfle).

A chaque tour :
• le joueur pioche une carte dans la pioche 
• pose une combinaison s’il le peut
• et rejette une carte sur le talon face visible.

Le joker remplace n’importe quelle carte, mais il ne peut y avoir qu’un seul joker par
combinaison. 

Le gagnant est le joueur qui a le moins de carte dans son jeu quand plus aucune combinaison n’est
possible ou bien aucune carte en premier.

**Fait**
 - Choix du nombre de joueurs
 - Choix de la valeur de l'AS
 - Pris en compte des jokers
 - Règles basiques de combinaisons
 - Gestion de la pioche vide
 - Gestion de la fin de partie 

**Non fait (car facultatif)** 
 - Facultatif : piocher soit dans la pioche, soit la carte du talon retournée
 - Facultatif : une fois le jeu commencé, les joueurs peuvent enrichir les combinaisons déjà posées (par exemple, rajouter le 4ème valet ou mettre un 10 de cœur après un 9 de cœur).
 - Facultatif : le joker peut être remplacé par la carte correspondante par un autre joueur, dans ce cas, le joueur ne peut le conserver dans son jeu, il doit le réutiliser immédiatement dans une autre combinaison.

**NB:** 
Pour faciliter le test du programme et l'expérience du jeu, les cartes des joueurs ont été ordonnées (triées), et les valeurs numériques sont visibles.
```
