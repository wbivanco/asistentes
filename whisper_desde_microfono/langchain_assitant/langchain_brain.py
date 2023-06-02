import dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from templates.templates import brain_template

dotenv.load_dotenv()

chat = ChatOpenAI(temperature=0.2)


class LangChainBrainAsistant:
    def chat(self, user_text):
        assitant_prompt = SystemMessagePromptTemplate.from_template(brain_template)