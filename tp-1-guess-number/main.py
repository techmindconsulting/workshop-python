import random

random_number = random.randint(1, 10)
user_number = input('Saisir un nombre :')
user_number = int(user_number)
while True:
    if random_number == user_number:
        print('Trouvé')
        break
    else:
        user_number = input('Saisir un nombre :')
        user_number = int(user_number)
