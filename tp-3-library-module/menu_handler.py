import manager.book as book

MENU_OPTIONS = {
    1: 'Ajouter un livre',
    2: 'Retirer un livre',
    3: 'Afficher les livres',
    4: 'Afficher le nombre de livre',
    5: 'Modifier le prix d\'un livre',
    6: 'Modifier la quantité d\'un livre',
    7: 'Quitter',
}

SEPARATOR = '*'


def run_option(option):
    """
    Execute la fonctionnalité selon le choix de l'utilisateur
    """
    if option not in range(1, len(MENU_OPTIONS) + 1):
        raise ValueError('Merci de saisir une option valide')

    print(SEPARATOR * 60)
    print(f'[{option}] - {MENU_OPTIONS[option].upper()}')
    print(SEPARATOR * 60)

    match option:
        case 1:
            book.add_book()
        case 2:
            book.remove_book()
        case 3:
            book.show_books()
        case 4:
            book.show_nb_books()
        case 5:
            book.update_book(field='price')
        case 6:
            book.update_book(field='quantity')
        case 7:
            raise KeyboardInterrupt


def show_options():
    """
    Affiche les options de l'application
    """
    print(60 * SEPARATOR)
    print('Bienvenue dans l\'application de gestion de librairie')
    for key in range(1, len(MENU_OPTIONS) + 1):
        print(f'[{key}] - {MENU_OPTIONS[key]}')
    print(60 * SEPARATOR)
