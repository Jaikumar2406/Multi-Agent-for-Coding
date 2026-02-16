from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from stateAgent.stateAgent import stateAgent
from agents.chattingAgent import chattingAgent
from agents.OrchestratorAgent import OrchestratorAgent
from agents.PlainigAgent import plainingAgent
from agents.Agent1 import agent1 , agent2 , agent3 , agent4
from agents.SynthesizerAgent import SynthesizerAgent
from agents.InputGeneratorAgent import input_generator_agent
from agents.run_code import execute_user_code
from agents.router import route_from_planner , execution_router



def build_workflow():
    graph = StateGraph(stateAgent)

    # -------- Nodes --------
    graph.add_node("OrchestratorAgent", OrchestratorAgent)
    graph.add_node("chattingAgent", chattingAgent)
    graph.add_node("PlanningAgent", plainingAgent)

    graph.add_node("agent1", agent1)
    graph.add_node("agent2", agent2)
    graph.add_node("agent3", agent3)
    graph.add_node("agent4", agent4)

    graph.add_node("SynthesizerAgent", SynthesizerAgent)
    graph.add_node("InputGeneratorAgent", input_generator_agent)
    graph.add_node("ExecutorAgent", execute_user_code)

    # -------- Entry --------
    graph.set_entry_point("OrchestratorAgent")

    # -------- Orchestrator routing --------
    graph.add_conditional_edges(
        "OrchestratorAgent",
        route_from_planner,
        {
            "Chat": "chattingAgent",
            "Problem": "PlanningAgent"
        }
    )

    # -------- Chat flow --------
    graph.add_edge("chattingAgent", END)

    # -------- Planning → parallel solvers --------
    graph.add_edge("PlanningAgent", "agent1")
    graph.add_edge("PlanningAgent", "agent2")
    graph.add_edge("PlanningAgent", "agent3")
    graph.add_edge("PlanningAgent", "agent4")

    # -------- Solvers → Synthesizer --------
    graph.add_edge("agent1", "SynthesizerAgent")
    graph.add_edge("agent2", "SynthesizerAgent")
    graph.add_edge("agent3", "SynthesizerAgent")
    graph.add_edge("agent4", "SynthesizerAgent")

    # -------- Synthesis → Input generation --------
    graph.add_edge("SynthesizerAgent", "InputGeneratorAgent")

    # -------- Input → Execution --------
    graph.add_edge("InputGeneratorAgent", "ExecutorAgent")

    # -------- Execution routing --------
    graph.add_conditional_edges(
        "ExecutorAgent",
        execution_router,
        {
            "success": END,
            "error": "OrchestratorAgent"
        }
    )

    memory = MemorySaver()
    return graph.compile(checkpointer=memory)
