#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd


# In[13]:


pd.read_csv("florida-hispanic-dataset.csv")


# In[14]:


names = ['Bob','Jessica','Mary','John','Mel']


# In[15]:


grades = [76,95,77,78,99]


# In[16]:


GradeList = zip(names,grades)


# In[17]:


df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])


# In[18]:


df.to_csv('florida-hispanic-dataset.csv',index=False,header=False)


# In[19]:


pd.read_csv("florida-hispanic-dataset.csv")


# In[21]:


df.head()


# In[ ]:




