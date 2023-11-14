from time import sleep

import pygame

from HUD.hud_bar import generate_hud, draw_hud
from Sons.sound_effects import get_piou_sound, get_boum_sound, finish_sound
from assets.fonts_generator import get_police_menu
from assets.game_generator import get_random_rect_template, get_object_dictionnary
from integer_hexa_generator import interger_generator
from movements import target_movements, decoy_movements
from score.scores_functions import check_score_type


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


def launch_game(difficulty, largeur_ecran, hauteur_ecran, screen):
    integer, number_of_target, number_of_decoy, number_of_horizontal, is_hexa = difficulty
    clock = pygame.time.Clock()
    pygame.init()
    running = True
    dt = 0
    FONT_SIZE = 32

    # Initialisation de variables de couleurs
    ORANGE = (255, 127, 0)
    NOIR = (0, 0, 0)
    BLEU = (0, 0, 255)
    INDIGO = (75, 0, 130)
    GRIS = (211, 211, 211)
    BLANC = (255, 255, 255)

    # Framerate et vitesse des objets
    FPS = 30
    SPEED_X = round(60 // FPS)
    SPEED_Y = round(90 // FPS)
    i = 0
    j = 0

    # Position initiale de la cible
    target_x_cible, target_y_cible = largeur_ecran // 2, hauteur_ecran // 2
    # Pour cacher le curseur de la souris
    pygame.mouse.set_visible(False)

    decoy_hit = 0
    score = 0
    list_of_onscreen_items = [number_of_target, decoy_hit, score]
    list_speeds_target = [(SPEED_X, round(SPEED_Y * 1.1, 1)), (SPEED_X * 2, SPEED_Y * 1.5), (-SPEED_X * 4, SPEED_Y),
                          (-SPEED_X * 2, SPEED_Y)]
    list_speeds_decoy = [(SPEED_X * 2, round(SPEED_Y * 1.2, 1)), (SPEED_X * 2.2, SPEED_Y * 1.5),
                         (-SPEED_X * 3, SPEED_Y * 1.45), (-SPEED_X * 2, SPEED_Y)]

    # En fonction de la difficulté, défini les variables de variation du score
    if is_hexa:
        SCORE_INCREMENT = 500
        SCORE_DECREMENT = 100
    else:
        SCORE_INCREMENT = 200
        SCORE_DECREMENT = 75

    # Variable utilisée pour ne pas supprimer une donnée pendant le parcours du dictionnaire
    key_to_remove = None

    # Création des nombres à cliquer. Utilisation d'un set pour garantir l'absence de doublon
    # et création des nombres des leurres
    target_numbers, decoy_numbers = interger_generator(integer, number_of_target, FONT_SIZE, NOIR, number_of_decoy,
                                                       is_hexa)

    # Création des supports des cibles
    target_list = get_random_rect_template(number_of_target, largeur_ecran, FONT_SIZE)

    # Création du dictionnairte des cibles, contenu et contenant
    dictionnary_of_target = get_object_dictionnary(target_list, target_numbers, list_speeds_target)

    # Création des supports des leurres
    decoy_list = get_random_rect_template(number_of_decoy, largeur_ecran, FONT_SIZE)

    # Création du dictionnairte des leuures, contenu et contenant
    dictionnary_of_decoy = get_object_dictionnary(decoy_list, decoy_numbers, list_speeds_decoy)

    HUD = generate_hud(largeur_ecran, hauteur_ecran, NOIR)

    list_name_components = ask_name_components(largeur_ecran, hauteur_ecran, BLANC)

    nom = ''
    endgame = False

    while running:
        screen.fill(ORANGE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                target_x_cible, target_y_cible = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                get_piou_sound()
                for dicK, dicV in dictionnary_of_target.items():
                    if dicV[0].collidepoint(event.pos):
                        key_to_remove = dicK
                        score += SCORE_INCREMENT
                        get_boum_sound()
                        number_of_target -= 1
                        list_of_onscreen_items[0], list_of_onscreen_items[2] = number_of_target, score
                for decoy_key, decoy_values in dictionnary_of_decoy.items():
                    if decoy_values[0].collidepoint(event.pos):
                        score -= SCORE_DECREMENT
                        decoy_hit += 1
                        list_of_onscreen_items[1], list_of_onscreen_items[2] = decoy_hit, score
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nom = nom[:-1]
                elif event.key == pygame.K_RETURN:
                    check_score_type(score, nom)
                    break
                else:
                    if len(nom) == 20:
                        break
                    else:
                        nom += event.unicode

        if key_to_remove is not None:
            dictionnary_of_target.pop(key_to_remove)
            key_to_remove = None

        # Création des CIBLES sur leur support
        dictionnary_of_target = target_movements(dictionnary_of_target, screen, largeur_ecran, FONT_SIZE,
                                                 hauteur_ecran).copy()

        # Création des LEURRES sur leur support
        dictionnary_of_decoy = decoy_movements(dictionnary_of_decoy, screen, largeur_ecran, FONT_SIZE,
                                               hauteur_ecran).copy()

        if len(dictionnary_of_target.keys()) == 0:
            sleep(0.5)
            if not endgame:
                finish_sound()
            endgame = True
            # Ecran d'affichage des scores
            score_text = f'Score : {score}'
            text_surface = get_police_menu(40).render(nom, True, BLANC)
            score_surface = get_police_menu(40).render(score_text, True, BLANC)
            list_name_components[3][0] = text_surface
            list_name_components[1][0] = score_surface
            screen.fill(NOIR)
            for detail in list_name_components:
                screen.blit(detail[0], detail[1])
            # sleep(1.0)
            # pygame.quit()

        # Dessin du réticule de visée
        pygame.draw.circle(screen, (0, 0, 0), (target_x_cible, target_y_cible), 16, 2)
        pygame.draw.line(screen, (0, 0, 0), (target_x_cible - 1, target_y_cible - 14),
                         (target_x_cible - 1, target_y_cible + 14), 2)
        pygame.draw.line(screen, (0, 0, 0), (target_x_cible - 14, target_y_cible - 1),
                         (target_x_cible + 14, target_y_cible - 1), 2)

        # Dessin du HUD
        draw_hud(screen, GRIS, HUD, list_of_onscreen_items, NOIR)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
