import pygame

from assets.fonts_generator import get_police_menu
from score.scores_functions import load_score_data, get_score_elements

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
position_titre = [(largeur_ecran // 2, round(hauteur_ecran * 0.083)), (largeur_ecran // 2, round(hauteur_ecran * 0.5385))]
print(position_titre)

# Division de l'écran en deux
police = get_police_menu(40)

# Création de deux rectangles contenant les titres
for i in range(len(score_titre)):
    name_temp = get_police_menu(50).render(score_titre[i], True, BLANC)
    name_hovered = get_police_menu(50).render(score_titre[i], True, ORANGE)
    temp_rect = name_temp.get_rect(center=position_titre[i])
    display_score_titles.update({i: (name_temp, temp_rect, score_titre[i])})
    hovered_labels.append(name_hovered)

print("taille titre", display_score_titles[1][1])
scores_type = load_score_data()
data_key = list(scores_type.keys())
scores_type_display = []
hiscores = {}
lowscores = {}
initial_position_elements = ([round(largeur_ecran*0.378), round(hauteur_ecran*0.1264)], [round(largeur_ecran*0.378), round(hauteur_ecran*0.5944)])

for i in range(len(data_key)):
    print("Tour de boucle 1")
    scores_type_display.append(get_score_elements(scores_type, data_key[i], initial_position_elements[i], police, BLANC))

hiscores, lowscores = scores_type_display



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

    for score in hiscores.values():
        screen.blit(score[0][0], score[0][1])
        screen.blit(score[1][0], score[1][1])
        screen.blit(score[2][0], score[2][1])

    pygame.display.flip()

pygame.quit()
