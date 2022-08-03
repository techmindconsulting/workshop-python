# TP 1 - Nombre mystère

[Retour](../README.md)

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

## Déroulé du script

Au début du script, vous devez générer un nombre aléatoire compris entre 0 et 10 (vous pouvez agrandir ou réduire cet intervalle pour simplifier ou complexifier le jeu).

Le joueur dispose alors de 5 essais (là encore, libre à vous de changer cette valeur) pour trouver le nombre mystère.

À chaque essai, vous devez indiquer au joueur si le nombre qu'il a entré est plus petit ou plus grand que le nombre mystère.

Si le nombre entré par l'utilisateur est égal au nombre mystère, alors le joueur gagne la partie.

Dans le cas d'une victoire, vous devez indiquer au joueur combien d'essais ont été nécessaires pour gagner.

Si le joueur ne trouve pas le nombre mystère avec les 5 essais disponibles, il perd la partie.

[https://raw.githubusercontent.com/techmindconsulting/workshop-python/main/tp-1-guess-number/main.py](Récupérer le fichier à compléter)

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