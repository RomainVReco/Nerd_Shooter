import random

import pygame


# Création de manière aléatoire et sans chevauchement des aires des rectangles
def get_random_rect_template(number_of_target, largeur_ecran, FONT_SIZE_GAME):
    object_list = list()
    while len(object_list) < number_of_target:
        object_creation_process = pygame.Rect(random.randint(0, largeur_ecran - FONT_SIZE_GAME), 0, FONT_SIZE_GAME,
                                              FONT_SIZE_GAME)
        not_colliding = True
        for obj in object_list:
            if obj.colliderect(object_creation_process):
                not_colliding = False
        if not_colliding:
            object_list.append(object_creation_process)
    assert len(object_list) == number_of_target, ("La liste des rectangles est différente de ", number_of_target)
    return list(object_list)


# Boucle de création du dictionnaire pour placer les messages sur l'écran
def get_object_dictionnary(target_list, target_numbers, list_speeds_target) -> dict:
    j = 0
    dictionnary_of_target = {}
    for target in target_list:
        coordinates = target.topleft
        rect = target_numbers[j].get_rect()
        rect.topleft = coordinates
        speed_temp = list_speeds_target[random.randint(0, 3)]
        dictionnary_of_target.update({target_numbers[j]: [rect, 0, 0, speed_temp]})
        print(dictionnary_of_target)
        j += 1
    return dictionnary_of_target