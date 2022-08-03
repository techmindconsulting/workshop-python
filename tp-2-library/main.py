MENU_OPTIONS = {
    1: 'Ajouter un livre',
    2: 'Retirer un livre',
    3: 'Afficher les livres',
    4: 'Afficher le nombre de livre',
    5: 'Modifier le prix d\'un livre',
    6: 'Modifier la quantité d\'un livre',
    7: 'Quitter'
}


def add_book():
    pass


def remove_book():
    pass


def show_books():
    pass


def show_nb_books():
    pass


def update(field):
    pass


def run_option(option):
    print(f"{MENU_OPTIONS[option]}")
    match option:
        case 1:
            add_book()
        case 2:
            remove_book()
        case 3:
            show_books()
        case 4:
            show_nb_books()
        case 5:
            update(field="price")
        case 6:
            update(field="quantity")
        case 7:
            exit()


# Le tableau il faudra ajouter vos livres, ça sera un tableau de dictionnaire
library = []
book = {"title": "Les misérables", "price": 10, "quantity": 10}
library.append(book)  # Ajout d'un premier livre


def start():
    while True:
        show_options()
        run_option(int(input('Merci de saisir une option: ')))


def show_options():
    print('Bienvenue dans l\'application de gestion de librairie')
    # Compléter la fonction en faisant une boucle for sur MENU_OPTIONS
    for key in range(1, 7):
        print(f'[{key}] - Afficher un livre')  # A remplacer


start()
