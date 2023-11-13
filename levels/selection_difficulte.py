import pygame.font

from assets.fonts_generator import get_police_difficulte
from levels.game_engine import launch_game


# Affiche la page de sélection de la difficulté.
# La fonction contient également les paramètres de difficulté
def select_difficulty(largeur_ecran, hauteur_ecran, screen):
    running = True
    PATH_IMAGE = "../assets/img/"

    # Initialisation de variables de couleurs
    ORANGE = (255, 127, 0)
    NOIR = (0, 0, 0)
    BLEU = (0, 0, 255)
    INDIGO = (75, 0, 130)
    GRIS = (211, 211, 211)
    BLANC = (255, 255, 255)
    DARK_GREY = (169, 169, 169)

    # difficulté = (muliple à cibler, nombre de cibles, nombre de leurres, nombre d'obstacles, is_hexadecimal)
    EASY = (2, 5, 5, 0, False)
    NORMAL = (7, 10, 10, 1, False)
    HARD = (9, 10, 10, 3, True)

    titre_selection_difficulte = get_police_difficulte(80).render("Choisissez la difficulte : ", True, BLANC)
    position_titre_selection = (round(largeur_ecran*0.05), round(hauteur_ecran*0.06))
    titre_selection_rect = titre_selection_difficulte.get_rect(topleft=position_titre_selection)
    selection_labels = ["Facile", "Normal", "Difficile", "Personalisee"]
    selection_images = ["NervousWojak-70px.png", "wojak-70px.png", "rages_screaming-70px.png", "doomer_stage22v-70px.png"]
    display_selection = {}
    selection_labels_hovered = list()
    position_image_temp = (round(largeur_ecran*0.21), position_titre_selection[1])

    for i in range(len(selection_labels)):
        image_temp = pygame.image.load(PATH_IMAGE+selection_images[i])
        position_image_temp = (round(largeur_ecran*0.21), position_image_temp[1]+round(hauteur_ecran*0.1778))
        image_rect_temp = image_temp.get_rect(topleft=position_image_temp)

        selection_temp = get_police_difficulte(80).render(selection_labels[i], True, BLANC)
        position_selection_temp = (image_rect_temp.right+45, image_rect_temp.top)
        selection_rect_temp = selection_temp.get_rect(topleft=position_selection_temp)

        display_selection.update({i: [[image_temp, image_rect_temp], [selection_temp, selection_rect_temp], selection_labels[i]]})
        selection_labels_hovered.append(get_police_difficulte(80).render(selection_labels[i], True, ORANGE))

    screen.fill(NOIR)
    screen.blit(titre_selection_difficulte, titre_selection_rect)

    while running:
        MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if display_selection.get(0)[1][1].collidepoint(event.pos):
                    print("EASY")
                    launch_game(EASY, largeur_ecran, hauteur_ecran, screen)
                elif display_selection.get(1)[1][1].collidepoint(event.pos):
                    print("NORMAL")
                    launch_game(NORMAL, largeur_ecran, hauteur_ecran, screen)
                elif display_selection.get(2)[1][1].collidepoint(event.pos):
                    print("HARD")
                    launch_game(HARD, largeur_ecran, hauteur_ecran, screen)
                elif display_selection.get(3)[1][1].collidepoint(event.pos):
                    print("CUSTOM")
                    launch_game_custom(largeur_ecran, hauteur_ecran)

        j = 0
        for items in display_selection.values():
            screen.blit(items[0][0], items[0][1])
            if items[1][1].collidepoint(MOUSE_POS):
                screen.blit(selection_labels_hovered[j], items[1][1])
            else:
                screen.blit(items[1][0], items[1][1])
            j += 1

        pygame.display.flip()

    pygame.quit()
