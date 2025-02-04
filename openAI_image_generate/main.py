import os
from dotenv import load_dotenv
import openai
from openai import OpenAI
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Define a function to generate an image based on a prompt
def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        #size="256x256",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url

# Streamlit UI
st.title("DALL-E Image Generator")

# Input prompt from user
prompt = "Create a image for a cat sitting on the chair."


# Generate and display the image
if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        try:
            image_url = generate_image(prompt)
            st.image(image_url, caption=prompt, use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")

