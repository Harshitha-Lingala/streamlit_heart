import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df=pd.read_csv('heart.csv')

df_survived=df[df['chd']==0]
df_dead=df[df['chd']==1]

dead_famhist=df_dead.groupby('famhist')['chd'].count()
survived_famhist=df_survived.groupby('famhist')['chd'].count()

st.title('Family History of Heart Patients')

plt.subplot(2,1,1)
plt.pie(dead_famhist,labels=['Absent','Present'],autopct='%1.1f%%')
plt.title('Family History of Patients succumbed to Heart Disease : Present vs. Absent')


plt.subplot(2,1,2)
plt.pie(survived_famhist,labels=['Absent','Present'],autopct='%1.1f%%')
plt.title('Family History of Patients survived a Heart condition : Present vs. Absent')
plt.show()

st.pyplot(plt)