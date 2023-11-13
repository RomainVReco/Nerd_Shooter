import random

from assets.fonts_generator import get_police_vanilla


def interger_generator(integer, number_of_target, font_size, COLOR, number_of_decoy, is_hexa):
    set_pair = set()
    while len(set_pair) < number_of_target:
        entier = random.randrange(integer, 150, integer)
        if is_hexa:
            entier = hex(entier)
        set_pair.add(entier)

    # On transforme le set en list, pour accéder aux valeurs plus facilement
    list_pair = list(set_pair)
    list_msg = list()

    # Les multiples sont transformés en message affichable à l'écran
    for i in range(len(list_pair)):
        list_msg.append(get_police_vanilla(font_size).render(str(list_pair[i]), True, COLOR))

    # Création des nombres des leurres, ici multiples de 3
    challenge_integer = integer
    while challenge_integer % integer == 0:
        challenge_integer = random.randint(2, 21)

    set_decoy = set()
    while len(set_decoy) < number_of_decoy:
        # Pose problème car si CHallenge_integer = 21 alors pas assez de choix pour ajouter des leurres
        # Il faut modifier l'amplitude de challenge_integer
        entier_decoy = random.randrange(challenge_integer, 250, challenge_integer)
        if entier_decoy % challenge_integer == 0 and entier_decoy % integer != 0:
            if is_hexa:
                entier_decoy = hex(entier_decoy)
            set_decoy.add(entier_decoy)

    list_decoy = list(set_decoy)
    list_msg_decoy = list()

    for i in range(len(list_decoy)):
        list_msg_decoy.append(get_police_vanilla(font_size).render(str(list_decoy[i]), True, COLOR))

    return list_msg, list_msg_decoy


def set_difficulty(integer, is_hexa):
    while integer not in ("2", "3", "4", "5", "6", "7", "8", "9"):
        integer = str(input("De quel chiffre voules-vous dégommer les multiples ? 2-9 \n")).strip()
    integer = int(integer)

    while is_hexa not in ("0", "1"):
        is_hexa = str((input("Difficile ? 0-1 \n")))
    is_hexa = bool(int(is_hexa))

    return integer, is_hexa
