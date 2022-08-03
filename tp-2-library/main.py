MENU_OPTIONS = {
    1: 'Ajouter un livre',
    2: 'Retirer un livre',
    3: 'Afficher les livres',
    4: 'Afficher le nombre de livre',
    5: 'Modifier le prix d\'un livre',
    6: 'Modifier la quantité d\'un livre',
    7: 'Quitter',
}

PRICE = 'price'
QUANTITY = 'quantity'

FIELDS = {PRICE: 'prix', QUANTITY: 'quantité'}

SEPARATOR = '*'

library = []
book = {'title': 'Les misérables', 'price': 10, 'quantity': 10}
library.append(book)


def find_position_book(value):
    """
    Recherche la position du livre
    """
    for position, book in enumerate(library):
        if book["title"].lower() == value.lower():
            return position
    return None


def get_max_title_length():
    """
    Retourne la longueur du titre le plus long de la librairie
    """
    max_length = 0
    for book in library:
        if len(book["title"]) > max_length:
            max_length = len(book["title"])

    return max_length


def ask_title(message='Merci de saisir le titre: ', check_duplicated=False):
    """
    Demande à l'utilisateur de saisir un titre
    """
    if not check_duplicated:
        return input('Merci de saisir le titre: ')

    is_exists = True
    while is_exists:
        title = input('Merci de saisir le titre: ')
        is_exists = bool(
            [book for book in library if book["title"].lower() == title.lower()]
        )
        print('Livre existe déja' if is_exists else 'OK, merci de saisir les champs suivants')

    return title.capitalize()


def ask_price(message='Merci de saisir le prix: '):
    """
    Demande à l'utilisateur de saisir un prix
    """
    price = 0
    while True:
        try:
            while price <= 0:
                price = float(input(message))
                if price == 0:
                    print('Le prix doit être supérieur à 0€')
        except ValueError:
            print('Merci de saisir un réel prix')
        else:
            return price


def ask_quantity(message='Merci de saisir la quantité: '):
    """
    Demande à l'utilisateur de saisir une quantité
    """
    quantity = 0
    while True:
        try:
            while quantity <= 0:
                quantity = int(input(message))
                if quantity == 0:
                    print('La quantité doit être supérieur à 0')
        except ValueError:
            print('Merci de saisir une réelle quantité')
        else:
            return quantity


def ask_new_value(field):
    """
    Demande une nouvelle valeur à saisir pour le prix ou la quantité
    """
    value = 0
    while True:
        try:
            while value <= 0:
                message = 'la nouvelle' if field == QUANTITY else 'le nouveau'
                value = input(f'Merci de saisir {message} {FIELDS[field]}: ')
                value = float(value) if field == PRICE else int(value)
                if value == 0:
                    print(f'{message.capitalize()} {FIELDS[field]} doit être supérieur à 0')
        except ValueError:
            print(f'Merci de saisir une bonne valeur pour {FIELDS[field]}')
        else:
            return value


def add_book():
    """
    Ajoute un livre avec les champs suivants: titre, prix et la quantité
    """
    title = ask_title(check_duplicated=True)
    price = ask_price()
    quantity = ask_quantity()

    new_book = {'title': title, 'price': price, 'quantity': quantity}
    library.append(new_book)
    show_books()


def show_books():
    """
    Affiche les livres dans l'ordre alphabétique
    """
    show_nb_books()
    max_length = get_max_title_length()
    global library
    library = sorted(library, key=lambda book: book["title"])
    for key, book in enumerate(library):
        print('{} - {} || Prix: {:.2f}€ || Stock: {}'.format(
            key + 1,
            book["title"].ljust(max_length),
            book["price"],
            book["quantity"])
        )


def show_nb_books():
    nb_book = len(library)
    total_stock = 0
    print(f'{nb_book} {"ouvrages" if nb_book > 1 else "ouvrage" }')
    for book in library:
        total_stock += book["quantity"]

    print(
        f'{total_stock} {"livres en stock" if total_stock > 1 else "livre en stock" }'
    )


def update_book(field):
    """
    Met à jour le prix ou la quantité du livre
    """
    position = None

    while position is None:
        title = ask_title(message='Merci de saisir le film à mettre à jour')
        position = find_position_book(title)
        print('Livre introuvable' if position is None else 'Livre trouvé')

    value = ask_new_value(field)
    library[position][field] = value
    print(f'{FIELDS[field].capitalize()} du livre {title} a été mise à jour')
    show_books()


def remove_book():
    """
    Supprime un livre de l'application
    """
    global library
    position = None

    while position is None:
        title = ask_title(message='Merci de saisir le titre du livre à supprimer: ')
        position = find_position_book(title)
        print('Livre introuvable' if position is None else 'Livre trouvé')

    del library[position]
    print(f'{title} a été supprimé')
    show_books()


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
            add_book()
        case 2:
            remove_book()
        case 3:
            show_books()
        case 4:
            show_nb_books()
        case 5:
            update_book(field='price')
        case 6:
            update_book(field='quantity')
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


def start():
    """
    Démarre l'application
    """
    while True:
        show_options()
        try:
            run_option(int(input('Merci de saisir une option valide: ')))
        except KeyboardInterrupt:
            print('\nAurevoir...')
            exit()
        except ValueError:
            pass


start()
