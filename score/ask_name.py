import pygame

from assets.fonts_generator import get_police_menu
from config import get_largeur_ecran, get_hauteur_ecran

largeur_ecran = get_largeur_ecran()
hauteur_ecran = get_hauteur_ecran()

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

margin_title = round(hauteur_ecran * 0.1)
CENTER_X = largeur_ecran // 2
CENTER_Y = hauteur_ecran // 2.5
score = 0


def ask_name_components(largeur_ecran, hauteur_ecran, score):
    CENTER_X = largeur_ecran // 2
    CENTER_Y = hauteur_ecran // 2.5
    list_name_components = list()
    # Création du titre
    text_endgame = get_police_menu(40).render(f"Toutes les cibles ont ete detruites !", True, BLANC)
    text_endgame_rect = text_endgame.get_rect(center=(CENTER_X, CENTER_Y))
    list_name_components.append([text_endgame, text_endgame_rect])

    text_score = get_police_menu(40).render(f'Score : {score}', True, BLANC)
    top_endgame = text_endgame_rect.top
    top_endgame += text_endgame_rect.height
    left_endgame = text_endgame_rect.left
    text_score_rect = text_score.get_rect(topleft=(left_endgame, top_endgame))
    list_name_components.append([text_score, text_score_rect])

    text_nom = get_police_menu(40).render("Votre nom : ", True, BLANC)
    top_score = text_score_rect.top
    top_score += text_score_rect.height
    left_score = text_score_rect.left
    text_nom_rect = text_nom.get_rect(topleft=(left_score, top_score))
    list_name_components.append([text_nom, text_nom_rect])

    left_nom = left_score + text_nom_rect.width
    input_text = get_police_menu(40).render('', True, BLANC)
    input_box = pygame.Rect(left_nom, top_score, 390, 44)
    list_name_components.append([input_text, input_box])
    return list_name_components


list_name = ask_name_components(largeur_ecran, hauteur_ecran, score)

nom = ''

# while running:
#     MOUSE_POS = pygame.mouse.get_pos()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_BACKSPACE:
#                 nom = nom[:-1]
#             elif event.key == pygame.K_RETURN:
#                 check_score_type(score, nom)
#             else:
#                 if len(nom) == 20:
#                     break
#                 else:
#                     nom += event.unicode
#
#     text_surface = get_police_menu(40).render(nom, True, BLANC)
#     list_name[3][0] = text_surface
#     screen.fill(NOIR)
#     for detail in list_name:
#         screen.blit(detail[0], detail[1])
#
#     pygame.display.flip()
#
# pygame.quit()
