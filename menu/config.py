import pygame

from score.score_display import menu

largeur_ecran = 1280
hauteur_ecran = 720


def get_largeur_ecran():
    return largeur_ecran


def get_hauteur_ecran():
    return hauteur_ecran


pygame.init()
menu(largeur_ecran, hauteur_ecran)
