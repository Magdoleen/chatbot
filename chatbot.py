from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("DFI Ticketing Bot")
                     #storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     #database = mongodb_name,
                     #database_uri = mongodb_uri)
#bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)
trainer.train(['What is your name?', 'My name is Candice'])
trainer.train(['Who are you?', 'I am a bot' ])
trainer.train(['Who created you?', 'Tony Stark', 'Sahil Rajput', 'You?'])
#trainer.set_trainer(ChatterBotCorpusTrainer)
#bot.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("chatbotPage.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(userText)
    print(str(bot.get_response(userText)))
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()
