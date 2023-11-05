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

# Variables pour la découpe de l'écran
margin_title = round(hauteur_ecran*0.1)
CENTER_X = largeur_ecran//2
HAUTEUR_BLOC_MENU = (hauteur_ecran - hauteur_ecran*0.2 - hauteur_ecran*0.1)
SCREEN_SLICE_VALUE = 0.17

titre_selection_difficulte = get_police_difficulte(80).render("Choisissez la difficulte : ", True, BLANC)
position_titre_selection = (round(largeur_ecran*0.05), round(hauteur_ecran*0.06))
titre_selection_rect = titre_selection_difficulte.get_rect(topleft=position_titre_selection)
print(titre_selection_rect)
help(pygame.rect.Rect)

selection_labels = ["Facile", "Normal", "Difficle", "Personalisée"]
selection_images = ["soyjak-100px.png", "wojak-100px.png", "rages_screaming-100px.png", "doomer_stage2-100px.png"]
position_image_facile = ((CENTER_X//2), (hauteur_ecran*0.2+hauteur_ecran*0.1))


for i in range(len(selection_labels)):
    image_temp = pygame.load(PATH_IMAGE+selection_images[i])
    position_temp = position_image_facile
    image_rect_temp = image_temp.get_rect(center=position_temp)

position_image_facile = ((CENTER_X//2), (hauteur_ecran*0.2+hauteur_ecran*0.1))
image_facile = pygame.image.load("../assets/img/soyjak-100px.png")
image_facile_rect = image_facile.get_rect(center=position_image_facile)

selection_facile = get_police_difficulte(80).render("Facile", True, BLANC)
position_facile = (image_facile_rect.right+15, image_facile_rect.top+5)
selection_facile_rect = selection_facile.get_rect(topleft=position_facile)

while running:
    MOUSE_POS = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(NOIR)
    screen.blit(titre_selection_difficulte, titre_selection_rect)
    screen.blit(image_facile, image_facile_rect)
    screen.blit(selection_facile, selection_facile_rect)

    pygame.display.flip()

pygame.quit()


