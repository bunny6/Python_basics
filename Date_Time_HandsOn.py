
#importing libraries

import pandas as pd   


#creating lambda function for accessing the data in date time format.

d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p') 

#parse_date will convert the date object into date-time data type.

df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)  


df.head()

#day_name will fetch the day for perticular date.

df.loc[0, 'Date'].day_name()     

#fetched the day for whole df
  
df['Date'].dt.day_name()         

 #added it to the df.

df['DayOfWeek'] = df['Date'].dt.day_name()  

df


 #Earliest date in df


df['Date'].min()              


#Most recent date in df.


df['Date'].max()               


#span between two dates.


df['Date'].max() - df['Date'].min()     


#fetching details betwwne dates.


filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))  
df.loc[filt]    


 #setting index as date. This will make slicing easy.


df.set_index('Date', inplace=True) 




df





df['2019']

df['2020-01':'2020-02']


#getting mean for close column from jan to feb. 

df['2020-01':'2020-02']['Close'].mean()  


#max high value in jan month
df['2020-01-01']['High'].max()    





highs = df['High'].resample('D').max()    #resample is used fetch data. Like we can fetch data Day wise,week wise.
highs['2020-01-01']





get_ipython().run_line_magic('matplotlib', 'inline')



#ploting the data. X-axis will be always time.

highs.plot()             





df.resample('W').mean()





df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})






