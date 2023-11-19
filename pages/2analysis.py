import streamlit as st
import pandas as pd
import pythainlp
from pythainlp.corpus.common import thai_stopwords
from pythainlp import word_tokenize
from wordcloud import WordCloud, STOPWORDS
#import matplotlib as plt
import matplotlib.pyplot as plt


df = pd.read_csv('./samsungreview.csv')
dftext=pd.DataFrame(df)
st.bar_chart(dftext['sentiment'].value_counts())
thai_stopwords = list(thai_stopwords())
#st.write(thai_stopwords)

def text_process(text):
    final = "".join(u for u in text if u not in ("?", ".", ";", ":", "!", '"', "ๆ", "ฯ"))
    final = word_tokenize(final)
    final = " ".join(word for word in final)
    final = " ".join(word for word in final.split()
                     if word.lower not in thai_stopwords)
    return final

dftext['text_tokens'] = dftext['text'].apply(text_process)

from sklearn.model_selection import train_test_split
X = dftext[['text_tokens']]
y = dftext['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn.feature_extraction.text import CountVectorizer
cvec = CountVectorizer(analyzer=lambda x:x.split(' '))
cvec.fit_transform(X_train['text_tokens'])
#cvec.vocabulary_

train_bow = cvec.transform(X_train['text_tokens'])
pd.DataFrame(train_bow.toarray(), columns=cvec.get_feature_names_out(), index=X_train['text_tokens'])

from sklearn.naive_bayes import MultinomialNB
naive_bayes_model = MultinomialNB()
naive_bayes_model.fit(train_bow, y_train)


#from sklearn.metrics import confusion_matrix,classification_report
#predictions_nb = naive_bayes_model.predict(test_bow)
#test_bow = cvec.transform(X_test['text_tokens'])
##print(classification_report(predictions_nb, y_test))

my_text=st.text_area("กรุณาป้อนความคิดเห็นสำหรับใช้ในการวิเคราะห์")

if st.button("วิเคราะห์ความคิดเห็น"):
    my_tokens = text_process(my_text)
    my_bow = cvec.transform(pd.Series([my_tokens]))
    my_predictions = naive_bayes_model.predict(my_bow)
    my_predictions  
    
    st.button("ไม่วิเคราะห์ความคิดเห็น")
else:
    st.button("ไม่วิเคราะห์ความคิดเห็น")