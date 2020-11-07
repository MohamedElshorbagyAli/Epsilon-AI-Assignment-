#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
sns.set(rc={'figure.figsize':[8,8]},font_scale=1.2) 


# In[2]:


df = pd.read_csv('./50ulke.csv',sep=",")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df['National Income'].hist(color='g')


# In[7]:


sns.kdeplot(df['National Income'], color='g')


# In[8]:


df['Growth'].hist(color='g')


# In[9]:


sns.kdeplot(df['Growth'], color='g')


# In[10]:


df['Per person'].hist(color='g')


# In[11]:


sns.kdeplot(df['Per person'],color='g')


# In[12]:


sns.regplot(x=df['Growth'],y=df['National Income'],color='g')


# In[13]:


sns.regplot(x=df['Per person'],y=df['National Income'],color='g')


# In[14]:


sns.regplot(x=df['Growth'],y=df['Per person'],color='g')


# In[15]:


sns.jointplot(x='Growth', y='National Income', data=df, kind='scatter',height=8,color='g')


# In[16]:


sns.jointplot(x='Per person', y='National Income', data=df, kind='scatter',height=8,color='g')


# In[17]:


sns.jointplot(x='Growth', y='Per person', data=df, kind='scatter',height=8,color='g')


# In[18]:


sns.pairplot(df, vars=['National Income', 'Growth','Per person'],height=3, aspect=1.3)


# In[19]:


sns.pairplot(df, vars=['National Income', 'Growth','Per person'],hue='Continent',height=3, aspect=1.3)


# In[20]:


sns.boxplot(df['National Income'],color='g')


# In[21]:


sns.boxplot(df['Growth'],color='g')


# In[22]:


sns.boxplot(df['Per person'],color='g')


# In[23]:


sns.boxplot(x='Continent',y='National Income',data=df)


# In[24]:


sns.boxplot(x='Continent',y='Growth',data=df)


# In[25]:


sns.boxplot(x='Continent',y='Per person',data=df)


# In[26]:


sns.violinplot(x='Continent',y='National Income',data=df)


# In[27]:


sns.violinplot(x='Continent',y='Growth',data=df)


# In[28]:


sns.violinplot(x='Continent',y='Per person',data=df)


# In[29]:


sns.stripplot(x='Continent',y='National Income',data=df)


# In[30]:


sns.stripplot(x='Continent',y='Growth',data=df)


# In[31]:


sns.stripplot(x='Continent',y='Per person',data=df)


# In[32]:


sns.swarmplot(x='Continent',y='National Income',data=df)


# In[33]:


sns.swarmplot(x='Continent',y='Growth',data=df)


# In[34]:


sns.swarmplot(x='Continent',y='Per person',data=df)


# In[35]:


sns.barplot(x='Continent',y='National Income',data=df)


# In[36]:


sns.barplot(x='Continent',y='Growth',data=df)


# In[37]:


sns.barplot(x='Continent',y='Per person',data=df)


# In[38]:


df.corr()


# In[39]:


sns.heatmap(df.corr(),annot=True)

