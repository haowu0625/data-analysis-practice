
# coding: utf-8

# In[2]:

import pandas as pd

data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")
data.head()


# In[3]:

data.columns


# In[4]:

data["Do you celebrate Thanksgiving?"].value_counts()


# In[5]:

data = data[data["Do you celebrate Thanksgiving?"] == "Yes"]


# In[6]:

data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[7]:

data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]["Do you typically have gravy?"]


# In[8]:


data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].value_counts()


# In[9]:


ate_pies = (pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
&
pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])
 &
 pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
)

ate_pies.value_counts()


# In[10]:

def intstring(t):
    if pd.isnull(t):
        return None
    else:
        j=t.split(' ')
        p=j[0]
        p=p.replace('+','')
        p=int(p)
    return p    


# In[11]:

data["int_age"] = data["Age"].apply(intstring)
data["int_age"].describe()


# In[12]:

def strincome(t):
    if pd.isnull(t):
        return None
    else:
        j=t.split(' ')[0]
        if j=='Prefer':
            return None
        j=j.replace(',','')
        j=j.replace('$','')
        j=int(j)
    return j


# In[13]:

data['int_income']=data['How much total combined money did all members of your HOUSEHOLD earn last year?'].apply(strincome)


# In[14]:

data['int_income'].describe()


# In[15]:

newdatas=data[data['int_income']<150000]


# In[16]:

newdatas['How far will you travel for Thanksgiving?'].value_counts()


# In[18]:

new_data=data[data['int_income']>150000]


# In[19]:

new_data['How far will you travel for Thanksgiving?'].value_counts()


# In[22]:

data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_age"
)


# In[23]:


data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_income"
)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



