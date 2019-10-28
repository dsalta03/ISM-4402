#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Pie Charting Your Dataset
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)
df


# In[3]:


#Creating New Column
df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']
df


# In[4]:


#Creating Pie Chart of Demerits
plt.pie(df['TotalDemerits'])


# In[10]:


#Creating a Customized Pie Chart
plt.pie(df['TotalDemerits'],
#This adds the students' names as labels to the pie pieces.
labels=df['Names'],
#This is what explodes out the pie piece for the fifth student. You can increase or decrease the 
#amount to your liking.
explode=(0,0,0,0.25,0),
#This is what rotates the pie chart to different
#points.
startangle=180,
#This is what formats the numeric labels on
#the pie pieces.
autopct='%1.1f%%',)
plt.axis('equal')

plt.show()


# In[ ]:




