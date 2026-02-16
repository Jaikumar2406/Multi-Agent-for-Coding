from typing import TypedDict, Literal, Optional, List , Any
from pydantic import BaseModel , Field

class stateAgent(TypedDict , total=False):
    question:str
    mode:Literal["Problem" , "Chat"]
    planning :str
    agent1:str
    agent2:str
    agent3:str
    agent4:str
    agent1_response:str
    agent2_response:str
    agent3_response:str
    agent4_response:str
    Synthesizer:str
    param : list
    status:str
    max_try:int
    trying:int
    messages: List[dict]
    error : str


class StructureOutput(BaseModel):
    mode: Literal["Problem", "Chat"] = Field(..., description="Decides whether input is a problem or normal chat")
    problem: str = Field(..., description="LLM-understood problem statement for PlannerAgent")
    question :str= Field(..., description="LLM-understood what are the user question in short approx 1 to 2 lines PlannerAgent")


class plaining_output(BaseModel):
    agent1:str = Field(..., description="Task assigned to solver agent 1")
    agent2:str = Field(..., description="Task assigned to solver agent 2")
    agent3:str = Field(..., description="Task assigned to solver agent 3")
    agent4:str = Field(..., description="Task assigned to solver agent 4")

class InputGeneratorOutput(BaseModel):
    param: List[Any] = Field(
        ...,
        description="Input values for calling the function, in correct order"
    )