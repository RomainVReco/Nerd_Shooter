from operator import itemgetter

import json

PATH = "../score/"
file_name = "tableau_scores.json"


def load_score_data():
    """
    :return: les scores du jeu au format JSON
    """
    with open(PATH + file_name, "r") as tableau:
        return json.load(tableau)


def write_score_data(scores_json):
    """
    A partir d'une nouvelle liste de score, met à jour le fichier JSON enregistré localement
    :param scores_json:
    :return: None
    """
    with open(PATH + file_name, "w") as tableau:
        json.dump(scores_json, tableau)


def set_score_place(hiscores):
    """
    A partir d'une liste de dictionnaires contenant les scores des différents joueurs, affecte la bonne place aux scores
    à chaque nouveau score enregistré
    :param hiscores: liste de dictionnaires, contenant une clé 'place'
    :return: renvoie la liste de dictionnaires avec le bon numéro pour la clé 'place'
    """
    i = 1
    for dict_score in hiscores:
        dict_score['place'] = str(i)
        i += 1
    return hiscores


def insert_hiscores(score, name):
    """
    Ajoute dans le tableau des scores du jeu, le score > 0 et le nom passé en paramètre. La liste des scores > 0 est
    alors classé par score décroissant. L'ajout du bon numéro de place est géré automatiquement.
    :param score: le score réalisé par le joueur, arrêté en fin de partie
    :param name: le nom renseigné par le joueur en fin de partie
    :return: None, le fichier JSON des scores est mis à jour avec la nouvelle donnée et le nouveau classement
    """
    file_insert = load_score_data()
    hiscores = file_insert['hi-scores']
    new_score = {
        'place': -1,
        'name': name,
        'score': score
    }
    hiscores.append(new_score)
    hiscores.sort(key=itemgetter('score'), reverse=True)
    file_insert['hi-scores'] = set_score_place(hiscores)
    write_score_data(file_insert)


def insert_lowscores(score, name):
    """
    Ajoute dans le tableau des scores du jeu, le score < 0 et le nom passé en paramètre. La liste des scores < 0 est
    alors classé par score décroissant. L'ajout du bon numéro de place est géré automatiquement.
    :param score: le score réalisé par le joueur, arrêté en fin de partie
    :param name: le nom renseigné par le joueur en fin de partie
    :return: None, le fichier JSON des scores est mis à jour avec la nouvelle donnée et le nouveau classement
    """
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
    """
    Vérifier si le score est > ou < 0 pour classer ce score le hi-scores ou le low-scores
    :param score: le score réalisé par le joueur, arrêté en fin de partie
    :param name: le nom renseigné par le joueur en fin de partie
    :return: aucun
    """
    if int(score) > 0:
        insert_hiscores(score, name)
    else:
        insert_lowscores(score, name)


def get_score_elements(score_data, data_key, center_elements, police, color) -> dict:
    """
    Prépare les éléments graphiques à afficher sur le tableau des scores
    :param score_data: la base de données JSON récupérée en dict
    :param data_key: clé du dictionnaire
    :param center_elements: la position initiale des rectangles
    :param police: le type de font désiré
    :param color:
    :return: un dictionnaire contenant les images, poisitions et scores à placer sur l'écran
    """
    values_list = list()
    score_dict = {}
    i = 0
    position_temp = center_elements.copy()
    value_rect = 0
    turn = 0
    for score in (score_data[data_key]):
        value_dict_score = score.values()
        for value in value_dict_score:
            value_temp = police.render(str(value), True, color)
            value_rect = value_temp.get_rect(topleft=position_temp)
            position_temp[0] += value_rect.width + 100
            if turn == 2:
                value_rect.left = 900
            values_list.append((value_temp, value_rect))
            turn += 1
        position_temp[1] += value_rect.height
        position_temp[0] = center_elements[0]
        list_temp = values_list.copy()
        score_dict.update({i: list_temp})
        values_list.clear()
        i += 1
        turn = 0
        if len(score_dict) == 5:
            return score_dict
    return score_dict
