#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd   #importing libraries


# In[2]:


d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')      #creating lambda function for accessing the data in date time format.
df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)  #parse_date will convert the date object into date-time data type.


# In[3]:


df.head()


# In[4]:


df.loc[0, 'Date'].day_name()     #day_name will fetch the day for perticular date.


# In[5]:


df['Date'].dt.day_name()          #fetched the day for whole df


# In[6]:


df['DayOfWeek'] = df['Date'].dt.day_name()   #added it to the df.


# In[7]:


df


# In[8]:


df['Date'].min()               #Earliest date in df


# In[9]:


df['Date'].max()               #Most recent date in df.


# In[10]:


df['Date'].max() - df['Date'].min()     #span between two dates.


# In[11]:


filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))  #fetching details betwwne dates.
df.loc[filt]    


# In[12]:


df.set_index('Date', inplace=True)  #setting index as date. This will make slicing easy.


# In[13]:


df


# In[14]:


df['2019']


# In[15]:


df['2020-01':'2020-02']


# In[16]:


df['2020-01':'2020-02']['Close'].mean()  #getting mean for close column from jan to feb. 


# In[17]:


df['2020-01-01']['High'].max()    #max high value in jan month


# In[18]:


highs = df['High'].resample('D').max()    #resample is used fetch data. Like we can fetch data Day wise,week wise.
highs['2020-01-01']


# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


highs.plot()             #ploting the data. X-axis will be always time.


# In[21]:


df.resample('W').mean()


# In[22]:


df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})


# In[ ]:




