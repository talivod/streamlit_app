#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import streamlit as st  # 🎈 data web app development


# In[33]:


#import text file 
df = pd.read_csv('C:\\Users\\tali\\Desktop\\Elad_project\\80123_Tali.txt', sep=',' , header=None, skiprows=[0])
print(df)


# In[34]:


#add headers after loading the DataFrame by directly assigning values to the df.columns attribute
df_header = pd.read_excel('C:/Users/tali/Desktop/Elad_project/Copy of HeadersForFileName80123.xlsx', sheet_name='Sheet1')
headers = df_header.iloc[0, :].tolist()
df.columns = headers
print(df)


# In[35]:


from IPython.display import display
import pandas as pd
display(df)


# In[36]:


import streamlit as st
st.write(df.style.highlight_max(axis=0))


# In[ ]:





# In[ ]:




