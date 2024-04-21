import streamlit as st
import bot


imgs = ["bot/data_base/images/q.jpeg",
        "bot/data_base/images/q_2.jpg",
        "bot/data_base/images/q_3.jpg"]

options = [
    "-1 этаж север",
    "-1 этаж юг",
    "2 этаж"
]
canteen = st.selectbox("Which stolovka?", options=options)
img = imgs[options.index(canteen)]
st.write("Количество людей в столовой: ", bot.count_people(img))
with st.expander("фото"):
    st.image(img)
