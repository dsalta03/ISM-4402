#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Load Data from CSV
import pandas as pd
Location = "datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

# We import the numpy library
import numpy as np

# create a column for timemgmt that shows busy if a student
# exercises more than three hours per week AND studies more than
# seventeen hours per week
df['timemgmt'] = np.where((df['exercise']>3) & (df['hours']>17),'busy', '-')
df.tail(10)


# In[ ]:




