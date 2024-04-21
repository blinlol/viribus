import streamlit as st
import time
import random
import bot

def typewrite(message: str):
    for s in message:
        yield s
        time.sleep(random.random() * 0.03)


def user(message: str):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(message)


def history():
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(message["content"])
        elif message["role"] == "user":
            with st.chat_message("user", avatar="🧑‍💻"):
                st.markdown(message["content"])
    if "bad" in st.session_state and st.session_state.bad:
        q, c = st.session_state.bad
        assistant(q, c)
        st.session_state.bad = []


def assistant(question, context=0):
    with st.chat_message("assistant", avatar="🤖"):
        answer, link = bot.answer(question, context)
        response = st.write_stream(typewrite(answer))
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    for title, url in link.items():
        st.link_button(title, url)

    if "Пожалуйста будьте Культурными!" not in answer and context < 3:
        st.write("Is answer good?")
        st.button("yes", on_click=answer_is_good, args=[response])
        st.button("no", on_click=answer_is_bad, args=[question, context + 1])


def answer_is_good(response):
    pass


def answer_is_bad(quetion, context):
    del st.session_state.messages[-1]
    st.session_state.bad = [quetion, context]

st.markdown("""
# QuantumMind Chat 🧠
""")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.uid = random.randint(0, 1 << 64)

history()

if prompt := st.chat_input("Any quetions?"):
    user(prompt)
    assistant(prompt)
