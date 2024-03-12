import os
import streamlit as st
from langchain_openai import ChatOpenAI


# os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


# mixtral = ChatOpenAI(
#     model = "mixtral-8x7b-32768",
#     openai_api_base = "https://api.groq.com/openai/v1",
#     openai_api_key = st.secrets["GROQ_API_KEY"]
# )

mixtral = ChatOpenAI(
    model = "mistralai/Mixtral-8x7B-Instruct-v0.1",
    openai_api_base = "https://api.endpoints.anyscale.com/v1",
    openai_api_key = st.secrets["ANYSCALE_API_KEY"]
)

st.header("🧘 Learn through Socratic Method.")
st.write("Learn any topic through dialogues. 📒")

# Define the levels
levels = ["a child", "a teen", "a college student", "a grad student", "an expert"]

# Create a text input for the topic
topic = st.text_input("Enter a topic")

# Create a dropdown for the level selection
level = st.selectbox("Select a level", levels)

# topic = "Zero Knowledge Proof"
# level = "a child"
prompt = f"Explain the {topic} - by simulating a conversation between the domain expert of {topic} and {level}."


# Button to trigger the conversation
if st.button("teach me this"):
    response = mixtral.invoke(prompt)
    st.write(response.content)





