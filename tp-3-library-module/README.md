# TP 3 - Modulaiser l'application de gestion de librairie

[Retour](../README.md)

## Présentation

Dans ce projet, vous allez devoir rendre modulaire le projet précédent en proposant une arboresence avec paquets et/ou modules ce qui vous semple le plus cohérent, 
vous devez aussi respecter les standards pep8 en installant la paquet flake8 dans un environnement virtuelles.


![Arboresence](https://files.realpython.com/media/pkg2.dab97c2f9c58.png)


## Notions techniques à appliquer

- Paquet
- Module
- Environnement virtuel
- Gestioinnaire de paquet https://pypi.org/

## Description

1. Créer un environnement virtuel
```
 python -m venv .env
```

2. Activer l'environnement virtuel

[Windows] 
```
source .env/Scripts/activate
```

[Linux] 
```
source .env/bin/activate 
```

3. Installer flake8
```
pip install flake8
```

4. Créer un fichier de configuration à la racine du projet .flake8 et placez y la configuration suivante
```
[flake8]
exclude =
 .git,
 .gitignore,
 *.pot,
 *.py[co]
 __pycache__,
 env,
 .env

max-line-length = 120
```
Pour executer flake8

```
flake8 .
```
ou
```
python -m flake8 .
```

5. Stocker vos dépendances dans le fichier requirements.txt
```
pip freeze > requirements.txt
```

## Exemple projet utilsant des paquets et module
- https://github.com/sfinx13/scaffolder_dirs_accounting
- https://github.com/sfinx13/fundraising-webscrapper
- https://github.com/sfinx13/demo-poo-python


## Documentation
- [Les modules en détail](https://docs.python.org/fr/3/tutorial/modules.html#more-on-modules)
- [Les paquets](https://docs.python.org/fr/3/tutorial/modules.html#packages)
- [Environnement virtuels et paquets](https://docs.python.org/fr/3/tutorial/venv.html?highlight=pip)
- [Spécification PEP8](https://peps.python.org/pep-0008/)


[Retour](../README.md)
