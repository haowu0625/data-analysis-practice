
# coding: utf-8

# In[1]:

import csv


# In[2]:

f=open('guns.csv','r')


# In[3]:

ss=csv.reader(f)


# In[4]:

data=list(ss)


# In[5]:

print(data[0:5])


# In[6]:

headers=data[0]


# In[7]:

datas=data[1:]


# In[8]:

print(headers)


# In[9]:

print(datas[0:5])


# In[10]:

years=[]
for year in datas:
    tt=year[1]
    years.append(tt)


# In[11]:

year_counts={}
for year in years:
    if year not in year_counts:
        year_counts[year]=0
    else:
        year_counts[year]+=1


# In[12]:

year_counts


# In[13]:

import datetime
datess=[]
for row in datas:
    year=int(row[1])
    month=int(row[2])
    date=datetime.datetime(year=year,month=month,day=1)
    datess.append(date)
    
    


# In[14]:

print(datess[0:4])


# In[15]:

date_counts={}
for date in dates:
    if date not in date_counts:
        date_counts[date]=0
    date_counts[date]+=1    
    


# In[16]:

sex=[]
for data in datas:
    sx=data[5]
    sex.append(sx)
    


# In[17]:

sex


# In[18]:

sex_counts={}
for sx in sex:
    if sx not in sex_counts:
        sex_counts[sx]=0
    sex_counts[sx]+=1    


# In[19]:

sex_counts


# In[20]:

race=[k[7] for k in datas]


# In[21]:

print(race)


# In[22]:

race_counts={}
for k in race:
    if k not in race_counts:
        race_counts[k]=0
    race_counts[k]+=1    


# In[23]:

race_counts


# In[24]:

d=open('census.csv','r')


# In[25]:

dddd=csv.reader(d)


# In[26]:

census=list(dddd)


# In[27]:

census


# In[28]:

mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}


# In[29]:

race_per_hundredk={}


# In[30]:

for t in race_counts:
    j=race_counts[t]/mapping[t]*100000
    race_per_hundredk[t]=j
    
    


# In[31]:

race_per_hundredk


# In[32]:

intents=[k[3] for k in datas]


# In[33]:

races=[k[7] for k in datas]


# In[ ]:




# In[36]:

homicide_race_counts={}
for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk
        
        


# In[ ]:



