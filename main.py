import sys
import os

# Adding src to python path to ensure imports work correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from src.deep_research.agent import agent
from langchain.messages import HumanMessage
from langgraph.types import Overwrite

def main():
    print("[Deep Research Agent] Initializing...")
    
    # Example research query
    query = "Compare Python vs JavaScript for web development"
    
    print(f"[Deep Research Agent] Starting research on: {query}\n")
    
    try:
        for chunk in agent.stream(
            {
                "messages": [
                    HumanMessage(content=query)
                ]
            },
            stream_mode="updates",
        ):
            for node, update in chunk.items():
                if not update or not (messages := update.get("messages")):
                    continue
                msg_list = messages.value if isinstance(messages, Overwrite) else messages
                for msg in msg_list:
                    if hasattr(msg, "content") and msg.content:
                        print(msg.content)
    except Exception as e:
        print(f"\n[Deep Research Agent] An error occurred: {e}")

if __name__ == "__main__":
    main()
