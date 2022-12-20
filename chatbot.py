import random  # to get a random response
import json
import pickle  # for serialization
import numpy as np
import nltk  # natural language toolkit

from nltk.stem import WordNetLemmatizer  # this will reduce the word to its stem so we dont lose any performance

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Droupout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer

intents = json.loads(open("intents.json").read())  # we are reading json file and loading it on to intents variable
# making it essentially a dictionary

words = []
classes = []
documents = []
ignore_letters = ['?', "!", ",", "."]

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)  # tokenize splits a sentence into individual words
        words.append(word_list)
        documents.append((word_list, intent["tag"]))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print(documents)
