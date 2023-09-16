import json

file = 'test.json'

with open(file) as f:
    cnt = json.load(f)

with open(file, 'w') as f:
    json.dump(cnt, f, indent=4)