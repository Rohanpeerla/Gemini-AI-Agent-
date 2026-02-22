import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

load_dotenv()

def build_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

    agent = create_agent(
        model=llm,
        tools=[],  # add tools later if needed
    )

    return agent


if __name__ == "__main__":
    agent = build_agent()

    print("Conversational Agent Started (type 'exit' to quit)\n")

    # 🔥 Conversation history storage
    messages = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        # Add user message to history
        messages.append(("user", user_input))

        response = agent.invoke({"messages": messages})

        ai_message = response["messages"][-1].content
        print("AI:", ai_message)

        # Add AI response to history
        messages.append(("assistant", ai_message))