#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("survey_results_public.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[8]:


pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)


# In[9]:


df.head()


# In[10]:


schema_df=pd.read_csv("survey_results_schema.csv")


# In[11]:


schema_df


# In[12]:


df.tail()


# # Dataframe

# In[13]:


Info={"Name":["Shubham","Dileep","Sanad"],"Branch":["Computer","Entc","Mechanical"],"Email":["s@gmail.com","d@gmail.com","n@gmail.com"]}


# In[14]:


Info


# In[15]:


df1=pd.DataFrame(Info)


# In[16]:


df1


# In[17]:


df1['Email']


# In[18]:


df1[["Name","Email"]]


# In[19]:


type(df1['Email'])


# In[20]:


df1.columns


# In[21]:


df1.iloc[:,:] #simple way


# In[22]:


df1.iloc[[0,1,2],[0,1,2]]# 1st row and 2nd row with email column.


# # Practice on Dataset

# In[23]:


df.shape


# In[24]:


df.columns


# In[25]:


df.iloc[0:10,0:10]


# In[26]:


df["Hobbyist"]


# In[27]:


df["Hobbyist"].value_counts()


# In[28]:


df.iloc[:,2]


# In[29]:


df.iloc[[0],[1]]


# In[30]:


df.loc[0] #to print a row ------


# In[31]:


df.loc[[0,1,2],'Hobbyist']


# In[32]:


df.iloc[[0,1,2],[2]]


# In[33]:


df.loc[0:2,'Hobbyist':"Employment"]


# # Setting index

# In[34]:


Index=["First","Second","Third"]


# In[35]:


df1['Index']=Index


# In[36]:


df1


# In[37]:


df1.set_index('Index')


# In[38]:


df1


# In[39]:


df1.set_index('Index',inplace=True)


# In[40]:


df1


# In[41]:


df1


# In[42]:


df1.index


# In[43]:


df1.loc[["First","Second"],["Name","Email"]]


# In[44]:


df1.loc["First"]


# In[45]:


df.set_index('Respondent',inplace=True)


# In[46]:


df.head()


# In[47]:


df.loc[1:20,"MainBranch":"OpenSourcer"]


# In[48]:


df['Hobbyist']=='yes'


# In[49]:


high_salary=(df["ConvertedComp"]>70000)


# In[52]:


df.loc[high_salary,["Country","LanguageWorkedWith","ConvertedComp"]]


# In[53]:


countries=["India","United States","United Kingdom","Canada","Germany"]
filt=df["Country"].isin(countries)


# In[54]:


df.loc[filt,"Country"]


# In[57]:


df["LanguageWorkedWith"]


# In[58]:


filt=df["LanguageWorkedWith"].str.contains("Python",na=False)


# In[61]:


df.loc[filt,"LanguageWorkedWith"]


# In[62]:


df1


# In[64]:


df1.reset_index()


# In[76]:


dict1={"Name":["Shubham","Dileep","Ajay"],"Last":["Gharde","Yadav","Polke"],"Branch":["Comp","ENTC","CIVIL"]}


# In[77]:


dict1


# In[78]:


df2=pd.DataFrame(dict1)


# In[79]:


df2


# In[80]:


columns=df2.columns


# In[81]:


columns


# In[83]:


df2.columns=[x.upper() for x in columns]


# In[84]:


df2


# In[85]:


#to replace any spaces we do
#df.columns=df.columns.str.replace(" ","_")


# In[88]:


df2.rename(columns={"NAME":"First","LAST":"Last","BRANCH":"Branch"})


# In[ ]:


df2.loc[2]=["Yadav","Dileep"]


# In[89]:


df3=pd.read_excel("multi_threading_activity.xlsx")


# In[90]:


df3.head()


# In[92]:


df3.loc[0]


# In[94]:


df3.loc[0,"A"]


# In[95]:


df3.loc[0,"B"]


# In[96]:


df3.iloc[:,:]


# In[98]:


df3.isnull().sum()


# In[99]:


df3.value_counts()


# In[100]:


df3["A"].value_counts()


# In[104]:


import numpy as np


# In[112]:


df3['A'].replace("hdoisahdo",np.nan,inplace=True)


# In[113]:


df3["A"].mean()


# In[114]:


