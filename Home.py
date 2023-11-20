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
<div style="background-color:#363062;padding:25px;border-radius:15px; border: 2px double #ffffff;">
<center><h5>การวิเคราะห์ความรู้สึกของลูกค้าเป็นกระบวนการที่สำคัญในธุรกิจและบริการต่างๆ เพื่อเข้าใจและตอบสนองต่อความต้องการของลูกค้าได้อย่างมีประสิทธิภาพ การเข้าใจความรู้สึกของลูกค้ามีประโยชน์ในหลายด้านที่สามารถช่วยธุรกิจเติบโตและสร้างความพึงพอใจของลูกค้าได้
ปัญหาที่พบในการทำความรู้สึกของลูกค้า เกิดจากปริมาณข้อมูลที่มากมายจากการรีวิวและคะแนนจากลูกค้า นี่คือปริมาณข้อมูลที่มากเกินไปที่อาจทำให้เรายากที่จะสกัดความสำคัญออกจากข้อมูลที่ไม่สำคัญ การคัดแยกความรู้สึกอาจจะล้าช้าในการตอบสนองต่อความต้องการของลูกค้า และการปรับปรุงบริการอาจไม่ทันสมัยตามความต้องการของลูกค้า
ผู้วิจัยได้เห็นถึงความสำคัญของการวิเคราะห์  ความรู้สึกของลูกค้าและแก้ปัญหาความล้าช้าในการวิเคราะห์ความรู้สึก จึงใช้วิธีการที่มีประสิทธิภาพและรวดเร็วเพื่อแก้ปัญหาให้ทันต่อการปรับปรุงสินค้าหรือบริการให้ทันกับความต้องการของลูกค้าโดยผู้จัดทำ ได้ทำการทดลองจำแนกข้อมูลด้วยเทคนิคsentiment analysis จำนวน 3 เทคนิค ได้แก่ 1 Logistic Regression  2 Naive Bayes 3 Support  Vector  Machines  (SVM)กับชุดข้อมูล Samsung reviewข้อมูลประกอบด้วย 210 แถว 2 คอลัมน์ 2 คลาส
ผลการทดลอง เทคนิคที่ให้ประสิทธิภาพสูงสุดคือ Naive Bayes ให้ค่า94% รองลงมาคือ Logistic Regression ให้ค่า89%สุดท้ายคือเทคนิค Support  Vector  Machines  (SVM)ให้ค่า 84%
สรุปผลเทคนิคที่ให้ประสิทธิภาพที่ดีที่สุดคือ
Naive Bayesเนื่องจากให้ค่า accuracy สูงที่สุด

</h5></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")



html_2 = """
<div style="background-color:#363062;padding:25px;border-radius:15px; border: 2px double #ffffff;">
<center><h5>Customer sentiment analysis is an important process for businesses and services to understand and respond to customer needs effectively. Understanding customer sentiment can be beneficial in many ways that can help businesses grow and create customer satisfaction.
The problem with customer sentiment analysis is that it comes from the large amount of data from customer reviews and ratings. This is too much data that can make it difficult to extract the important from the unimportant. Sentiment classification may be delayed in responding to customer needs, and service improvements may not be up-to-date with customer needs.
The researcher saw the importance of customer sentiment analysis and found a way to solve the problem of delayed sentiment analysis. Therefore, they used an efficient and fast method to solve the problem of being able to improve products or services in time with customer needs. The researcher conducted an experiment to classify data using 3 sentiment analysis techniques: 1. Logistic Regression 2. Naive Bayes 3. Support Vector Machines (SVM) with the Samsung review dataset. The data consists of 210 rows, 2 columns, and 2 classes.
The results of the experiment, the technique that gave the highest performance was Naive Bayes, giving a value of 94%, followed by Logistic Regression, giving a value of 89%. Finally, the Support Vector Machines (SVM) technique gave a value of 84%.
In conclusion, the technique that gives the best performance is Naive Bayes because it gives the highest accuracy.


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