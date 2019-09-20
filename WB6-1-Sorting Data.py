#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[16]:


# Sorting by name, age, and then grade, Ascending
df = df.sort_values(by=['fname', 'age', 'grade'],ascending=[True, True, True]) 
df.head()


# In[ ]:





# In[ ]:




