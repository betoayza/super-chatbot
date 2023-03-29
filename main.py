from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import sys
# ListTrainer es un entrenador basado en listas, más básico

chatbot = ChatBot('Super Bot', logic_adapters=[
    {
        "import_path": "chatterbot.logic.BestMatch",
        "default_response": "I don't understand, please be more specific, human",
        "maximun_similarity_threshold": 0.90
    }
])  # crea objeto ChatterBot
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
        break

# exit program
print("\n\nThanks for try this chatbot!")
sys.exit()