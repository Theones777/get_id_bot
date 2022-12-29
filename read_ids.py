import json
import pprint


with open('ids.json') as f:
    a = json.load(f)
pprint.pprint(a)
