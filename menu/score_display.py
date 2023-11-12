import pygame

from Sons.sound_effects import play_intro_music
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

display_score_titles = {}
hovered_labels = []
score_titre = ["Hall of Fame", "Hall of Shame"]
position_titre = [(640, 60), (640, 420)]

# Division de l'écran en deux

# Création de deux rectangles contenant les titres
for i in range(len(score_titre)):
    name_temp = get_police_menu(50).render(score_titre[i], True, BLANC)
    name_hovered = get_police_menu(50).render(score_titre[i], True, ORANGE)
    temp_rect = name_temp.get_rect(center=position_titre[i])
    display_score_titles.update({i: (name_temp, temp_rect, score_titre[i])})
    hovered_labels.append(name_hovered)

while running:
    MOUSE_POS = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(NOIR)
    for display in display_score_titles.values():
        screen.blit(display[0], display[1])
    j = 0
    for items in display_score_titles.values():
        if items[1].collidepoint(MOUSE_POS):
            screen.blit(hovered_labels[j], items[1])
        else:
            screen.blit(items[0], items[1])
        j += 1

    pygame.display.flip()

pygame.quit()
