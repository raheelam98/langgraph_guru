# langgraph_guru
From Fundamentals to Advanced Techniques with Python and FastAPI on VSCode

[ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)

**rm note :**A chat prompt either sends content to the LLM as a human message or receives a response back from the LLM as an AI-generated answer.

```bash
from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "write message"
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)
```
