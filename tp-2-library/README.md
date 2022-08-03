# TP 2 - Gestion d'une librarie

[Retour](../README.md)

## Correction
[Cliquer pour voir une correction](https://github.com/techmindconsulting/workshop-python/blob/correction/tp-2-library/main.py)


Dans ce projet, vous allez devoir créer un programme en ligne de commande qui permet de manipuler une liste de livres.


Notions techniques à appliquer


- Affichage avec les chaines formatés (f-string => {})
- Saisie utilisateurs
- Les conditions
- Les boucles
- Manipuler une liste
- Manipuler un dictionnaire
- Les fonctions
- La gestions des erreurs

Description
Par définition, dans notre programme library.py un livre est défini par son titre, son prix et le nombre de livre en stock

Exemple:
```
# Titre = Les misérables  
# Prix = 10€
book = {"title": "Les misérables", "price": 10, "quantity": 10}
```

Le programme doit permettre de réaliser 6 actions  et doit être organiser sous forme de fonction
1. Ajouter un livre à la librairie
2. Retirer un livre à la librairie
3. Afficher les livres de la librairie
4. Afficher le nombre de livre
5. Modifier le prix d'un livre
6. Modifier le stock du livre
7. Quitter le programme

Voici la programme principale  
```
MENU_OPTIONS = { 
    1: 'Ajouter un livre', 
    2: 'Retirer un livre', 
    3: 'Afficher les livres', 
    4: 'Afficher le nombre de livre'
    4: 'Modifier le prix d\'un livre', 
    5: 'Modifier la quantité d\'un livre', 
    6: 'Quitter' 
}

# Le tableau il faudra ajouter vos livres, ça sera un tableau de dictionnaire 
library = [] 
book = {"title": "Les misérables", "price": 10, "quantity": 10} 
library.append(book)  # Ajout d'un premier livre 
def start(): 
    while(True): 
        show_options() 
        run_option(int(input('Merci de saisir une option: ')))
```

[A compléter] La fonction show_options doit permettre d'afficher le numéro et le titre de l'option à l'aide d'une boucle 
Le menu est défini dans la constante MENU_OPTIONS

```
def show_options(): 
    print('Bienvenue dans l\'application de gestion de librairie') 
    # Compléter la fonction en faisant une boucle for sur MENU_OPTIONS 
    for key in range(1, 7): 
        print(f'[{key}] - Afficher un livre')  # A remplacer
```


[A compléter] La fonction run_option permet d'exécuter la fonction voulue grâce au numéro saisi
Vous devez donc demander à l'utilisateur de choisir parmi une de ces actions en entrant un nombre de 1 à 6.
Vous devez gérer le cas de figure où l'utilisateur ne rentre pas un nombre compris entre 1 et 6 ou s'il rentre par exemple des lettres ou un autre symbole invalide. 
```
def run_option(option): 
    print(f"{MENU_OPTIONS[option]}") 
    match option: 
        case 1: 
            add_book()  # Ajout de livre 
        case 2: 
            remove_book()  # Suppression de livre 
        case 3: 
            show_books()  # Affichage de livre 
        case 4: 
            update(field="price")  # Mise à jour prix 
        case 5: 
            update(field="quantity")  # Mise à jour quantité 
        case 6: 
            exit()  # Sortir du programme
```

Remarque: Nous allons plutôt privilégier l'instruction match case  pour conditionner les traitement au lieu d'une longue liste de 
```
if condition: 
    instruction 
elif condition: 
    instruction
elif condition:  
    instruction
elif condition:  
    instruction 
else: 
    instruction
```

En cas d'erreur de saisie vous devez afficher de nouveau le menu avec les options disponibles, jusqu'à ce que l'utilisateur choisisse une option valide.

Le but ici est juste d'interagir avec l'utilisateur et de manipuler une liste de dictionnaire en fonction de son choix.

[A compléter]  Ecrire les fonctions pour chacune des actions
```
def add_book():
    pass

def remove_book():
    pass

def show_books():
    pass

def update(field):
    pass

```

Pour le programme puisse se lancer, il faudra appeler la fonction start
```
start()
```

## Documentation
- [L'instruction pass](https://docs.python.org/fr/3/tutorial/controlflow.html#pass-statements)

- [L'instruction match](https://docs.python.org/fr/3/tutorial/controlflow.html#match-statements)

- [Listes](https://docs.python.org/fr/3/tutorial/introduction.html#lists)

- [Compléments sur les listes](https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists)

- [Liste en compréhension](https://docs.python.org/fr/3/tutorial/datastructures.html#list-comprehensions)

- [L'instruction del](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement)

- [Dictionnaires](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries)

- [L'instruction for](https://docs.python.org/fr/3/tutorial/controlflow.html#for-statements)

- [Techiques de boucles](https://docs.python.org/fr/3/tutorial/datastructures.html#looping-techniques)

- [Valeur par défaut des arguments](https://docs.python.org/fr/3/tutorial/controlflow.html#default-argument-values)

- [Les arguments nommé](https://docs.python.org/fr/3/tutorial/controlflow.html#keyword-arguments)

- [Fonctions anonymes](https://docs.python.org/fr/3/tutorial/controlflow.html#lambda-expressions)

- [Chaines de documentation](https://docs.python.org/fr/3/tutorial/controlflow.html#documentation-strings)


[Retour](../README.md)