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

hasBounced = False

dic = {1: [34, 45, 60], 2: (50, 60, 30), 3: hasBounced}
print(dic)
print(dic.get(1))
print(dic.values())
print(dic)

game = "game"

dic_2 = {1: 34, 45: 60, 2: [50, 60, 30], 4: hasBounced}
dic_3 = {1: [game, False, False, (0.5, 0.5)]}

print(dic_2)
hasBounced = True
dic_2.update({4: hasBounced})
print("Dic après chgmnt hasBounced : ", dic)

if dic_2.get(4):
    print("coucou")

variables_temp = dic_3.get(1)
print("Variables temps : ", variables_temp)
temp = (variables_temp[3][0] * -1, 0.5)
variables_temp[3] = temp
print("Variables modifiées : ", variables_temp)
new_dic_3 = dic_3.update({1: variables_temp})

print("Mise à jour dic_3 : ", dic_3)

print("Type dic_3 : ", type(dic_3))
print("Dic_2 : ", dic_2)
# dic_3 = dic_2.copy()
print("Copie de dic_2 dans dic_3 : ", dic_3)

# dic_3 = fonction(dic_2)

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
