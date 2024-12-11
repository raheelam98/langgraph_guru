
from typing import List, Sequence

from dotenv import load_dotenv

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph

from chain import generation_chain, reflection_chain

#Load environment variables from .env file
load_dotenv()

# define nodes name
REFLECT = "reflect"
GENERATE = "generate"

# return chain to run node 

# Define the generation node function which receives an input 
# state (a sequence of messages).
def generation_node(state: Sequence[BaseMessage]):
    # Invoke the generation chain with the current state, 
    # where state is passed as a dictionary with "messages" as the key.
    return generation_chain.invoke({"messages": state})

# Define the reflection node function which receives a sequence of messages.
def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    # Invoke the reflection chain with the current messages,
    # where messages are passed as a dictionary with "messages" as the key.
    res = reflection_chain.invoke({"messages": messages})

    # Return the response as a list containing HumanMessage,
    # transforming the content from the LLM's response into a human message.
    return [HumanMessage(content=res.content)]


# Initialize the MessageGraph builder
builder: MessageGraph = MessageGraph()

# Add the generate node to the graph
builder.add_node(GENERATE, generation_node)

# Add the reflect node to the graph
builder.add_node(REFLECT, reflection_node)

# Set the entry point of the graph to the generate node (commented out alternative version)
# builder.set_entry_point(generation_node)

# Set the entry point of the graph to the generate node using the node name
builder.set_entry_point(GENERATE)

# Define a function to determine if the process should continue
def should_continue(state: List[BaseMessage]):
    if len(state) > 6:
        return END
    return REFLECT

# Add conditional edges from the generate node based on the should_continue function
builder.add_conditional_edges(GENERATE, should_continue)

# Add an edge from the reflect node back to the generate node
builder.add_edge(REFLECT, GENERATE)

# Compile the graph
graph = builder.compile()

# Print the graph representation in Mermaid syntax
print(graph.get_graph().draw_mermaid())

# Main entry point
if __name__ == '__main__':
    print("hi LangGraph")
    inputs = HumanMessage(content="""Make this tweet better:"
                          @LainChainAI

                          - newly Tool Calling feature is seriouly underated.
                          After a long wati. It's here- manking the implementation of agent accross different mosels with funtion calling
                          Mode a video covering their newest blog post
                                 """)
    
    response = graph.invoke(inputs)



