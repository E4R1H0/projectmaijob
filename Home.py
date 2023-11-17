import json
import time
import requests
import streamlit as st
#from streamlit_lottie import st_lottie
#from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.header("การวิเคราะห์ความรู้สึก(Sentiment Analysis)💯💯💯")
st.subheader("Nonthakan Jarpun 🐻 DATA SCIENCE NPRU")

col1, col2 = st.columns(2)
with col1:
    st.image('./pic/earth.jpg')
    #lot3="https://lottie.host/ab6efbe2-81bd-4dd5-a2a8-e9567db3ae42/Exp97i4ktM.json"
    #lottie3 = load_lottieurl(lot3)
    #st_lottie(lottie3)
with col2:
    st.image('./pic/DS1.jpg')
st.balloons()
