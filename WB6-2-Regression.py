#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
Location = "datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

#Create a new column where you convert gender to numeric values, like
# 1 for female and 0 for male. now add gender to your regression
def gen_to_num(x): 
    if x == 'female':
        return 1
    if x == 'male':
        return 0
    
df['gender_val'] = df['gender'].apply(gen_to_num)


# First Regression
import statsmodels.formula.api as sm

#It shows the dependent variable on the left of the tilde
#(~) and the independent variables we want considered on the right.
result = sm.ols(
formula='grade ~ age + exercise + hours + gender_val',
data=df).fit()
result.summary()


# In[12]:


# Second Regression
import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ exercise + hours + gender_val',
data=df).fit()
result.summary()


# In[ ]:




