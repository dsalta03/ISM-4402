#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
# Starting the dataset
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]

# Creating the dataset
DegreeList = zip(names,grades, bsdegrees, msdegrees, phddegrees)
df = pd.DataFrame(data=DegreeList,columns=['Names','Grades', 'BS', 'MS', 'PhD'])
df


# In[16]:


# Computing Aggregate Statistics
print('The number of students having their PhD: ')
df['PhD'].count() # number of values


# In[19]:


# Other Measures of Central Tendency
# mode = the most common single value
df['Grades'].mode()


# In[21]:


# Computing Variance
# computes the variance of the values in a column
df['BS'].var()


# In[22]:


#Computing Variance on All Numeric Columns
df.var()


# In[ ]:




