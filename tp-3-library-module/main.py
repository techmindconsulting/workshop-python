import menu_handler as menu


def start():
    """
    Démarre l'application
    """
    while True:
        menu.show_options()
        try:
            menu.run_option(int(input('Merci de saisir une option valide: ')))
        except KeyboardInterrupt:
            print('\nAurevoir...')
            exit()
        except ValueError:
            pass


start()
