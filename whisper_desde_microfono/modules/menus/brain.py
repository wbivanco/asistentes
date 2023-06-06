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
    return eval(response.content)

def create_notion_page(data):
    properties = {
        "Name": {"title": [{"text": {"content": f"{data.get('title', None)}"}}]},        
    } # OJO!, Name asi se llama el encabezado de la página en Notion y el segundo title es nombre 
    # en el template de Langchain, sino devuelve None. 
    children_page = [{"object": "block", "paragraph":{"rich_text": [{"text":{"content": f"{data.get('content', None)}"}}]}}] # Aquí
    # es donde se carga en si el contenido de la página y que se accede desde el título cargado en el 
    # paso anterior en Notion con el contenido del segundo content.
    notion.create_page(properties=properties, children=children_page)

def start_brain_mode():
    say_welcome()
    assistant_response = generate_response()
    print(assistant_response.get('content', None))
    talker.talk(assistant_response.get('content', None))
    create_notion_page(assistant_response)