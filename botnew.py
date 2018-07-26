from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot



bot = ChatBot('Test')

##for file in os.listdir('file'):
##    chats=open('file/'+files)
##    bot.train(chats)

#con =open('chat.txt','r').readlines()
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")

while True:
    ques=input(" ")
    respo=bot.get_response(ques)
    print(respo)
