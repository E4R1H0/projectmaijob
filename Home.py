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

st.image('./pic/what-is-sentiment-analysis-cover.jpg')
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


html_3 = """
<div style="background-color:#363062;padding:25px;border-radius:15px; border: 3px double #ffffff;">
<center><h5>การวิเคราะห์ความรู้สึกของลูกค้าเป็นกระบวนการที่สำคัญในธุรกิจและบริการต่างๆ เพื่อเข้าใจและตอบสนองต่อความต้องการของลูกค้าได้อย่างมีประสิทธิภาพ การเข้าใจความรู้สึกของลูกค้ามีประโยชน์ในหลายด้านที่สามารถช่วยธุรกิจเติบโตและสร้างความพึงพอใจของลูกค้าได้
วิจัยนี้ได้ออกแบบและพัฒนาระบบการวิเคราะห์ความรู้สึกของลูกค้าโดยได้ทำการทดลองจำแนกข้อมูลด้วยเทคนิคsentiment analysis จำนวน 3 เทคนิค ได้แก่ 1 Logistic Regression  2 Naive Bayes 3 Support  Vector  Machines  (SVM)กับชุดข้อมูล Samsung reviewข้อมูลประกอบด้วย 254 แถว 2 คอลัมน์ 2 คลาสเพื่อหาเทคนิคที่มีประสิทธิภาที่สุดเพื่อนำไปพัฒนาเป็นระบบ
ผลการทดลอง เทคนิคที่ให้ประสิทธิภาพสูงสุดคือ Naive Bayes ให้ค่า91% รองลงมาคือ Logistic Regression ให้ค่า86%สุดท้ายคือเทคนิค Support  Vector  Machines  (SVM)ให้ค่า 82%
สรุปผลเทคนิคที่ให้ประสิทธิภาพที่ดีที่สุดคือ
Naive Bayesเนื่องจากให้ค่า accuracy สูงที่สุด
</h5></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")



html_2 = """
<div style="background-color:#363062;padding:25px;border-radius:15px; border: 3px double #ffffff;">
<center><h5>Customer sentiment analysis is a critical process for businesses and services to understand and respond to customer needs effectively. Understanding customer sentiment can benefit businesses in many ways, such as helping them grow and increase customer satisfaction.
This research designed and developed a customer sentiment analysis system. The system was evaluated using three sentiment analysis techniques: 1) logistic regression, 2) naive Bayes, and 3) support vector machines (SVM) on a Samsung review dataset consisting of 254 rows, 2 columns, and 2 classes. The goal of the evaluation was to identify the most efficient technique to develop into a system.
The results of the evaluation showed that naive Bayes was the most efficient technique, with an accuracy of 91%. Logistic regression was second, with an accuracy of 86%, and support vector machines (SVM) was third, with an accuracy of 82%.
</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

html_4 = """
<div style="background-color:#363062;">
<center><h5 style="text-indent: 50%;">Nonthakan Jarpun 64/44 004</h5></center>
</div>
"""
st.markdown(html_4, unsafe_allow_html=True)
st.markdown("")