df3["A"]=df3["A"].fillna(3.978043050206615)


# In[115]:


df3.isnull().sum()


# In[116]:


df3["B"].value_counts()


# In[119]:


df3["B"]=pd.to_numeric(df3["B"], errors="coerce")


# In[120]:


df3["A"]=pd.to_numeric(df3["A"], errors="coerce")


# In[126]:


df3=df3.replace("NaN",0)


# In[128]:


df3["A+B"]=df3["A"]+df3["B"]


# In[129]:


df3


# In[130]:


df3.head()


# In[143]:


df3.loc[[2],["A","B"]]


# In[140]:


df3.iloc[0:3,:]


# In[144]:


df2


# In[145]:


df2["NAME"]=df2["NAME"].str.lower()


# In[146]:


df2


# In[147]:


df2["NAME"].apply(len)


# In[151]:


def update_branch(branch):
    return branch.upper()


# In[153]:


df2["BRANCH"].apply(update_email)


# In[154]:


df2["BRANCH"]=df2["BRANCH"].apply(lambda x:x.lower())


# In[155]:


df2


# In[156]:


df2.apply(pd.Series.min)


# In[158]:


df2.apply(lambda x:x.min())


# In[159]:


df2.applymap(len)


# In[161]:


df2.applymap(str.lower)


# In[162]:


df2


# In[163]:


df2["NAME"].map({'shubham':'harsh','dileep':'Sai',"ajay":"jayesh"})


# In[164]:


df2


# In[165]:


df2["NAME"]=df2["NAME"].replace({"shubham":"harsh","dileep":"Sai","ajay":"jayesh"})


# In[166]:


df2


# In[167]:


df


# In[169]:


columns=df.columns


# In[170]:


df.rename(columns={"ConvertedComp":"SalaryUSD"},inplace=True)


# In[173]:


df["SalaryUSD"]


# In[174]:


df["Hobbyist"].map({"Yes":True,"No":False})


# In[175]:


df["Hobbyist"]


# In[176]:


df["Hobbyist"]=df["Hobbyist"].map({"Yes":True,"No":False})


# In[177]:


df


# In[178]:


people={"First":["Shubham","Harsh","Utkarsh"],"Last":["Gharde","Kapoor","Banerjee"],"Email":["S@gmail.com","h@gmail.com","u@gmail.com"]}


# In[179]:


people


# In[180]:


df4=pd.DataFrame(people)


# In[181]:


df4


# In[182]:


df4["First"]+' '+df4["Last"]


# In[183]:


df4["Full_Name"]=df4["First"]+' '+df4["Last"]


# In[184]:


df4


# In[192]:


df4.drop(columns=["First","Last"],inplace=True) #if we write inplace=true, it will effect the df original value


# In[193]:


df4


# In[194]:


df4["Full_Name"].str.split(" ")


# In[195]:


df4["Full_Name"].str.split(" ",expand=True)# just a well designed df


# In[196]:


df4[["First","last"]]=df4["Full_Name"].str.split(" ",expand=True)# just a well designed df


# In[197]:


df4


# In[198]:


df4.append({"First":"Roy"},ignore_index=True)


# In[199]:


people1={"First":["Shubham","Harsh"],"Last":["Gharde","Kapoor"],"Email":["S@gmail.com","h@gmail.com"]}


# In[200]:


df5=pd.DataFrame(people1)


# In[201]:


df5


# In[211]:


df4=df4.append(df5,ignore_index=True,sort=False)


# In[212]:


df4


# In[214]:


df4.drop(index=4)


# In[215]:


filt3=df4['last']=="Banerjee"
df4.drop(index=df4[filt3].index)


# # Sorting the Data
# 

# In[216]:


people4={"First":["Shubham","Harsh","Utkarsh"],"Last":["Gharde","Kapoor","Banerjee"],"Email":["S@gmail.com","h@gmail.com","u@gmail.com"]}


# In[217]:


df6=pd.DataFrame(people4)


# In[218]:


df6


# In[219]:


df6.sort_values(by="Last",ascending=False)


# In[221]:


df6.sort_values(by=["Last","First"],ascending=True)


# In[222]:


df6.sort_values(by=["Last","First"],ascending=False)


# In[223]:


