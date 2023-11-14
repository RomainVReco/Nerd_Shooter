import pygame
from assets.fonts_generator import get_police_menu


def ask_name_components(largeur_ecran, hauteur_ecran, color):
    CENTER_X = largeur_ecran // 2
    CENTER_Y = hauteur_ecran // 2.5
    list_name_components = list()
    # Création du titre
    text_endgame = get_police_menu(40).render(f"Toutes les cibles ont ete detruites !", True, color)
    text_endgame_rect = text_endgame.get_rect(center=(CENTER_X, CENTER_Y))
    list_name_components.append([text_endgame, text_endgame_rect])

    text_score = get_police_menu(40).render('Score : ', True, color)
    top_endgame = text_endgame_rect.top
    top_endgame += text_endgame_rect.height
    left_endgame = text_endgame_rect.left
    text_score_rect = text_score.get_rect(topleft=(left_endgame, top_endgame))
    list_name_components.append([text_score, text_score_rect])

    text_nom = get_police_menu(40).render("Votre nom : ", True, color)
    top_score = text_score_rect.top
    top_score += text_score_rect.height
    left_score = text_score_rect.left
    text_nom_rect = text_nom.get_rect(topleft=(left_score, top_score))
    list_name_components.append([text_nom, text_nom_rect])

    left_nom = left_score + text_nom_rect.width
    input_text = get_police_menu(40).render('', True, color)
    input_box = pygame.Rect(left_nom, top_score, 390, 44)
    list_name_components.append([input_text, input_box])
    return list_name_components
