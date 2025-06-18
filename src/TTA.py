from Tools import add_task, get_tasks, ddg, get_time
from langchain_google_genai import ChatGoogleGenerativeAI
from Database import delete_all_tasks
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, SystemMessage
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode


from dotenv import load_dotenv
load_dotenv()  


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


tools = [add_task, get_tasks, delete_all_tasks, ddg, get_time]
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash").bind_tools(tools)

def model_call(state:AgentState) -> AgentState:
    system_prompt = SystemMessage(content=
        "You are my Task Tracker assistant, please answer my query to the best of your ability. And when user asks you to add a task, it is not necessary to ask for the deadline is the user does not specify it. Also Answer if the user gives a general question which is not related to tasks"
    )
    response = model.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}

def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"

graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)


tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("our_agent")

graph.add_conditional_edges(
    "our_agent",
    should_continue,
    {
        "continue": "tools",
        "end": END,
    },
)

graph.add_edge("tools", "our_agent")

app = graph.compile()