import pygame.font

largeur_ecran = 1280
hauteur_ecran = 720

pygame.init()
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Nerd shooter")
running = True


def get_police_difficulte(font_size):
    return pygame.font.Font("OptimusPrincepsSemiBold.ttf", font_size)