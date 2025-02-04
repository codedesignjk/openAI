from dotenv import load_dotenv
import os
import openai

# Load .env file
load_dotenv()

# Set OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=openai_api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
             "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Who is the Prime Minister of India?"
        }
    ]
)

print(completion.choices[0].message)
