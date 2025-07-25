from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from chat_memory import conversation
from langchain.callbacks import LangChainTracer

tracer = LangChainTracer()

llm = ChatOpenAI(model_name="gpt-4", callbacks=[tracer])

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    callbacks=[tracer],
    verbose=True
)


def planner_agent(state, callbacks=[tracer]):
    user_input = state.get("user_input", "")

    response = conversation.predict(input=user_input)

    print(f"[PLANNER] user_input: {user_input}")
    print(f"[PLANNER] llm_response: {response}")

    return {
        **state,
        "task": "Find recipe",
        "description": response,
        "status": "ok"
    }

