# coding_skill.py
import json
from sys import argv


LANGUAGES = ["C++", "PHP", "Python", "C#", "Haskell", "Java", "JavaScript",
             "Ruby", "CSS", "C"]


def read_json():
    with open(argv[1], 'r') as f:
        data = json.load(f)

    return data


def get_max_level_person(listy):
    max_value = 0
    max_value_person = ""
    for el in listy:
        if el[0][1]['level'] > max_value:
            max_value = el[0][1]['level']
            max_value_person = el[0][0]

    return max_value_person


def get_best_guy():
    skills = []
    names = []
    for i in range(len(read_json()['people'])):
        skills.append([x for x in read_json()['people'][i]['skills']])
    for j in range(len(read_json()['people'])):
        names.append(["".join(y for y in read_json()['people']
                     [j]['first_name']) + " " + "".join
                    (x for x in read_json()['people'][j]['last_name'])])

    tuples = [(names[i], skills[i]) for i in range(0, len(names))]
    dst_list = []

    for lang in LANGUAGES:
        lang_list = []
        for el in tuples:
            lang_list.append([(x, y) for x in el[0] for y in el[1]
                             if y['name'] == lang])
            lang_list = [x for x in lang_list if x != []]
        dst_list.append(get_max_level_person(lang_list))
    idx = 0
    result = {}
    for lang in LANGUAGES:
        result[lang] = dst_list[idx]
        idx += 1

    return result


def beautiful():
    res = ""
    for key, value in get_best_guy().items():
        res += "{0} - {1}\n".format(key, value)

    return res


def main():
    print(beautiful())


if __name__ == '__main__':
    main()
