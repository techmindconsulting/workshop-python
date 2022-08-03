import random


MIN = 1
MAX = 100
NB_ATTEMPTS = 5


def ask_number(nb_min, nb_max):
    while True:
        try:
            user_number = int(input('Saisir un nombre un nombre entre {} et {} : '.format(MIN, MAX)))
        except Exception:
            print('Merci de saisir un nombre entre {} et {}'.format(nb_min, nb_max))
        else:
            if nb_min <= user_number <= nb_max:
                return user_number


random_number = random.randint(MIN, MAX)
nb_trial = 0
while True:
    nb_trial += 1
    user_input = ask_number(MIN, MAX)
    if random_number == user_input:
        print('Trouvé au bout de {} tentative(s)'.format(nb_trial))
        break
    elif user_input > random_number:
        print('Trop  grand')
    else:
        print('Trop petit')

    if nb_trial >= NB_ATTEMPTS:
        print('Perdu, Le nombre aléatoire était {}'.format(random_number))
        break
