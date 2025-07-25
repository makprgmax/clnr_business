from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()

llm = ChatOpenAI(model="gpt-4")

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

__all__ = ["conversation"]