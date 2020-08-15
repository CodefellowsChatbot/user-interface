import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from speech import sam_speak, record_audio

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('user-interface/user_interface/intents.json', 'r') as json_data, open('user-interface/user_interface/intents2.json', 'r') as json_data_2:
    intents = json.load(json_data)
    intents_2 = json.load(json_data_2)
    for el in intents_2["intents"]:
        intents["intents"].append(el)

FILE = "user-interface/user_interface/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"
#print("Let's chat! (type 'quit' to exit)")
sam_speak('How can I help you today?')
while True:
    #sentence = input("You: ")
    sentence = record_audio()
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                sam_speak(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand...")