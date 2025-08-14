import os
from turtle import mode
from dotenv import find_dotenv, load_dotenv
from langchain_groq import ChatGroq


load_dotenv(find_dotenv())
api__key = str(os.getenv("GROQ_API_KEY"))

model = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    groq_api_key=api__key,
    max_tokens=1000,
    temperature=0.5)

print("Model initialized successfully.")
print(model.invoke("Write a code to check number is prime or not in python."))
