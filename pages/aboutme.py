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
<center><h4>นายนนทกานต์ จ่าพันธุ์ 644285004 64/44</h4><h5>สาขาวิทยาการข้อมูล\tคณะวิทยาศาสตร์และเทคโนโลยี\nมหาวิทยาลัยราชภัฏนครปฐม</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

st.image('./pic/1.png')
