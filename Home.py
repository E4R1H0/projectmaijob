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

html_2 = """
<div style="background-color:#363062;">
<center><h4>บทคัดย่อ</h4></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

html_3 = """
<div style="background-color:#363062;padding:25px;border-radius:5px;border: 2px solid #ffffff;">
<center><h5>วัตถุประสงค์ของงานวิจัยนี้ คือ เพื่อทำการวิเคราะห์ความรู้สึกของลูกค้า โดยการใช้วิธีการที่รวดเร็วเพื่อให้ทันต่อการปรับปรุงสินค้าหรือบริการให้ทันกับความต้องการของลูกค้าโดยผู้จัดทำได้ทำการทดลองจำแนกข้อมูลด้วยเทคนิคsentiment analysis จำนวน 3 เทคนิค ได้แก่ 1 Logistic Regression  2 Naive Bayes 3 Support  Vector  Machines  (SVM)กับชุดข้อมูล Samsung reviewข้อมูลประกอบด้วย 210 แถว 2 คอลัมน์ 2 คลาส
ผลการทดลอง เทคนิคที่ให้ประสิทธิภาพสูงสุดคือ Naive Bayes ให้ค่า94% รองลงมาคือ Logistic Regression ให้ค่า89%สุดท้ายคือเทคนิค Support  Vector  Machines  (SVM)ให้ค่า 84%
สรุปผลเทคนิคที่ให้ประสิทธิภาพที่ดีที่สุดคือNaive Bayesเนื่องจากให้ค่า accuracy สูงที่สุด
</h5></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")

