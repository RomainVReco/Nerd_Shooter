from operator import itemgetter

import json

PATH = "../assets/"
file_name = "tableau_scores.json"


# f1 = open(PATH + file_name, "r", encoding='utf-8')
# s1 = f1.read()
# f1.close()
# print(s1)

# pierre = {
#     "count": 826,
#     "pages": 42,
#     "next": "https://rickandmortyapi.com/api/character/?page=2",
#     "prev": "no"
#   }

# with open("pierre.json","w") as f:
#     json.dump(pierre,f)

# with open("../assets/tableau_scores.json", "r") as tableau_scores:
#     des = json.load(tableau_scores)
# print("load JSON : ", des)


# hiscores = des['hi-scores']
# print(hiscores)
# rank_1 = hiscores[0]
# print(rank_1)
# print(rank_1['name'])

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


def load_score_data():
    with open(PATH + file_name, "r") as tableau:
        return json.load(tableau)


def write_score_data(scores_json):
    with open(PATH + file_name, "w") as tableau:
        json.dump(scores_json, tableau)


def set_score_place(hiscores):
    i = 1
    for dict_score in hiscores:
        dict_score['place'] = i
        i += 1
    return hiscores


def insert_hiscores(score, name):
    file_insert = load_score_data()
    hiscores = file_insert['hi-scores']
    new_score = {
        'place': -1,
        'name': name,
        'score': score
    }
    hiscores.append(new_score)
    hiscores.sort(key=itemgetter('score'), reversed=True)
    file_insert['hi-scores'] = set_score_place(hiscores)
    write_score_data(file_insert)


def insert_lowscores(score, name):
    file_insert = load_score_data()
    lowscores = file_insert['low-scores']
    new_score = {
        'place': -1,
        'name': name,
        'score': score
    }
    lowscores.append(new_score)
    lowscores.sort(key=itemgetter('score'))
    file_insert['low-scores'] = set_score_place(lowscores)
    write_score_data(file_insert)


def check_score_type(score, name):
    # Vérifier si le score est > ou < 0 pour classer ce score le hi-scores ou le low-scores
    if score > 0:
        insert_hiscores(score, name)
    else:
        insert_lowscores(score, name)


check_score_type(350, "Bob")
print(load_score_data())
