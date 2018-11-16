#!/usr/bin/env python
# coding: utf-8

# # W207 Final Project
# ### [Airbnb New User Bookings](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/data)
# ### Initial Exploratory Analysis

# Import Libraries

# In[4]:


import numpy as np
import pandas as pd
import os

# Files:

# In[3]:
DATA_PATH = './data/extracted'
for root, dirs, files in os.walk(DATA_PATH):
    for file in files:
        print(file)

# ### Exploratory - age_gender_bkts

# In[6]:


age_gender_bkts = pd.read_csv(f'{DATA_PATH}/age_gender_bkts.csv')


# In[10]:


age_gender_bkts.head()


# Appears the file contains the amount of users, split out by a few demographic characteristics, by country of destination.

# ### Exploratory - countries

# In[11]:


countries = pd.read_csv(f'{DATA_PATH}/countries.csv')


# In[13]:


countries


# Appears to contain summary stats for each destination country, as well as average distances.

# ### Exploratory - sample_submission_NDF

# In[14]:


sample_submission_NDF = pd.read_csv(f'{DATA_PATH}/sample_submission_NDF.csv')


# In[16]:


sample_submission_NDF.head()


# Format for submitting data, not super useful for us.

# ### Exploratory - sessions

# In[17]:


sessions = pd.read_csv(f'{DATA_PATH}/sessions.csv')


# In[20]:


sessions.head(20)


# Click stream data - can't really tell the specifics here

# In[19]:


sessions['action'].unique()


# There are a ton of actions, not sure if we can actually see search results.

# In[21]:


sessions['action_detail'].unique()


# Exploratory - train_users_2

# In[22]:


train_users_2 = pd.read_csv(f'{DATA_PATH}/train_users_2.csv')


# In[23]:


train_users_2.head()


# In[ ]:




