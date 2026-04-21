from datetime import datetime

from .prompts import RESEARCH_WORKFLOW_INSTRUCTIONS, SUBAGENT_DELEGATION_INSTRUCTIONS, RESEARCHER_INSTRUCTIONS
from .tools import search
from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model

from langchain.messages import HumanMessage
from langgraph.types import Overwrite

max_concurrent_research_units = 3
max_researcher_iterations = 3

current_date = datetime.now().strftime("%Y-%m-%d")

INSTRUCTIONS = (
    RESEARCH_WORKFLOW_INSTRUCTIONS
    + "\n\n"
    + "=" * 80
    + "\n\n"
    + SUBAGENT_DELEGATION_INSTRUCTIONS.format(
        max_concurrent_research_units=max_concurrent_research_units,
        max_researcher_iterations=max_researcher_iterations,
    )
)

research_sub_agent = {
    "name": "research-agent",
    "description": "Delegate research to the sub-agent. Give one topic at a time.",
    "system_prompt": RESEARCHER_INSTRUCTIONS.format(date=current_date),
    "tools": [search],
}

model = init_chat_model(model="anthropic:claude-sonnet-4-5-20250929", temperature=0.0)

agent = create_deep_agent(
    model=model,
    tools=[search],
    system_prompt=INSTRUCTIONS,
    subagents=[research_sub_agent],
)