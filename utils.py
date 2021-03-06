import requests

import candidat


def load_candidates(file_path):
    """
    Функция загружает из файла JSON список из
    экземпляров класса Candidates
    :return:
    """
    temp_candidates = requests.get(file_path).json()
    candidates = []
    for temp_cand in temp_candidates:
        ident = temp_cand.get("id")
        name = temp_cand.get("name")
        pictures = temp_cand.get("picture")
        position = temp_cand.get("position")
        skills = temp_cand.get("skills")

        candidate = candidat.Candidates(ident, name, pictures, position, skills)
        candidates.append(candidate)

    return candidates


def good_looking_candidates(file_path):
    """
    Функция загружает из файла список сущностей класса Candidates
    и формирует список кандидатов в заданном формате
    return: Возвращает список кандидатов в нужном формате
    """
    candidates = load_candidates(file_path)
    good_looking = ""
    for _c in candidates:
        good_looking += _c.get_candy_info()
    return good_looking


def get_candy_with_skill(input_skill, file_path):
    """
    Функция загружает из файла список сущностей класса Candidates
    и формирует список кандидатов с запрашиваемыми навыками в заданном формате
    :param input_skill: входящий навык
    :param file_path: путь к файлу Json
    :return: возвращает список кандидатов с запрашиваемым навыком
    """
    candidates = load_candidates(file_path)
    candy_with_skill = ""
    for _c in candidates:
        if _c.chek_candy_skill(input_skill):
            candy_with_skill += _c.chek_candy_skill(input_skill)
    return candy_with_skill


def get_candy_from_id(input_id, file_path):
    """
     Функция загружает из файла список сущностей класса Candidates
     и возвразает данные кандидата по ID
    :param input_id: Входящий ID
    :param file_path: путь к файлу Json
    :return: возвращает данные кандидата с запрашиваемым ID"""

    candidates = load_candidates(file_path)
    for _c in candidates:
        if _c.chek_candy_from_id(input_id):
            return _c.chek_candy_from_id(input_id)
