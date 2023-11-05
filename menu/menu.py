import math

import pygame

from assets.fonts_generator import get_police_menu

largeur_ecran = 1280
hauteur_ecran = 720

pygame.init()
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Nerd shooter")
running = True

# Initialisation de variables de couleurs
ORANGE = (255, 127, 0)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
INDIGO = (75, 0, 130)
GRIS = (211, 211, 211)
BLANC = (255, 255, 255)

margin_title = round(hauteur_ecran*0.1)
CENTER_X = largeur_ecran//2
HAUTEUR_BLOC_MENU = (hauteur_ecran - hauteur_ecran*0.2 - hauteur_ecran*0.1)
SCREEN_SLICE_VALUE = 0.17

# Création du titre
titre = get_police_menu(64).render("Nerd shooter", True, BLANC)
# xC = (xA + xB) / 2 ; yC = (yA + yB)/2 ==> centre d'un rectangle
position_titre = (largeur_ecran / 2, (hauteur_ecran * 0.2) / 2)
titre_rect = titre.get_rect(center=position_titre)

menu_labels = ["Démarrer", "Options", "High scores", "Quitter"]
display_menu = {}
position_temp = (position_titre[0], position_titre[1]+margin_title)
hovered_labels = list()

for i in range(len(menu_labels)):
    name_temp = get_police_menu(40).render(menu_labels[i], True, BLANC)
    name_hovered = get_police_menu(40).render(menu_labels[i], True, ORANGE)
    position_temp = (CENTER_X, (position_temp[1]+(HAUTEUR_BLOC_MENU*SCREEN_SLICE_VALUE)))
    temp_rect = name_temp.get_rect(center=position_temp)
    display_menu.update({i: (name_temp, temp_rect, menu_labels[i])})
    hovered_labels.append(name_hovered)

# demarrer = get_police(40).render("Démarrer", True, BLANC)
# position_demarrer = (CENTER_X, (position_titre[1]+margin_title+(HAUTEUR_BLOC_MENU*0.17)))
# demarrer_rect = demarrer.get_rect(center=position_demarrer)
#
# options = get_police(40).render("Options", True, BLANC)
# position_options = (CENTER_X, (position_demarrer[1]+(HAUTEUR_BLOC_MENU*0.17)))
# options_rect = options.get_rect(center=position_options)
#
# hiscores = get_police(40).render("High scores", True, BLANC)
# position_hiscores = (CENTER_X, (position_options[1] + (HAUTEUR_BLOC_MENU * 0.17)))
# hiscores_rect = hiscores.get_rect(center=position_hiscores)
#
# exit_game = get_police(40).render("Quitter", True, BLANC)
# position_exit_game = (CENTER_X, (position_hiscores[1] + (HAUTEUR_BLOC_MENU*0.17)))
# exit_game_rect = exit_game.get_rect(center=position_exit_game)


while running:
    MOUSE_POS = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if display_menu[0][1].collidepoint(event.pos):
                play()
            if display_menu[1][1].collidepoint(event.pos):
                options()
            if display_menu[2][1].collidepoint(event.pos):
                hiscores()
            if display_menu[3][1].collidepoint(event.pos):
                pygame.quit()

    screen.fill(NOIR)
    screen.blit(titre, titre_rect)
    j = 0
    for items in display_menu.values():
        if items[1].collidepoint(MOUSE_POS):
            screen.blit(hovered_labels[j], items[1])
        else:
            screen.blit(items[0], items[1])
        j += 1

    pygame.display.flip()

pygame.quit()
