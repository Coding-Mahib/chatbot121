import json

data = {'intents': []}

while True:
    cmd = str(input('>>> '))
    if cmd == 'add':
        print('\n')
        tag = str(input('[TAG]: '))
        patterns = str(input('[PATTERNS] (separated by comma): '))
        responses = str(input('[RESPONSES] (separated by comma): '))

        patterns = patterns.split(',,,')
        responses = responses.split(',,,')

        i = {'tag': tag, 'patterns': patterns, 'responses': responses}
        data['intents'].append(i)
    else:
        break
with open('test.json', 'w') as f:
    json.dump(data, f, indent=4)