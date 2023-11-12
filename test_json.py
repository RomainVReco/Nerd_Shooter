from operator import itemgetter
import pygame
import json
from assets.fonts_generator import get_police_menu

pygame.init()

ORANGE = (255, 127, 0)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
INDIGO = (75, 0, 130)
GRIS = (211, 211, 211)
BLANC = (255, 255, 255)
DARK_GREY = (169, 169, 169)

PATH = "../assets/"
file_name = "tableau_scores.json"

with open("score/tableau_scores.json", "r") as tableau_scores:
    des = json.load(tableau_scores)
print("load JSON : ", des)

print(des['hi-scores'])
hiscore_list = {}
data = des.keys()
print(type(data), data)

def get_score_elements(score_data, data_key):
    values_list = list()
    score_dict = {}
    i = 0
    for score in (score_data[data_key]):
        value_dict_score = score.values()
        for value in value_dict_score:
            value_temp = get_police_menu(40).render(str(value), True, BLANC)
            value_rect = value_temp.get_rect(center=(0, 0))
            values_list.append((value_temp, value_rect))
        score_dict.update({i: values_list})
        i += 1
        if len(score_dict) == 5:
            break


# print(len(hiscore_list))
# print(hiscore_list.keys())

# name_temp = get_police_menu(40).render(hiscore[key_dict_score[1]])
# score_temp = get_police_menu(40).render(hiscore[key_dict_score[2]])
# place_rect = place_temp.get_rect(center=(0, 0))
# name_rect = name_temp.get_rect(center=(0, 0))
# score_rect = score_temp.get_rect(center=(0, 0))
# hiscore_list.update({i: [[place_temp, place_rect], [name_temp, name_rect], [score_temp, score_rect]]})
# print(hiscore_list)
# if (len(hiscore_list)) == 5:
#     print('je breake')
#     break

# for item in hiscore:
#     print(item, "un tour de boucle")
#     # for i in range(3):

# place_temp = get_police_menu(40).render(hiscore[item[0]])
# name_temp = get_police_menu(40).render(hiscore[item[1]])
# score_temp = get_police_menu(40).render(hiscore[item[2]])

# new_score = {
#     'place': 6,
#     'name': 'Cain',
#     'score': 100
# }
# print('type des :', type(des))
# print("taille hiscore :", len(hiscores))
# print("type hiscore", type(hiscores))
#
# # hiscores.append(new_score)
#
# for x in hiscores:
#     print("Boucle JSON for:", x)
#     if x['score'] <= 2000:
#         # x['score'] += 500
#         print('Score haut :', x['score'])
# des['hi-scores'] = hiscores
# print(des)
# hiscores.sort(key=itemgetter('name'))
# print(hiscores)

# with open("../assets/tableau_scores.json", "w", encoding="utf-8") as ecriture:
#      json.dump(des, ecriture)
