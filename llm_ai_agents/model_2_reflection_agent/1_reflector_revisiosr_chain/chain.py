
# creating the reflector chain and the reviosr chain

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

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

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
           "system",
           "You are a twitter techie influencer assistant tasked with writing excellent twitter posts." 
           "Generate the best twitter post possible for the user's request."
           "If the user provides critique, respond with a revised version of your previous attempts."
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

#llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
llm = ChatOpenAI()
generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm

