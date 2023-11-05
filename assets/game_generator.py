import random

import pygame


# Création de manière aléatoire et sans chevauchement des aires des rectangles
# Ils peuvent servir de support à l'insertion d'image ou d'autres éléments
def get_random_rect_template(number_of_target, largeur_ecran, FONT_SIZE_GAME):
    object_list = set()
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

# def 