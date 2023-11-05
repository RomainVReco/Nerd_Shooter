import pygame

pygame.init()
pygame.mixer.init()

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

f = 0
print(bool(f))

g = 1
print(bool(g))
FPS = 30
hauteur = 720
vitesse = 60//FPS

print(vitesse)


largeur_ecran = 1280
hauteur_ecran = 720

pygame.init()
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
clock = pygame.time.Clock()
running = True
dt = 0
screen.fill("grey")
ORANGE = (255, 127, 0)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
INDIGO = (75,0,130)

pos_x_object = 0
pos_y_object = 0
WIDTH_OBJECT = 70
HEIGHT_OBJECT = 50
FPS = 30
clock = pygame.time.Clock()
number_of_enemies = 8
number_of_target = 5
number_of_horizontal_left = 3
number_of_horizontal_right = 3
number_of_horizontal = 3
