import json
import pprint


def refactor_dict(d_path, suff):
    with open(d_path) as f:
        dict_list = json.load(f)
    res_dict = {}
    for el in dict_list:
        res_dict[list(el.keys())[0]] = f'{suff}---id{list(el.values())[0][0]}'
    pprint.pprint(dict_list)
    print()
    pprint.pprint(res_dict)


refactor_dict('ids.json', 'geo')
