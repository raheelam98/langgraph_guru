
# creating the reflector chain and the tweet reviosr chain
# Prompt to predict, review the output, revise it, and provide suggestions for improvement

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

# Prompt to predict, review the output, revise it, and provide suggestions for improvement
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendation for the user."
            "Always provide detailed recommendations, including requests for length, virality, style, etc."
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

# Generate a message and continuously revise it based on feedback 
# from the reflection prompt until achieve the perfect result.
generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
           "system",
           "You are a twitter techie influencer assistant tasked with writing excellent twitter posts." 
           "Generate the best twitter post possible for the user's request."
           "If the user provides critique, respond with a revised version of your previous attempts."
        ),
        # placehoder for reflection and revision
        MessagesPlaceholder(variable_name="messages")
    ]
)

# Connect Prompt to LLM and Create Chain

# Initialize the language model as an instance of ChatOpenAI.

# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
llm = ChatOpenAI()

# Create the generation chain by combining the generation prompt with the language model.
generation_chain = generation_prompt | llm

# Create the reflection chain by combining the reflection prompt with the language model.
reflection_chain = reflection_prompt | llm
