import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.subheader("----------------------------------------")
st.header("การวิเคราะห์ความรู้สึก(Sentiment Analysis)")
st.subheader("Nonthakan Jarpun 🐻 DATA SCIENCE NPRU")
st.subheader("----------------------------------------")



col1, col2,col3 = st.columns(3)
with col1:
    st.image('./pic/earth.jpg')
with col2:
    st.write("  ")
with col3:
    st.image('./pic/DS1.jpg')
st.balloons()

