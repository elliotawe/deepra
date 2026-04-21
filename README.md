# Deep Research Agent 🚀

A sophisticated, autonomous research assistant built with LangChain and Claude Sonnet. This agent is designed to perform deep dives into complex topics by delegating specific research tasks to specialized sub-agents and synthesizing the findings.

> [!NOTE]
> **Operational Cost:** Running a comprehensive research task with this agent typically costs around **$1.48** in API usage (using Claude 3.5 Sonnet).

## ✨ Features

- **Hierarchical Delegation:** Uses a lead agent to orchestrate the research workflow and specialized sub-agents for focused data gathering.
- **Deep Web Integration:** Powered by [Tavily](https://tavily.com/), the agent searches the live web for the most up-to-date information.
- **Smart Content Parsing:** Automatically fetches webpage content and converts HTML into clean Markdown for processing.
- **Comprehensive Citation System:** Automatically tracks sources across all sub-agents and generates formatted inline citations `[1]` and a final "Sources" section.
- **Structured Reporting:** Automatically generates professional reports (`final_report.md`) with intelligent layouts for comparisons, lists, or overviews.
- **Efficient Parallelization:** Smart delegation logic that parallelizes research for comparisons while maintaining token efficiency for general queries.
- **Tool Call Budgets:** Built-in limits on search iterations to prevent infinite loops and manage API costs.

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** [LangChain](https://www.langchain.com/) / LangGraph
- **LLM:** Anthropic Claude 3.5 Sonnet
- **Search API:** Tavily
- **Core Library:** `deepagents`

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- [Anthropic API Key](https://console.anthropic.com/)
- [Tavily API Key](https://tavily.com/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd deep-research-agent
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory based on `.env.example`:
   ```bash
   cp .env.example .env
   # Then edit .env and add your API keys
   ```

## 📖 Usage

To start a research task, run the main entry point:

```bash
python main.py
```

By default, the agent is configured to research "Python vs JavaScript for web development". You can modify the query in `main.py`:

```python
# main.py
query = "Your custom research topic here"
```

## 🏗️ Architecture & Workflow

The project is structured as a clean Python package for maintainability:

-   `main.py`: The entry point for the application.
-   `src/deep_research/`: Core package containing agent logic.
    -   `agent.py`: Agent initialization and hierarchy.
    -   `prompts.py`: Research methodology and delegation instructions.
    -   `tools.py`: Search and web-parsing tools.
-   `.env.example`: Template for required environment variables.


## 📄 License

[MIT License](LICENSE) (or your preferred license)
