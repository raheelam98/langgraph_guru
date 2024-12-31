### Packages Requirement

### Launch the project with the LangGraph server
```bash
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev
```

[Research Rabbit - llama3.2 - Github](https://github.com/langchain-ai/research-rabbit?tab=readme-ov-file)

[Building a fully local research assistant from scratch with Ollama - 11 Dec 2024 - video](https://www.youtube.com/watch?v=XGuTzHoqlj8)

### Project Setup: Lang Graph with Poetry

Create a new directory for the project
```bash
mkdir reflection-agent
```

Change into the project directory
```bash
cd reflection-agent
```

Initialize a new poetry project
```bash
poetry init
```

List the files in the project directory  
```bash
ls
```

Display the contents of the pyproject.toml file
```bash
cat pyproject.toml
```

Add the specified dependencies to the project using poetry
```bash
poetry add python-dotenv black isort langchain langchain-openai langgraph langchain_google_genai
```

Install grandalf package using pip
```bash
pip install grandalf
```

Add the grandalf package to the project using poetry
```bash
poetry add grandalf
```

**Chatbot with Tools :** Integrate a web search tool into the bot.

First, install the requirements to use the [Tavily Search Engine](https://python.langchain.com/docs/integrations/tools/tavily_search/), and set your [TAVILY_API_KEY](https://tavily.com/).

```bash
poetry add tavily-python langchain_community
```

```bash
poetry add black isort
```

**Current virtual environment for your Poetry project**  

```bash
poetry env info --path
```

List all virtual environments associated with the current project

```bash
poetry env list
```

#### Run graph
 
https://mermaid.live/ 

