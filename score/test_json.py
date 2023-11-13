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

with open("tableau_scores.json", "r") as tableau_scores:
    des = json.load(tableau_scores)
print("load JSON : ", des)

print("des hi-scores", des['hi-scores'])
print("type de des hiscores [0]", des['hi-scores'][0], type(des['hi-scores'][0]))
hiscore_list = {}
data = des.keys()
print(type(data), data)
k = 1


# for score in (des['hi-scores']):
#     print("tour de boucle :", k)
#     print(score)
#     print("taille liste des values de des[]", len(list(score.values())))
#     print("Parcours des-hiscores via for", list(score.values())[0], type(score.values()))
#     k += 1


def get_score_elements(score_data, center_element, data_key):
    values_list = list()
    score_dict = {}
    i = 0
    position_temp = center_element.copy()
    value_rect = 0
    for score in (score_data[data_key]):
        value_dict_score = score.values()
        for value in value_dict_score:
            value_temp = get_police_menu(40).render(str(value), True, BLANC)
            value_rect = value_temp.get_rect(topleft=position_temp)
            position_temp[0] += value_rect.width + 15
            values_list.append((value_temp, value_rect))
        position_temp[1] += value_rect.height
        position_temp[0] = center_element[0]
        list_temp = values_list.copy()
        score_dict.update({i: list_temp})
        values_list.clear()
        i += 1
        if len(score_dict) == 5:
            return score_dict


position = [100, 20]
test = get_score_elements(des, position, 'hi-scores')
print("taille dictionnaire et contenu :", len(test), test)
print(test[0][0])
print(test[1])

#
# print("get score elements : ", + get_score_elements(des, 'hi-scores'))

# def get_score_elements(score_data, data_key, center_elements, police, color) -> dict:
#     p = 0
#     print("Position : ", center_elements)
#     values_list = list()
#     score_dict = {}
#     value_rect = []
#     k = 0
#     position_temp = center_elements.copy()
#     for score in (score_data[data_key]):
#         print(f'Tour de boucle {p}')
#         value_dict_score = score.values()
#         for value in value_dict_score:
#             value_temp = police.render(str(value), True, color)
#             print("valeur :", value)
#             value_rect = value_temp.get_rect()
#             position_temp[0] += value_rect.width
#             value_rect.topleft = position_temp
#             values_list.append([value_temp, value_rect])
#             print("Largeur rectangle :", value_rect.width)
#             position_temp[0] += value_rect.width
#             print("position x : ", position_temp[0])
#         score_dict.update({k: values_list})
#         center_elements[1] += 60
#         print("position y :", center_elements[1])
#         position_temp[0] = center_elements[0]
#         k += 1
#         p += 1
#         if len(score_dict) == 5:
#             return score_dict


print(len(hiscore_list))
print(hiscore_list.keys())

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
