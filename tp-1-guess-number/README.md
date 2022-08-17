# TP 1 - Nombre mystère

[Retour](../README.md)

## Présentation

Le but de ce projet est de permettre à un joueur d'essayer de deviner un nombre mystère généré aléatoirement par l'ordinateur, en 5 essais ou moins.

## Completer ce script

```
import random

random_number = 5 # random.randint(1, 10)
user_number = input('Saisir un nombre :')
user_number = int(user_number)
while True:
    if random_number == user_number:
        print('Trouvé')
        break
    else:
        user_number = input('Saisir un nombre :')
        user_number = int(user_number)
```

## Notions techniques à appliquer

- Affichage et saisie utilisateur
- Conversion de valeur
- Module random
- Les boucles
- Condition

## Description

Au début du script, vous devez générer un nombre aléatoire compris entre 0 et 10 (vous pouvez agrandir ou réduire cet intervalle pour simplifier ou complexifier le jeu).

Le joueur dispose alors de 5 essais (là encore, libre à vous de changer cette valeur) pour trouver le nombre mystère.

À chaque essai, vous devez indiquer au joueur si le nombre qu'il a entré est plus petit ou plus grand que le nombre mystère.

Si le nombre entré par l'utilisateur est égal au nombre mystère, alors le joueur gagne la partie.

Dans le cas d'une victoire, vous devez indiquer au joueur combien d'essais ont été nécessaires pour gagner.

Si le joueur ne trouve pas le nombre mystère avec les 5 essais disponibles, il perd la partie.

[https://raw.githubusercontent.com/techmindconsulting/workshop-python/main/tp-1-guess-number/main.py](Récupérer le fichier à compléter)

## Allez plus loin
Proposer une nouvelle plage de nombre selon le nombre saisi
Afficher le compteur d'essai à chaque saisi
### Démonstration 

```
Essai n°1 - Saisir un nombre un nombre entre 1 et 100 : 55
55 est trop petit
Essai n°2 - Saisir un nombre un nombre entre 55 et 100 : 78
78 est trop grand
Essai n°3 - Saisir un nombre un nombre entre 55 et 78 : 65
65 est trop grand
Essai n°4 - Saisir un nombre un nombre entre 55 et 65 : 58
GAGNE :D! Trouvé au bout de 4 tentative(s)
```

```
Essai n°1 - Saisir un nombre un nombre entre 1 et 100 : 1
1 est trop petit
Essai n°2 - Saisir un nombre un nombre entre 1 et 100 : 2
2 est trop petit
Essai n°3 - Saisir un nombre un nombre entre 2 et 100 : 3
3 est trop petit
Essai n°4 - Saisir un nombre un nombre entre 3 et 100 : 4
4 est trop petit
Essai n°5 - Saisir un nombre un nombre entre 4 et 100 : 5
5 est trop petit
PERDU :(! Le nombre aléatoire était 20
```

## Documentation

- [Les nombres](https://docs.python.org/fr/3/tutorial/introduction.html#numbers)

- [Les chaines de caractères](https://docs.python.org/fr/3/tutorial/introduction.html#strings)

- [Les booléens](https://docs.python.org/fr/3/library/stdtypes.html#truth-value-testing)

- [Premier pas vers la programmation](https://docs.python.org/fr/3/tutorial/introduction.html#first-steps-towards-programming)

- [L'instruction if](https://docs.python.org/fr/3/tutorial/controlflow.html#if-statements)

- [Définir une fonction](https://docs.python.org/fr/3/tutorial/controlflow.html#defining-functions)

- [La méthode de chaine de caractère format()](https://docs.python.org/fr/3/tutorial/inputoutput.html#the-string-format-method)

- [Les exception](https://docs.python.org/fr/3/tutorial/errors.html#exceptions)

- [Gestion des exceptions](https://docs.python.org/fr/3/tutorial/errors.html#handling-exceptions)

- [Syle de code](https://docs.python.org/fr/3/tutorial/controlflow.html#intermezzo-coding-style)

- [Module random](https://docs.python.org/fr/3/library/random.html)

[Retour](../README.md)