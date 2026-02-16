from stateAgent.stateAgent import stateAgent
from stateAgent.stateAgent import StructureOutput
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()



OrchestratorAgent_api_key =os.getenv("agent1_llm")
Orchestrator_Agent = ChatGroq(model="llama-3.3-70b-versatile" , api_key=OrchestratorAgent_api_key , temperature=0.7)
Orchestrator_Agent_ = Orchestrator_Agent.with_structured_output(StructureOutput)

def OrchestratorAgent(state: stateAgent):

    messages = state.get("messages", [])
    error_ = state.get("error", "")
    status = state.get("status", "ok")

    conversation = "\n".join(
        [f"{m['role'].upper()}: {m['content']}" for m in messages]
    )

    # ================= ERROR MODE =================
    if status == "error":

        if state.get("max_try", 0) <= 0:
            state["mode"] = "Chat"
            state["planning"] = (
                "Repeated execution failures. "
                "System should stop retries and respond gracefully."
            )
            return state

        prompt = f"""
You are the OrchestratorAgent of a multi-agent AI system.

Conversation so far:
{conversation}

Execution error:
{error_}

Your tasks:
1. Infer the user's intended QUESTION from the conversation.
2. Reinterpret that question considering the execution failure.

Rules:
- Do NOT solve the problem
- Do NOT write or fix code
- Do NOT decompose tasks

Return structured output only:
mode = "Problem"
question = inferred user question (1 sentence)
problem = ONE paragraph explanation for AI agents
"""

        response = Orchestrator_Agent_.invoke(prompt)

        state["mode"] = response.mode
        state["question"] = response.question
        state["planning"] = response.problem
        state["max_try"] -= 1
        return state

    # ================= NORMAL MODE =================
    prompt = f"""
You are the OrchestratorAgent of a multi-agent AI system.

Conversation so far:
{conversation}

Your tasks:
1. Infer the user's intended QUESTION from the conversation.
2. Decide whether this is Chat or Problem.

Definitions:
- Chat → discussion, learning, opinions
- Problem → build, debug, design, analyze, execute

Rules:
- Do NOT solve anything
- Do NOT write code
- Do NOT decompose tasks

Return structured output only:
mode = "Chat" or "Problem"
question = inferred user question (1 sentence)
problem = ONE paragraph summary for AI agents
"""

    response = Orchestrator_Agent_.invoke(prompt)

    state["mode"] = response.mode
    state["question"] = response.question
    state["planning"] = response.problem
    return state
