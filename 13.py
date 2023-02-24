#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import streamlit as st  # 🎈 data web app development


# In[2]:


import os
st.write(os.getcwd())


# In[3]:


#import text file 
df = pd.read_csv('C:\\Users\\tali\\Desktop\\Elad_project\\streamlit_app\\80123_Tali-11.txt', sep=',' , header=None, skiprows=[0])
print(df)


# In[4]:


#add headers after loading the DataFrame by directly assigning values to the df.columns attribute
df_header = pd.read_excel('C:/Users/tali/Desktop/Elad_project/streamlit_app/Copy of HeadersForFileName80123.xlsx', sheet_name='Sheet1')
headers = df_header.iloc[0, :].tolist()
df.columns = headers
print(df)


# In[5]:


from IPython.display import display
import pandas as pd
display(df)


# In[6]:


# Convert the 'time' column to a date-time format
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S %d/%m/%Y')


# In[7]:


import streamlit as st
st.write(df.style.highlight_max(axis=0))


# In[8]:


# extract 'Time' column and 'CO2' columns [1, 4, 7, 10, 13, 16]
df_co2_chart = df.iloc[:, [0, 1, 4, 7, 10, 13, 16]]


# In[9]:


# set 'Time' column as the index
df_co2_chart.set_index('Time', inplace=True)


# In[10]:


# create line chart with 'Time' on the y-axis and 'CO2' on the x-axis
st.line_chart(df_co2_chart)


# In[ ]:




