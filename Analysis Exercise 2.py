#!/usr/bin/env python
# coding: utf-8

# In[201]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[106]:


df.hist(edgecolor='black')


# In[202]:


df['Cars Sold'].mean()


# In[203]:


df['Cars Sold'].max()


# In[204]:


df['Cars Sold'].min()


# In[207]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[208]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[209]:


df['Years Experience'].mean()


# In[210]:


df[df['Years Experience']>3]['Hours Worked'].mean()


# In[211]:


pd.pivot_table(df, values=('Cars Sold'), index=['SalesTraining'])


# In[217]:


df.hist(column='Cars Sold', by='SalesTraining', 
        bins=13, color='yellow', edgecolor='black')
plt.title('Affect of Training on Number of Cars Sold',
             y=1.05, size=16)
plt.xlabel('Number of Cars')
plt.ylabel('Number of Employees')

plt.show()


# In[218]:


df.hist(column='Cars Sold', bins=13, color='yellow', 
        edgecolor='black')
plt.axvline(df['Cars Sold'].mean(), color='red', 
            linestyle='dashed', 
            linewidth=3, label='Mean')
plt.title('The Average Number of Cars Being Sold',
             y=1.05, size=16)
plt.xlabel('Number of Cars')
plt.ylabel('Number of Employees')
plt.show()


# In[226]:


plt.scatter(df['Cars Sold'], df['Hours Worked'])
plt.title('Affect of Hours Worked on Number of Cars Sold',
             y=1.05, size=16)
plt.xlabel('Number of Cars')
plt.ylabel('Number of Hours Worked')


# In[ ]:




