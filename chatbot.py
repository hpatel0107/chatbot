import function
import random
import json
import pickle
import numpy as np
import datetime
import time
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()

intents = json.loads(open("intents.json").read())

words = pickle.load(open('words1.pkl','rb'))
classes = pickle.load(open('classes1.pkl','rb'))

model = load_model('guni_chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r>ERROR_THRESHOLD]
    
    results.sort(key=lambda x:x[1], reverse=True)
    
    return_list = []
    
    for r in results:
        return_list.append({'intent':classes[r[0]], 'probability':str(r[1])})
    return return_list
def print_current_time():
    now = datetime.datetime.now()
    print(now.strftime("%I:%M:%S %p"))


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if tag=='time':
            result=print_current_time()
            break
            
        if tag=='date':
            function.get_current_date()
            #print (time.strftime("%Y-%m-%d"))
            break
        if tag=='attendance':
            function.get_attendance()
            #print (time.strftime("%Y-%m-%d"))
            break

            
        if tag=='day':        
            result = (time.strftime("%A"))
            break

        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print("Go! Bot is running")

while True:
    message = input("")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)


