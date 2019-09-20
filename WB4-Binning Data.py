#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
# Create the bin dividers
bins = [0, 80, 100]
# Create names for the four groups
group_names = ['fail', 'pass']


# In[2]:


# Cut Grades on passing or failing the program based on grade number. 
# In this example, it should be above 80.
df['masterprogram'] = pd.cut(df['grade'], bins, labels=group_names)
df


# In[3]:


# Count Number of Observations
pd.value_counts(df['masterprogram'])


# In[ ]:




