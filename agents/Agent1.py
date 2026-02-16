from stateAgent.stateAgent import stateAgent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()


OrchestratorAgent_api_key =os.getenv("agent1_llm")
optimizer_llm_api_key =os.getenv("optimizer_llm")
RAG_AGENT_api_key =os.getenv("RAG_AGENT")


Agent11 = ChatGroq(model="llama-3.3-70b-versatile" , api_key=OrchestratorAgent_api_key , temperature=0.7)
Agent12 = ChatGroq(model="llama-3.3-70b-versatile" , api_key=RAG_AGENT_api_key , temperature=0.7)
Agent13 = ChatGroq(model="llama-3.3-70b-versatile" , api_key=optimizer_llm_api_key , temperature=0.7)
Agent14 = ChatGroq(model="llama-3.3-70b-versatile" , api_key=OrchestratorAgent_api_key , temperature=0.7)

def agent1(state: stateAgent):
    prompt=f"""
You are SolverAgent_1 in a multi-agent AI system.

You receive a single task from the PlanningAgent via state["agent1"].

IMPORTANT RULE:
- If the received task is an EMPTY STRING, return an EMPTY STRING as output.
- In this case, do NOT write any code, comments, or text of any kind.

Your responsibility is to solve ONLY this assigned task.

You must follow these rules strictly:
- Output ONLY executable code and code comments.
- Do NOT include explanations outside comments.
- Do NOT include markdown, headings, or extra text.
- Do NOT solve any part of the problem that is not explicitly included in the task.
- Do NOT assume what other agents are doing.
- Assume your output will be merged with outputs from other solver agents.

If the task requires code, write clean, correct, and minimal code.
If the task does not require code, write concise commented logic only.

Output ONLY raw executable Python code.
Do NOT use markdown.
Do NOT use ```python or ``` fences.

Task to solve:
{state["agent1"]}


    """
    response = Agent11.invoke(prompt)
    return {
        "agent1_response": response.content
    }




def agent2(state :stateAgent):
    prompt = f"""
You are SolverAgent_2 in a multi-agent AI system.

You receive a single task from the PlanningAgent via state["agent2"].

IMPORTANT RULE:
- If the received task is an EMPTY STRING, return an EMPTY STRING as output.
- In this case, do NOT write any code, comments, or text of any kind.

Your responsibility is to solve ONLY this assigned task.

You must follow these rules strictly:
- Output ONLY executable code and code comments.
- Do NOT include explanations outside comments.
- Do NOT include markdown, headings, or extra text.
- Do NOT solve any part of the problem that is not explicitly included in the task.
- Do NOT assume what other agents are doing.
- Assume your output will be merged with outputs from other solver agents.

If the task requires code, write clean, correct, and minimal code.
If the task does not require code, write concise commented logic only.

Output ONLY raw executable Python code.
Do NOT use markdown.
Do NOT use ```python or ``` fences.

Task to solve:
{state["agent2"]}


    """
    response = Agent12.invoke(prompt)
    return {
        "agent2_response": response.content
    }
    

def agent3(state :stateAgent):
    prompt = f"""
You are SolverAgent_3 in a multi-agent AI system.

You receive a single task from the PlanningAgent via state["agent3"].

IMPORTANT RULE:
- If the received task is an EMPTY STRING, return an EMPTY STRING as output.
- In this case, do NOT write any code, comments, or text of any kind.

Your responsibility is to solve ONLY this assigned task.

You must follow these rules strictly:
- Output ONLY executable code and code comments.
- Do NOT include explanations outside comments.
- Do NOT include markdown, headings, or extra text.
- Do NOT solve any part of the problem that is not explicitly included in the task.
- Do NOT assume what other agents are doing.
- Assume your output will be merged with outputs from other solver agents.

If the task requires code, write clean, correct, and minimal code.
If the task does not require code, write concise commented logic only.

Output ONLY raw executable Python code.
Do NOT use markdown.
Do NOT use ```python or ``` fences.

Task to solve:
{state["agent3"]}


    """
    response = Agent13.invoke(prompt)
    return {
        "agent3_response": response.content
    }
    

def agent4(state :stateAgent):
    prompt = f"""
You are SolverAgent_4 in a multi-agent AI system.

You receive a single task from the PlanningAgent via state["agent4"].

IMPORTANT RULE:
- If the received task is an EMPTY STRING, return an EMPTY STRING as output.
- In this case, do NOT write any code, comments, or text of any kind.

Your responsibility is to solve ONLY this assigned task.

You must follow these rules strictly:
- Output ONLY executable code and code comments.
- Do NOT include explanations outside comments.
- Do NOT include markdown, headings, or extra text.
- Do NOT solve any part of the problem that is not explicitly included in the task.
- Do NOT assume what other agents are doing.
- Assume your output will be merged with outputs from other solver agents.

If the task requires code, write clean, correct, and minimal code.
If the task does not require code, write concise commented logic only.

Output ONLY raw executable Python code.
Do NOT use markdown.
Do NOT use ```python or ``` fences.

Task to solve:
{state["agent4"]}


    """
    response = Agent14.invoke(prompt)
    return {
        "agent4_response": response.content
    }
    