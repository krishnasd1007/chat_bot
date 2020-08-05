from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot_corpus.corpus import DATA_DIRECTORY

conan= ChatBot('My_Bot')

trainer = ListTrainer(conan)

convo = [
    'hello',
    'hey!',
    'hi',
    'yo',
    'what is your name?',
    'my name is conan',
    'how is krishna?',
    'she is the smartest girl i have met',
    'that is great!',
    'yeah, she is awesome!',
    'who made you?',
    'krishna made me',
    'who are you?'
    'I am conan, I am the faithful assistant of krishna madam',
    'who are you?',
    'I am conan, a chatbot',
]


trainer.train(convo)

while True:
    a = input()
    if a == 'exit':
        break
    ans = conan.get_response(a)
    print('conan : ', ans)