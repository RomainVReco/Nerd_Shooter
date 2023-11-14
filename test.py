import pygame

from assets.fonts_generator import get_police_difficulte

pygame.init()
pygame.mixer.init()

BLANC = (255, 255, 255)
a = ["sot"]
a *= 3
print(a)
FPS = 30
print((5 / FPS))

largeur_ecran = 1280
hauteur_ecran = 720
font_Test = pygame.font.Font("assets/fonts/OptimusPrincepsSemiBold.ttf", 80)

selection_facile = font_Test.render("Personnalisée", True, BLANC)
print("Taille personnlisée :", selection_facile.get_rect(center=(0, 0)))

for i in range(21, 150, 21):
    print("i : ", i, end=' ')
    print("i%2 :", i % 2)

liste_sprt = [-5, -8, -1, -3, -10]
print("avant sort() : ", liste_sprt)
liste_sprt.sort(reverse=True)
print("après sort() : ", liste_sprt)

text = "Capt. Steven Hiller"
print(len(text))
selection_facile = font_Test.render("Capt. Steven Hiller", True, BLANC)
rect = selection_facile.get_rect()
print("dimension 20 char :", rect)
score = 100

print("Toutes les cibles ont été détruites ! \n"
      f"Score {score} : \n"
      "Votre nom : ")
CENTER_X = largeur_ecran//2
CENTER_Y = hauteur_ecran//2
font_Test_40 = pygame.font.Font("assets/fonts/OptimusPrincepsSemiBold.ttf", 40)
text_endgame = font_Test_40.render("Toutes les cibles ont été détruites ! \n"
                                   f"Score {score} : \n"
                                   "Votre nom : ", True, BLANC)
text_endgame_rect = text_endgame.get_rect(center=(CENTER_X, CENTER_Y))
# input_box = pygame.Rect(CENTER_X, CENTER_Y, )
print(text_endgame_rect)
topleft = list(text_endgame_rect.topleft)
print(type(topleft))
height = text_endgame_rect.height

nom = font_Test_40.render("Capt. Steven Hiller ", True, BLANC)
nom_rect = nom.get_rect()
print(nom_rect)

chiffre = '1 000'
if chiffre > 0:
    print("ok")
chiffre_int = int(chiffre.replace(' ',''))
print(chiffre_int, type(chiffre_int))
