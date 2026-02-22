import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

load_dotenv()

st.set_page_config(page_title="Gemini AI Agent", page_icon="🤖")
st.title("🤖 Gemini 2.5 Flash Conversational Agent")

# Initialize session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Build agent
@st.cache_resource
def load_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )
    return create_agent(model=llm, tools=[])

agent = load_agent()

# Display chat history
for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(message)

# User input
if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append(("user", prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    response = agent.invoke({"messages": st.session_state.messages})
    ai_reply = response["messages"][-1].content

    st.session_state.messages.append(("assistant", ai_reply))

    with st.chat_message("assistant"):
        st.markdown(ai_reply)