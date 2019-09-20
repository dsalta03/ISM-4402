#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Creating a dataset
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
columns=['Names', 'Grades'])
df


# In[3]:


# Filtering out impossible grades
df.loc[df['Grades'] <= 100]


# In[6]:


# Replacing all subzero grades with a grade of 0
df.loc[(df['Grades'] < 0,'Grades')] = 0


# In[8]:


# Listing the table again
df


# In[ ]:




