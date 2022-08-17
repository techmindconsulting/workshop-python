import random


NB_MIN_RANDOM = 1
NB_MAX_RANDOM = 100
NB_ATTEMPTS = 5

nb_trial = 0


def ask_number(nb_min, nb_max):
    while True:
        try:
            global nb_trial
            nb_trial += 1
            print('Essai n°{} - '.format(nb_trial), end='')
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
            if nb_trial >= NB_ATTEMPTS:
                return 0
        else:
            if nb_min <= user_number <= nb_max:
                return user_number


nb_random = random.randint(NB_MIN_RANDOM, NB_MAX_RANDOM)
nb_min_random = NB_MIN_RANDOM
nb_max_random = NB_MAX_RANDOM

while nb_trial < NB_ATTEMPTS:
    nb_user_input = ask_number(nb_min_random, nb_max_random)
    if nb_random == nb_user_input:
        print('Trouvé au bout de {} tentative(s)'.format(nb_trial))
        break
    elif nb_user_input > nb_random:
        nb_max_random = nb_user_input
        print('{} est trop grand'.format(nb_user_input))
    else:
        print('{} est trop petit'.format(nb_user_input))
        nb_min_random = nb_user_input

    if nb_trial >= NB_ATTEMPTS:
        print('Perdu, Le nombre aléatoire était {}'.format(nb_random))
        break
