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


html_1 = """
<div style="background-color:#363062;padding:5px;border-radius:3px;border-bottom: 4px solid #ffffff;border-top: 4px solid #ffffff;">
<center><h4>การวิเคราะห์ความรู้สึกของลูกค้าร้านSamsung Thailand</h4><h5>Sentiment Analysis of customers of Samsung Thailand store</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

#st.header("การวิเคราะห์ความรู้สึก(Sentiment Analysis)")
#st.subheader("Nonthakan Jarpun 🐻 DATA SCIENCE NPRU")
#st.write("__________________________________________________")



col1, col2= st.columns(2)
with col1:
    st.image('./pic/earth.jpg')
with col2:
    st.image('./pic/DS1.jpg')
st.balloons()

