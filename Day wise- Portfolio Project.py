#!/usr/bin/env python
# coding: utf-8

# # COVID-19 DATASET - DAY WISE  

# In[2]:


import pandas as pd


# In[4]:


data = pd.read_csv(r"C:\Users\vinee\Desktop\day_wise.csv")


# In[5]:


data


# In[6]:


#1. # df.count()
    # df.isnull().sum()


# In[7]:


data.count()
#Null value means Missing values


# In[9]:


data.isnull().sum()


# In[10]:


#2. 
# import seaborn as.sns
# import matplotlib.pyplot.as.plt
# sns.heatmap(df.isnull())
# plt.show()


# In[12]:


import seaborn as sns


# In[13]:


import matplotlib.pyplot as plt


# In[15]:


sns.heatmap(data.isnull())
plt.show()


# ### Q.1) show the number of confirmed,deaths and recovered cases in each Date.

# In[16]:


data.head(2)


# In[22]:


#data.groupby('Date').sum().head(20)


# In[31]:


data.groupby('Date')['Confirmed'].sum().sort_values(ascending = False).head(10)


# In[32]:


data.groupby('Date')['Confirmed', 'Recovered'].sum()


# ## Q.2) Remove all the records where Confirmed Cases is less than 10.

# In[33]:


data.head(2)


# In[34]:


data.Confirmed<10


# ## Q.3) In which Date,maximum number of Confirmed cases were recorded? 

# In[39]:


data.head(2)


# In[42]:


data.groupby('Date').Confirmed.sum().sort_values(ascending=False).head(20)


# ## Q.4) In which Date,minimum number of Deaths cases were recorded ? 

# In[43]:


data.head(2)


# In[45]:


data.groupby('Date').Deaths.sum().sort_values(ascending = True).head(50)


# ## -By VIVEK.A -

# In[ ]:




