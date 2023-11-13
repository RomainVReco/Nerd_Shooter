import pygame

from assets.fonts_generator import get_police_menu
from levels.selection_difficulte import select_difficulty
from score.scores_functions import load_score_data, get_score_elements


def menu(largeur_ecran, hauteur_ecran):
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
    HAUTEUR_BLOC_MENU = (hauteur_ecran - hauteur_ecran * 0.2 - hauteur_ecran * 0.1)
    SCREEN_SLICE_VALUE = 0.17

    police = get_police_menu(80)
    # Création du titre
    titre = police.render("Nerd shooter", True, BLANC)
    # xC = (xA + xB) / 2 ; yC = (yA + yB)/2 ==> centre d'un rectangle
    position_titre = (largeur_ecran / 2, (hauteur_ecran * 0.2) / 2)
    titre_rect = titre.get_rect(center=position_titre)

    menu_labels = ["Demarrer", "High scores", "Quitter"]
    display_menu = {}
    position_temp = (position_titre[0], position_titre[1] + margin_title)
    hovered_labels = list()

    for i in range(len(menu_labels)):
        name_temp = police.render(menu_labels[i], True, BLANC)
        name_hovered = police.render(menu_labels[i], True, ORANGE)
        position_temp = (CENTER_X, (position_temp[1] + (HAUTEUR_BLOC_MENU * SCREEN_SLICE_VALUE)))
        temp_rect = name_temp.get_rect(center=position_temp)
        display_menu.update({i: (name_temp, temp_rect, menu_labels[i])})
        hovered_labels.append(name_hovered)

    print(display_menu)
    while running:
        MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if display_menu[0][1].collidepoint(event.pos):
                    select_difficulty(largeur_ecran, hauteur_ecran, screen)
                # if display_menu[1][1].collidepoint(event.pos):
                #     options()
                if display_menu[1][1].collidepoint(event.pos):
                    score_display(largeur_ecran, hauteur_ecran, screen)
                if display_menu[2][1].collidepoint(event.pos):
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


def score_display(largeur_ecran, hauteur_ecran, screen):
    running = True

    # Initialisation de variables de couleurs
    ORANGE = (255, 127, 0)
    NOIR = (0, 0, 0)
    BLANC = (255, 255, 255)

    display_score_titles = {}
    hovered_labels = []
    score_titre = ["Hall of Fame", "Hall of Shame"]
    position_titre = [(largeur_ecran // 2, round(hauteur_ecran * 0.083)),
                      (largeur_ecran // 2, round(hauteur_ecran * 0.5385))]
    print(position_titre)
    police = get_police_menu(40)

    # Création bouton retour:
    retour = get_police_menu(50).render("Retour", True, BLANC)
    retour_rect = retour.get_rect(center=(150, round(hauteur_ecran * 0.083)))
    retour_hovered = get_police_menu(50).render("Retour", True, ORANGE)

    # Création de deux rectangles contenant les titres
    for i in range(len(score_titre)):
        name_temp = get_police_menu(50).render(score_titre[i], True, BLANC)
        name_hovered = get_police_menu(50).render(score_titre[i], True, ORANGE)
        temp_rect = name_temp.get_rect(center=position_titre[i])
        display_score_titles.update({i: (name_temp, temp_rect, score_titre[i])})
        hovered_labels.append(name_hovered)

    scores_type = load_score_data()
    data_key = list(scores_type.keys())
    scores_type_display = []
    hiscores = {}
    lowscores = {}
    initial_position_elements = (
        [round(largeur_ecran * 0.25), round(hauteur_ecran * 0.15)], [round(largeur_ecran * 0.25),
                                                                     round(hauteur_ecran * 0.61)])
    for j in range(len(data_key)):
        print("élément de data key[j]", data_key[j])
        print("élément de initial position[j]", initial_position_elements[j])
        temp_scores = get_score_elements(scores_type, data_key[j], initial_position_elements[j], police, BLANC)
        scores_type_display.append(temp_scores)

    hiscores, lowscores = scores_type_display

    while running:
        MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour_rect.collidepoint(MOUSE_POS):
                    menu(largeur_ecran, hauteur_ecran)

        screen.fill(NOIR)
        screen.blit(retour, retour_rect)
        pygame.draw.rect(screen, BLANC, retour_rect, 1)
        if retour_rect.collidepoint(MOUSE_POS):
            screen.blit(retour_hovered, retour_rect)
            pygame.draw.rect(screen, ORANGE, retour_rect, 1)

        for display in display_score_titles.values():
            screen.blit(display[0], display[1])
        k = 0
        for items in display_score_titles.values():
            if items[1].collidepoint(MOUSE_POS):
                screen.blit(hovered_labels[k], items[1])
            else:
                screen.blit(items[0], items[1])
            k += 1

        for score in hiscores.values():
            screen.blit(score[0][0], score[0][1])
            screen.blit(score[1][0], score[1][1])
            screen.blit(score[2][0], score[2][1])

        for score in lowscores.values():
            screen.blit(score[0][0], score[0][1])
            screen.blit(score[1][0], score[1][1])
            screen.blit(score[2][0], score[2][1])

        pygame.display.flip()

    pygame.quit()
