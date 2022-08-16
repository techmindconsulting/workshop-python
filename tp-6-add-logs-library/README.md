# TP 6 - Gestion des logs

[Retour](../README.md)

## Démo 

### Generator

[Simple generator](https://gist.github.com/techmindconsulting/d3950b2b4614465cc8b91573657c2145)

[CSV generator](https://gist.github.com/techmindconsulting/70b319e6ce943f913078ffbe7997579a)

### Décorateur

[Decorator sans @](https://gist.github.com/techmindconsulting/8af19d6d5444eb1d8d35799f11f09aac)

[Decarateur avec @](https://gist.github.com/techmindconsulting/62bfa814b0a01a46c4cb325b1420344a)

**Dans vos programmes, toujours utiliser le decorateur avec le @**


## Présentation

Dans ce projet, vous allez devoir ajouter un fichier de log afin de tracer votre application à chaque appel de fonction. 
Vous allez devoir dans centraliser votre logique dans une fonction decorateuR et decorer toutes les fonctions de votre programme.

Le fichier de log `app.log` doit se trouver dans un repertoire log à la racine du projet
Le programme se chargera de créer le repertoire s'il n'existe pas.

Le niveau de log doit être INFO

Exemple d'une ligne de log

```
[2022-08-16 21:26:15] INFO: Appel de la fonction `search`
```

## Notions techniques à appliquer

- Decorator
- Module OS
- Module log 

```
import logging

logging.basicConfig(
    filename='myapp.log', 
    format='[%(asctime)s] %(levelname)s: %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    level=logging.INFO)


for name in ['John', 'Jack', 'Nicole', 'Samy', 'Sofy']:
    logging.info(f'Hello, world {name}!')
```


## Description

Au démarrage de l'application je dois pouvoir charger le CSV, nous pourrons le vérifier via la fonction "Afficher les livres"

Je dois pouvoir sauvegarder le fichier lorsque je quitte normalement le programme en passant par le menu

Je dois pouvoir sauvegarder lorsque l'erreur KeyboardInterrupt est intercepté


## Documentation
- [Logger dans un fichier](https://docs.python.org/fr/3/howto/logging.html#logging-to-a-file)
- [Afficher l'horodatage dans les messages] (https://docs.python.org/fr/3/howto/logging.html#displaying-the-date-time-in-messages)
- [Journalisatiopn](https://docs.python.org/fr/3/tutorial/stdlib2.html#logging)
- [Decorator](https://book.pythontips.com/en/latest/decorators.html#writing-your-first-decorator)
- [Geneartor](https://docs.python.org/fr/3/tutorial/classes.html#generators)

[Retour](../README.md)
