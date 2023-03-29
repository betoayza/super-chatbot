from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# ListTrainer es un entrenador basado en listas, más básico

chatbot = ChatBot('Super Bot')  # crea objeto ChatterBot
# conversation = open("training/conversations.yml") # crea la conversacion

trainer = ChatterBotCorpusTrainer(chatbot)
# trainer = ListTrainer(chatbot)
# trainer.train("chatterbot.corpus.english.conversations")
trainer.train("training/conversations.yml")

while True:
    try:
        request = input("You: ")
        response = chatbot.get_response(request)
        print(f"🤌\tSuper Bot ⭐: ", response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("\n\nThanks for try this chatbot!")
        break
