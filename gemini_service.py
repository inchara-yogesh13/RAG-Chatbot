import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Read the knowledge file only once when the server starts
with open("knowledge.txt", "r", encoding="utf-8") as file:
    knowledge = file.read()

documents = knowledge.split("----------------------------------")

def search_knowledge(question):

    question = question.lower()

    matches = []

    for doc in documents:

        if any(word in doc.lower() for word in question.split()):

            matches.append(doc)

    return "\n\n".join(matches) 
def get_ai_response(user_message):
    context = search_knowledge(user_message)

    prompt = f"""
You are a helpful AI assistant.

Below is some additional knowledge that may help answer the user's question.

Knowledge Base:
{knowledge}

User Question:
{user_message}

Instructions:
- If the knowledge base contains relevant information, use it in your answer.
- If the answer is not in the knowledge base, answer using your own knowledge.
- If both are useful, combine them naturally.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text