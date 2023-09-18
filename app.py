import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# From here down is all the StreamLit UI.
st.set_page_config(page_title="JeevesBot", page_icon=":robot:")
st.header("Good day, I am JeevesBot 🤵 How may I assist you?")


if "sessionMessages" not in st.session_state:
     st.session_state.sessionMessages = [
        SystemMessage(content="You are a snobby, upper-crust British butler.")
    ]



def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    assistant_answer  = chat(st.session_state.sessionMessages )
    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content


def get_text():
    input_text = st.text_input("You: ", key= input)
    return input_text

chat = ChatOpenAI(temperature=0)

user_input=get_text()
submit = st.button('Generate')  

if submit:
    response = load_answer(user_input)
    st.subheader("Jeeves:")
    st.write(response,key= 1)