df6.sort_index()


# In[226]:


df6["Last"].sort_values()


# In[230]:


df.sort_values(by=["Country","SalaryUSD"],ascending=[True,False],inplace=True)


# In[231]:


df[['Country',"SalaryUSD"]].head(50)


# In[234]:


df["SalaryUSD"].nlargest(10)  #10 largest value from the column.


# In[235]:


df.nlargest(10,["SalaryUSD"])


# # Grouping and Aggregating

# In[236]:


df.head()


# In[237]:


df.describe()


# In[240]:


cat=[]
num=[]
for i in df:
    if df[i].dtype==object:
        cat.append(i)
    else:
        num.append(i)
    

    


# In[241]:


cat


# In[242]:


num


# In[247]:


df["SalaryUSD"].mean()


# In[248]:


df["CompTotal"].mean()


# In[249]:


df["CompTotal"].median()


# In[250]:


df["CompTotal"].count()


# In[253]:


df["Hobbyist"]


# In[254]:


df["Hobbyist"].value_counts()


# In[255]:


df["Hobbyist"].value_counts(normalize=True)


# In[257]:


country_grp=df.groupby(["Country"])


# In[260]:


country_grp.get_group("India")


# In[261]:


filt5=df["Country"]=="India"
df[filt5]


# In[262]:


filt5=df["Country"]=="India"
df.loc[filt5]["SocialMedia"].value_counts()


# In[264]:


country_grp["SocialMedia"].value_counts().loc["United States"]


# In[265]:


country_grp["SocialMedia"].value_counts(normalize=True).loc["United States"]


# In[266]:


country_grp['SalaryUSD'].median().loc['Germany']


# In[269]:


df["SalaryUSD"][6]


# In[270]:


country_grp['SalaryUSD'].agg(["median","mean"])


# In[271]:


country_grp['SalaryUSD'].agg(["median","mean"]).loc["Canada"]


# In[272]:


filt7=df["Country"]=="India"                          #filter for columns country =india
df.loc[filt]["LanguageWorkedWith"].str.contains("Python").sum()  # people who worked with python


# In[274]:


country_res=df["Country"].value_counts()
country_res


# In[ ]:


# how many people from each country use python? Solution is below.


# In[277]:


country_python=country_grp["LanguageWorkedWith"].apply(lambda x:x.str.contains("Python").sum())
country_python


# In[279]:


python_df=pd.concat([country_res,country_python],axis=1,sort=False)


# In[280]:


python_df


# In[287]:


python_df.rename(columns={"Country":"NumberOfResponses","LanguageWorkedWith":"Python"},inplace=True)


# In[288]:


python_df


# In[289]:


# python_df["pctknowspython"]=(part/whole)

python_df["pctknowspython"]=(python_df["Python"]/python_df["NumberOfResponses"])*100


# In[290]:


python_df


# In[291]:


#sorting people who knows python by percentage
python_df.sort_values(by="pctknowspython",ascending=False,inplace=True)


# In[292]:


python_df


# # Handling missing values and null values

# In[1]:


import numpy as np
import pandas as pd


# In[9]:


people={"First":["Shubham","Harsh","Ajay","Jayesh",np.nan,None,"NA"],"Last":["Gharde","Kapoor","Polke","Ahire",np.nan,np.nan,"Missing"],"Email":["S@gmail.com","h@gmail.com","a@gmail.com",None,np.nan,"An@gmail.com","NA",],"age":["33",'55',"66","36",None,None,"Missing"]}


# In[10]:


people


# In[11]:


df=pd.DataFrame(people)


# In[12]:


df


# In[13]:


df.dropna()


# In[14]:


df.dropna(axis="index",how="any")


# In[15]:


df.dropna(axis="index",how="all")


# In[17]:


df.dropna(axis="columns",how="all")


# In[19]:


df.dropna(axis="columns",how="any")  #getting empty df becoz each column have a nan value in it


# In[20]:


df


# In[21]:


df.isnull().sum()


# In[22]:


df.info()


# In[26]:


df["First"].mode()[0]


# In[48]:


df["First"]=df["First"].fillna("Ajay")


# In[49]:


df.isnull().sum()


# In[50]:


df


# In[34]:


df["Last"].mode()[0]


