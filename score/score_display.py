import pygame

from assets.fonts_generator import get_police_menu
from score.scores_functions import load_score_data, get_score_elements


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
