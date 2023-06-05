from modules.talker.talk import Talker, TtsTalker
from modules.listen import Listener
from modules.notion.notion_integration import Notion
from modules.langchain_assitant.langchain_brain import LangChainBrainAsistant


talker = Talker(TtsTalker())
listener = Listener()
langchain_assistant = LangChainBrainAsistant()
notion = Notion()


def say_welcome():
    talker.talk(
        "Hola, bienvenido al modo sábelo todo"
        "hazme cualquier pregunta que necesites"
    )

def listen_to_response():
    return listener.listen()

def generate_response():
    response = langchain_assistant.chat(listen_to_response())
    return response 

def create_notion_page(data):
    pass

def start_brain_mode():
    say_welcome()
    assistant_response = generate_response()
    print(assistant_response.content)
    talker.talk(assistant_response.content)