# In[51]:


df["Last"]=df["Last"].fillna("Ahire")


# In[36]:


df["Email"].mode()[0]


# In[37]:


df["Email"]=df["Email"].fillna("An@gmail.com")


# In[40]:


df["age"].mode()[0]


# In[44]:


df['age']=pd.to_numeric(df['age'],errors='coerce')


# In[45]:


df["age"].mean()


# In[46]:


df["age"]=df["age"].fillna(47.5)


# In[52]:


df.isnull().sum()


# In[57]:


df


# In[54]:


df["First"]=pd.to_numeric(df["First"],errors="coerce")


# In[70]:


df["First"]=df["First"].replace("NaN","Ajay")


# In[55]:


df["First"]=df["First"].fillna(df["First"].mean())


# In[56]:


df


# In[60]:


df["Last"].value_counts()


# In[62]:


df["Last"].mode()[0]


# In[64]:


df["Last"]=df["Last"].replace("Missing","Ahire")


# In[65]:


df


# In[68]:


df["First"]=df["First"].replace({"NaN":"Ajay"})


# In[71]:


df


# In[72]:


people1={"First":["Shubham","Harsh","Ajay","Jayesh",np.nan,None,"NA"],"Last":["Gharde","Kapoor","Polke","Ahire",np.nan,np.nan,"Missing"],"Email":["S@gmail.com","h@gmail.com","a@gmail.com",None,np.nan,"An@gmail.com","NA",],"age":["33",'55',"66","36",None,None,"Missing"]}


# In[74]:


df2=pd.DataFrame(people1)


# In[75]:


df2


# In[91]:


df2.replace("NA",np.nan,inplace=True)
df2.replace("Missing",np.nan,inplace=True)


# In[92]:


df2.isnull().sum()


# In[93]:


df2["First"].mode()[0]


# In[94]:


df2["First"]=df2["First"].fillna("Ajay")


# In[95]:


df2


# In[96]:


df2["Last"].mode()[0]


# In[97]:


df2["Last"]=df2["Last"].fillna("Ahire")


# In[98]:


df2


# In[99]:


df2["Email"].mode()[0]


# In[100]:


df2["Email"]=df2["Email"].fillna("An@gmail.com")


# In[101]:


df2


# In[102]:


df2["age"].mode()[0]


# In[105]:


(df2['age']).dtype


# In[108]:


df2["age"]=pd.to_numeric(df2["age"],errors="coerce")
df2['age'].replace('NaN',0)


# In[109]:


df["age"].mean()


# In[112]:


df2["age"]=df2["age"].fillna(47.5)


# In[113]:


df2


# In[114]:


#to convert the data type of a column, we do:

#df["CN"]=df["CN"].astype("Float")
#df["CN"]=df["CN"].astype("int")


# In[136]:


df4=pd.read_csv('survey_results_public.csv')


# In[137]:


df4


# In[138]:


df4["MainBranch"].isnull().sum()


# In[139]:


df4["MainBranch"].mode()[0]


# In[140]:


df4["MainBranch"]=df4["MainBranch"].fillna('I am a developer by profession')


# In[141]:


df4["MainBranch"].isnull().sum()


# In[142]:


df4.isnull().sum()


# In[144]:


df4.info()


# In[145]:


df4['OpenSource'].mode()[0]


# In[146]:


df4['OpenSource']=df4['OpenSource'].fillna(df4['OpenSource'].mode()[0])


# In[147]:


df4['OpenSource'].isnull().sum()


# In[149]:


df4["YearsCode"].unique()


# In[150]:


df4["YearsCode"].replace('Less than 1 year',0,inplace=True)


# In[151]:


df4["YearsCode"].replace('More than 50 years',51,inplace=True)


# In[152]:


df4["YearsCode"].isnull().sum()


# In[153]:


df4["YearsCode"].mode()[0]


# In[154]:


df4["YearsCode"]=df4["YearsCode"].astype(float)


# In[156]:


df4["YearsCode"].dtype


# In[157]:


df4["YearsCode"].mean()


# In[158]:


df4["YearsCode"]=df4["YearsCode"].fillna(df4["YearsCode"].mean())


# In[159]:


df4["YearsCode"].isnull().sum()


# In[ ]:




