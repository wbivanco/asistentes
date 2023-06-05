import dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
) # El primero une los otros dos y es lo que se envía al modelo, el segundo me permite dar un rol al 
# chat y el tercero es el texto escrito por el humano.

from modules.templates.templates import brain_template

dotenv.load_dotenv()

chat = ChatOpenAI(temperature=0.2) # Temperature indica que tan disruptiva u original es la respuesta.


class LangChainBrainAsistant:
    def chat(self, user_text):
        assitant_prompt = SystemMessagePromptTemplate.from_template(brain_template)
        user_prompt = HumanMessagePromptTemplate.from_template("{user_text}")
        chat_prompt = ChatPromptTemplate.from_messages(
            [assitant_prompt, user_prompt]
        )
        response = chat(chat_prompt.format_prompt(user_text=user_text).to_messages())
        return response