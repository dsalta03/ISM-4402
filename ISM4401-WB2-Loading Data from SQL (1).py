#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
from sqlalchemy import create_engine

# Connect to sqlite db
db_file = r'datasets/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))

#To see the names of a table, we use this code
sql = "select name from sqlite_master where type = 'table';"

#loads the data resulting from that query into the dataframe
sales_data_df = pd.read_sql(sql, engine)

#Now, to see the fields as headers at the top of each column, we enter the code
sales_data_df.head()


# In[13]:


#To see all the data from scores table
sql = "select * from scores;"
#loads the data resulting from that query into the dataframe
scores_df = pd.read_sql(sql, engine)
#Now, to see the fields as headers at the top of each column, we enter the code
scores_df.head()


# In[ ]:




