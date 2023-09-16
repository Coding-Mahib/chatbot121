# import json

# with open('ai.json') as f:
#     cnt1 = json.load(f)
# with open('../intents0.1.json') as f:
#     cnt2 = json.load(f)
# c = cnt1['intents'] + cnt2['intents']

import os

files = os.listdir('.')

f = []

def extension(filename: str):
    e = filename.split('.')
    return e[len(e) - 1]

for file in files:
    if extension(file) == 'json':
        f.append(file)
print(f)