import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import colorama
import random
import pickle
from TextToSpeech import TTS

colorama.init()
from colorama import Fore, Style, Back

with open("AI_Bot\intents.json") as file:
    data = json.load(file)

def chat(text):
    # load trained model
    model = keras.models.load_model('AI_Bot/chat_model')
    # load tokenizer object
    with open('AI_Bot/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    # load label encoder object
    with open('AI_Bot/label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
    # parameters
    max_len = 20
    # while True:
    print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
    # inp = input()
    inp=text
    if inp.lower() == "kill":
        TTS.speak("Bye Sir")
        # break
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    for i in data['intents']:
        if i['tag'] == tag:
            reply = np.random.choice(i['responses'])
            print("ChatBot:" + reply)
            TTS.speak(reply)
    # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))


# print("Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
# chat()