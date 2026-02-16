from stateAgent.stateAgent import stateAgent
from stateAgent.stateAgent import plaining_output
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()


plaining_llm_api_key =os.getenv("agent2_llm")
PlainigAgent = ChatGroq(model="llama-3.3-70b-versatile" , api_key=plaining_llm_api_key , temperature=0.6)
Plainig_Agent = PlainigAgent.with_structured_output(plaining_output)

def plainingAgent(state: stateAgent):
    prompt = f"""
You are the PlanningAgent in a multi-agent AI system.

You receive a problem description in:
{state["planning"]}

Your goal is to decompose the problem based on LOGICAL COMPLEXITY,
not based on solution ownership.

Agent Complexity Rules:
- agent1: handle problems with only ONE simple logical step.
- agent2: handle parts of the problem involving TWO to THREE logical steps.
- agent3: handle parts involving THREE to FOUR logical steps.
- agent4: handle any complex or high-risk logic so the problem can be solved safely.

Decomposition Rules:
- All agents are equally important.
- Complexity should increase gradually from agent1 to agent4.
- Use only the agents that are actually required.
- If the entire problem fits agent1, leave others empty.
- Do NOT split only by arithmetic operations mechanically;
  consider logical reasoning depth.

You MUST NOT:
- Solve the problem
- Write code
- Give implementation hints
- Create unnecessary agents

Always respond ONLY using the structured output:
agent1, agent2, agent3, agent4

If an agent is not required, return an empty string.
"""

    response = Plainig_Agent.invoke(prompt)
    return {
        "agent1": response.agent1,
        "agent2": response.agent2,
        "agent3": response.agent3,
        "agent4": response.agent4
    }