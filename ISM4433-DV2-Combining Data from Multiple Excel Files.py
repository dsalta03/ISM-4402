#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
#Import the glob library
import glob

# set all_data to an empty dataframe.
all_data = pd.DataFrame()

#This line will loop through all files that match the pattern.
for f in glob.glob("datasets/datasets/weekly_call_data/weekdata*.xlsx"):
    #Load the Excel file in f into the dataframe df
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
    
#Append the contents of df to the dataframe all_data.
all_data.describe()


# In[13]:


all_data.head()


# In[ ]:




