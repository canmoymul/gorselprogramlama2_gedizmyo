#!/usr/bin/env python
# coding: utf-8

# # Seriler (Series)

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


benimSözlüğüm = {"Ali" : 40 , "Hülya" : 30 , "Yekta" : 50}


# In[3]:


pd.Series(benimSözlüğüm)


# In[4]:


type(pd.Series(benimSözlüğüm))


# In[5]:


benimYaşlarım = [40,30,50]
benimİsimlerim = ["Ali","Hülya","Yekta"]


# In[6]:


pd.Series(benimYaşlarım)


# In[7]:


pd.Series(benimYaşlarım,benimİsimlerim)


# In[8]:


pd.Series(data=benimYaşlarım, index=benimİsimlerim)


# In[9]:


numpyDizisi = np.array([40,30,50])


# In[10]:


numpyDizisi


# In[11]:


pd.Series(numpyDizisi)


# In[12]:


pd.Series(numpyDizisi,benimİsimlerim)


# # Seri Özellikleri

# In[13]:


pd.Series(["Mevlüt","Yağız","Ayşe"],[1,2,3])


# In[14]:


yarışmaSonucu1 = pd.Series([10,5,1],["Yekta","Hülya","Yağız"])


# In[15]:


yarışmaSonucu1


# In[16]:


yarışmaSonucu2 = pd.Series([20,10,8],["Yekta","Hülya","Yağız"])


# In[17]:


yarışmaSonucu2


# In[18]:


yarışmaSonucu2["Yekta"]


# In[19]:


toplamPuan = yarışmaSonucu1 + yarışmaSonucu2


# In[20]:


toplamPuan


# In[21]:


farklıSeries1 = pd.Series([20,30,40,50],["a","b","c","d"])


# In[22]:


farklıSeries2 = pd.Series([10,5,3,1],["a","c","f","g"])


# In[ ]:




