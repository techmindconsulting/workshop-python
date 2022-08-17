import random


NB_MIN_RANDOM = 1
NB_MAX_RANDOM = 100
NB_ATTEMPTS = 5

nb_trial = 0


def ask_number(nb_min, nb_max):
    try:
        user_number = int(
            input('Saisir un nombre un nombre entre {} et {} : '.format(
                nb_min,
                nb_max)
            )
        )
    except Exception:
        print('Merci de saisir un nombre entre {} et {}'.format(
            nb_min,
            nb_max)
        )
        user_number = 0
    finally:
        return user_number


nb_random = random.randint(NB_MIN_RANDOM, NB_MAX_RANDOM)
nb_min_random = NB_MIN_RANDOM
nb_max_random = NB_MAX_RANDOM

while nb_trial < NB_ATTEMPTS:
    nb_trial += 1
    print('Essai n°{} - '.format(nb_trial), end='')
    nb_user_input = ask_number(nb_min_random, nb_max_random)
    if nb_random == nb_user_input:
        print('GAGNE :D! Trouvé au bout de {} tentative(s)'.format(nb_trial))
        break
    elif nb_user_input > nb_random:
        nb_max_random = nb_user_input if nb_user_input <= nb_max_random else nb_max_random
        print('{} est trop grand'.format(nb_user_input))
    else:
        print('{} est trop petit'.format(nb_user_input))
        nb_min_random = nb_user_input if nb_user_input != 0 else 1

    if nb_trial >= NB_ATTEMPTS:
        print('PERDU :(! Le nombre aléatoire était {}'.format(nb_random))
        break
