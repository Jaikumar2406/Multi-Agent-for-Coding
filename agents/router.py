from stateAgent.stateAgent import stateAgent 


def execution_router(state: stateAgent) -> str:
    if state.get("status") == "success" or state.get("max_try", 0) >= 5:
        return "success"
    return "error"


def route_from_planner(state: stateAgent) -> str:
    mode = state.get("mode", "Chat")

    if mode == "Chat":
        return "Chat"

    return "Problem"

