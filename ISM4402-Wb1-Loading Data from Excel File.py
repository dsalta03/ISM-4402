#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[20]:


Location = "ISM4402-AGE-dataset.xlsx"
df = pd.read_excel(Location)


# In[21]:


df.head()


# In[24]:


names = ['Bob','Jessica','Mary','John','Mel']


# In[25]:


grades = [76,95,77,78,99]


# In[26]:


GradeList = zip(names,grades)


# In[27]:


df = pd.DataFrame(data = GradeList,
columns=['Names','Grades'])
writer = pd.ExcelWriter('dataframe.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


# In[29]:


df.head()


# In[ ]:




