from stateAgent.stateAgent import stateAgent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

Synthesizer_llm_api_key = os.getenv("agent3_llm")

Synthesizer = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=Synthesizer_llm_api_key,
    temperature=0.0
)

def SynthesizerAgent(state: stateAgent):
    agent_responses = [
        state.get("agent1_response", "").strip(),
        state.get("agent2_response", "").strip(),
        state.get("agent3_response", "").strip(),
        state.get("agent4_response", "").strip(),
    ]

    non_empty_responses = [r for r in agent_responses if r]

    if not non_empty_responses:
        return {"Synthesizer": ""}

    prompt = f"""
You are the SynthesizerAgent in a multi-agent AI system.

Original user question:
{state["question"]}

Below are partial solutions from solver agents.
Some may be empty and have already been removed.

{chr(10).join(non_empty_responses)}

Your task:
- Combine the above content into ONE final answer.
- Use the user question as the primary reference.
- Remove redundancy and contradictions.
- Do NOT add new features or assumptions.
- Do NOT mention agents or the synthesis process.

OUTPUT RULES:
- Output ONLY the final result.
- If the user question requires code, output ONLY executable Python code with necessary comments.
- If the user question does NOT require code, output ONLY plain text.
- No markdown, no headings, no explanations outside comments.
"""

    response = Synthesizer.invoke(prompt)
    return {"Synthesizer": response.content}
