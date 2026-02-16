from stateAgent.stateAgent import stateAgent, InputGeneratorOutput
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

input_gen_api_key = os.getenv("combine_llm")

input_gen_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=input_gen_api_key,
    temperature=0.7
)

input_gen_llm_structured = input_gen_llm.with_structured_output(InputGeneratorOutput)

def input_generator_agent(state: stateAgent):
    prompt = f"""
You are the InputGeneratorAgent in a multi-agent AI system.

You receive:
- A problem description
- A Python function definition

Problem description:
{state["planning"]}

Function code:
{state["Synthesizer"]}

Your task is to generate example input VALUES for calling the function.

STRICT RULES:
- Return ONLY the predefined structured output.
- The output MUST be a JSON object with a single key named "param".
- The value of "param" MUST be a list of input values.
- The values must be directly usable in a Python function call.
- Do NOT include explanations, text, or code.
- Do NOT return a raw list.

Example valid output:
{{ "param": [2, 3] }}
"""
    response = input_gen_llm_structured.invoke(prompt)

    state["param"] = response.param
    return state
