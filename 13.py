#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import streamlit as st  # 🎈 data web app development


# In[ ]:


#import text file 
df = pd.read_csv('C:\\Users\\tali\\Desktop\\Elad_project\\80123_Tali-11.txt', sep=',' , header=None, skiprows=[0])
print(df)

