#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


ilkIndeksler = ["Simpson","Simpson","Simpson","South Park","South Park","South Park"]

icIndeksler = ["Homer","Bart","Marge","Cartman","Kenny","Kyle"]


# In[3]:


birlesmisIndeks = list(zip(ilkIndeksler,icIndeksler))


# In[4]:


birlesmisIndeks


# In[5]:


type(birlesmisIndeks)


# In[6]:


birlesmisIndeks = pd.MultiIndex.from_tuples(birlesmisIndeks)


# In[7]:


birlesmisIndeks


# In[8]:


type(birlesmisIndeks)


# In[9]:


benimCizgiFilmListem = [[40,"A"],[10,"B"],[30,"C"],[9,"D"],[9,"E"],[9,"F"]]


# In[10]:


cizgiFilmNumpyDizisi = np.array(benimCizgiFilmListem)


# In[11]:


cizgiFilmDataFrame = pd.DataFrame(cizgiFilmNumpyDizisi,index=birlesmisIndeks,columns=["Yas","Meslek"])


# In[12]:


cizgiFilmDataFrame


# In[13]:


cizgiFilmDataFrame.loc["Simpson"]


# In[14]:


cizgiFilmDataFrame.loc["South Park"]


# In[15]:


cizgiFilmDataFrame.loc["South Park"].loc["Kenny"]


# In[16]:


cizgiFilmDataFrame


# In[17]:


cizgiFilmDataFrame.index.names = ["CizgiFilm","İsim"]


# In[18]:


cizgiFilmDataFrame


# # Eksik Veriler

# In[19]:


sozlukVerisi = {"Istanbul" : [30,29,np.nan],"Ankara" : [20,np.nan,25],"Izmir" : [40,39,38]}


# In[20]:


havaDurumuDataFrame = pd.DataFrame(sozlukVerisi)


# In[21]:


havaDurumuDataFrame


# In[24]:


havaDurumuDataFrame.dropna()


# In[25]:


havaDurumuDataFrame.dropna(axis = 1)


# In[26]:


yeniVeri = {"Istanbul" : [30,29,np.nan],"Ankara" : [20,np.nan,25],"Izmir" : [40,39,38],"Kütahya":[18,np.nan,np.nan]}


# In[27]:


yeniDataFrame = pd.DataFrame(yeniVeri)


# In[28]:


yeniDataFrame


# In[29]:


yeniDataFrame.dropna(axis=1,thresh=2)


# In[30]:


yeniDataFrame


# In[31]:


yeniDataFrame.fillna(23)


# # Gruplandırmak

# In[32]:


maasSozlugu = {"Departman" : ["Yazılım","Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"], "Calisan Ismi" : ["Bülent","Koray","Aykut","Mehmet","Eren","Burçin"],"Maas":[100,150,200,300,400,500]}


# In[45]:


maasDataFrame = pd.DataFrame(maasSozlugu)


# In[46]:


maasDataFrame


# In[47]:


grupObjesi = maasDataFrame.groupby("Departman")


# In[48]:


grupObjesi


# In[49]:


grupObjesi.count()


# In[50]:


grupObjesi.mean()


# In[51]:


grupObjesi.min()


# In[52]:


grupObjesi.max()


# In[53]:


grupObjesi.describe()


# # CONCAT

# In[55]:


sozluk1 = {"Isim" : ["Ahmet","Mehmet","Zeynep","Atıl"], "Spor":["Koşu","Yüzme","Koşu","Basketbol"],"Kalori":[100,200,300,400]}


# In[56]:


dataFrame1 = pd.DataFrame(sozluk1,index  = [0,1,2,3])


# In[57]:


dataFrame1


# In[58]:


sozluk2 = {"Isim":["Osman","Levent","Atlas","Fatma"],"Spor":["Koşu","Yüzme","Koşu","Basketbol"],"Kalori":[200,100,50,300]}


# In[59]:


dataFrame2 = pd.DataFrame(sozluk2,index = [4,5,6,7])


# In[60]:


dataFrame2


# In[61]:


sozluk3 = {"Isim": ["Ayşe","Mahmut","Duygu","Nur"],"Spor" : ["Koşu","Yüzme","Badminton","Tenis"],"Kalori":[300,400,500,250]}


# In[62]:


dataFrame3 = pd.DataFrame(sozluk3,index=[8,9,10,11])


# In[63]:


dataFrame3


# In[64]:


pd.concat([dataFrame1,dataFrame2,dataFrame3],axis = 0)


# In[65]:


mergeSozluk1 = {"Isim" : ["Ahmet","Mehmet","Zeynep","Atıl"],"Spor":["Koşu","Yüzme","Koşu","Basketbol"]}


# In[66]:


mergeDataFrame1 = pd.DataFrame(mergeSozluk1)


# In[67]:


mergeDataFrame1


# In[68]:


mergeSozluk2 = {"Isim":["Ahmet","Mehmet","Zeynep","Atıl"],"Kalori":[100,200,150,250]}


# In[69]:


mergeDataFrame2 = pd.DataFrame(mergeSozluk2)


# In[70]:


mergeDataFrame2


# In[74]:


pd.merge(mergeDataFrame1,mergeDataFrame2,on="Isim")


# In[ ]:




