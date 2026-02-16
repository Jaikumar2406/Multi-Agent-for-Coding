from stateAgent.stateAgent import stateAgent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

chat_api_key =os.getenv("evauate_llm1")

chat = ChatGroq(model="llama-3.3-70b-versatile" , api_key=chat_api_key , temperature=0.7)

def chattingAgent(state: stateAgent):
    prompt = f"""
You are a helpful assistant.

User query:
{state.get("question", "")}
"""
    response = chat.invoke(prompt)
    state["planning"] = response.content
    state["mode"] = "Chat"
    return state