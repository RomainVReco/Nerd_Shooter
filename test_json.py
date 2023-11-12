
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