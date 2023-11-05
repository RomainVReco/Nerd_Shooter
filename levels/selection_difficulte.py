import pygame.font

from assets.fonts_generator import get_police_difficulte

largeur_ecran = 1280
hauteur_ecran = 720

pygame.init()
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Nerd shooter")
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
                launch_game(EASY)
            elif display_selection.get(1)[1][1].collidepoint(event.pos):
                print("NORMAL")
                lauch_game(NORMAL)
            elif display_selection.get(2)[1][1].collidepoint(event.pos):
                print("HARD")
                lauch_game(HARD)
            elif display_selection.get(3)[1][1].collidepoint(event.pos):
                print("CUSTOM")
                lauch_game_custom()

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


