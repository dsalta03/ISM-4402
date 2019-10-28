#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Creating a Scatter Plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#specifies that figures should be shown inline
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
#creates a scatter plot using the index of the
#dataframe as the x and the values of column Col as
#the y
plt.scatter(df['hours'], df['grade'])


# In[ ]:




