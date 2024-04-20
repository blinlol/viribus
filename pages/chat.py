import streamlit as st
import time
import random
import bot

def typewrite(message: str):
    for s in message:
        yield s
        time.sleep(random.random() * 0)


def user(message: str):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(message)


def assistant(question):
    with st.chat_message("assistant", avatar="🤖"):
        answer = bot.answer(prompt)
        response = st.write_stream(typewrite(answer))
    st.session_state.messages.append({"role": "assistant", "content": response})


def answer_is_good():
    pass


def answer_is_bad():
    pass


st.title("MAKAKI V ATAKE")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.uid = random.randint(0, 1 << 64)

for message in st.session_state.messages:
    if message["role"] == "assistant":
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message["content"])
    elif message["role"] == "user":
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(message["content"])

if prompt := st.chat_input("Any quetions?"):
    user(prompt)
    assistant(prompt)

    st.write("Is answer good?")
    st.button("yes", on_click=answer_is_good())
    st.button("no", on_click=answer_is_bad())