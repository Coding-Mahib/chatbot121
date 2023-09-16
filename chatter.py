import random
import json
import pyttsx3

import torch
from model import NeuralNet
from nltk_utils import tokenize, bag_of_words, stem

import os

files = os.listdir('./intents')

def extension(filename: str):
    e = filename.split('.')
    return e[len(e) - 1]

intents = {'intents': []}

for file in files:
    if extension(file) == 'json':
        with open('./intents/' + file) as f:
            intents['intents'].extend(json.load(f)['intents'])

FILE = './chat-0.2-beta.model'
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
model_state = data['model_state']
tags = data['tags']
all_words = data['all_words']

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

import datetime

def get_time():
	return datetime.datetime.now().strftime('%I:%m %p')

def get_resp(text: str):
    sent = tokenize(text)
    x = bag_of_words(sent, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)

    output = model(x)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
    	if tag == 'time':
    		return get_time()
    	else:
        	for intent in intents['intents']:
        		if tag == intent['tag']:
        			resp = random.choice(intent["responses"])
        			return resp
    else:
        return 'I don\'t understand it ...'
