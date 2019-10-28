#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing Dataset from CSV File
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[4]:


#Creating a Histogram not Creating a Box Plot
df.hist()


# In[8]:


#Simple Histogram. Creating Histogram for Single Column
df.hist(column="age")


# In[7]:


#Categorized Histogram
df.hist(column="age", by="gender")


# In[ ]:




