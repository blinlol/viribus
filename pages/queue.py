import streamlit as st
import bot
import pandas


@st.cache_data
def stolovka():
    return pandas.read_csv("bot/data_base/dist.csv")


imgs = ["bot/data_base/images/q.jpeg",
        "bot/data_base/images/q_2.jpg",
        "bot/data_base/images/q_3.jpg"]

options = [
    "-1 этаж север",
    "-1 этаж юг",
    "2 этаж"
]

st.title("QuantumMind Q-Checker 🧠")

st.text("Which stolovka?")
canteen = st.selectbox("", options=options)
img = imgs[options.index(canteen)]
st.write("Количество людей в столовой: ", bot.count_people(img))
with st.expander("фото"):
    st.image(img)

import plotly.graph_objects as go

data = stolovka()
fig = go.Figure(data=go.Scatter(x=data['dt'], y=data['n'], mode='lines+markers', marker_color='lightsalmon'))
fig.update_layout(title='Заполненность столовки по дням недели',
                  xaxis_title='Дни недели',
                  yaxis_title='Заполненность, %',
                  template='plotly_dark')

st.plotly_chart(fig)