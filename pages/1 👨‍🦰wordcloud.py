import streamlit as st
import pandas as pd
import pythainlp
from pythainlp.corpus.common import thai_stopwords
from pythainlp import word_tokenize
from wordcloud import WordCloud, STOPWORDS
#import matplotlib as plt
import matplotlib.pyplot as plt
import pickle


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

df_pos = dftext[dftext['sentiment'] == 'pos']
pos_word_all = " ".join(text for text in df_pos['text_tokens'])
#st.write(pos_word_all)

st.header("Positive ")
import matplotlib as mpl
mpl.font_manager.fontManager.addfont('THSarabunNew.ttf')
reg = r"[ก-๙a-zA-Z']+"
fp = 'THSarabunNew.ttf'
wordcloud = WordCloud(stopwords=thai_stopwords, background_color = 'white', max_words=2000, height = 2000, width=4000, font_path=fp, regexp=reg).generate(pos_word_all)
fg1=plt.figure(figsize = (30,8))
plt.imshow(wordcloud)
plt.axis('off')
st.pyplot(fg1)
plt.show()


st.header("Negative ")
#import matplotlib as mpl
df_neg = dftext[dftext['sentiment'] == 'neg']
neg_word_all = " ".join(text for text in df_neg['text_tokens'])
wordcloud2 = WordCloud(stopwords=thai_stopwords, background_color = 'white', max_words=2000, height = 2000, width=4000, font_path=fp, regexp=reg).generate(neg_word_all)
fg2=plt.figure(figsize = (30,8))
plt.imshow(wordcloud2)
plt.axis('off')
st.pyplot(fg2)
plt.show()