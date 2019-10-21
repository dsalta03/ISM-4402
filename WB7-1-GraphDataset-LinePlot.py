#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Line Plotting Your Dataset
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[9]:


#Code to Plot a Customized Graph
import matplotlib.pyplot as plt
df.plot()
#displayText: the text we want to show for this annotation
#xloc, yloc: the coordinates of the data point we want to annotate
#xtext, ytext: coordinates of where we want thetext to appear using the coordinate system specified in textcoords
#xycoords: sets the coordinate system to use to find the data point; it can be set separately for x and y
#textcoords: sets the coordinate system to use to place the text
displayText = "Wow!"
xloc = 0
yloc = 76
xtext = 0
ytext = 0
plt.annotate(displayText,
xy=(xloc, yloc),
xytext=(xtext,ytext),
xycoords=('axes fraction', 'data'),
textcoords='offset points')


# In[7]:


#Code to Plot a Customized Graph
df.plot()
displayText = "Wow!"
xloc = 0
yloc = 76
xtext = 180
ytext = 100
plt.annotate(displayText,
xy=(xloc, yloc),
arrowprops=dict(facecolor='black',
shrink=0.05),
xytext=(xtext,ytext),
xycoords=('axes fraction', 'data'),
textcoords='offset points')


# In[ ]:




