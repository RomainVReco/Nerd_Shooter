
import pygame


# Renvoie un objet Font pour le menu d'accueil, dont la taille peut être adaptée lors de l'appel
def get_police_menu(font_size):
    return pygame.font.Font("../assets/fonts/OptimusPrincepsSemiBold.ttf", font_size)


# Renvoie un objet Font pour la sélection de difficulté, dont la taille peut être adaptée lors de l'appel
def get_police_difficulte(font_size):
    return pygame.font.Font("../assets/fonts/OptimusPrincepsSemiBold.ttf", font_size)


# Renvoie un objet Font basique, dont la taille peut être adaptée lors de l'appel
def get_police_vanilla(font_size):
    return pygame.font.Font('freesansbold.ttf', font_size)
