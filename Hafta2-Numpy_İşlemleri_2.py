#!/usr/bin/env python
# coding: utf-8

# # Slicing (Dilimleme)

# In[1]:


# [başlama:bitiş]
# [başlama:bitiş:adımSayısı]
# [:bitiş:adımSayısı] 0. indeksten başlar
# [başlama::adımSayısı] son indekse kadar gider
# [::] 


# In[2]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7])


# In[3]:


arr


# In[29]:


arr2 = np.arange(1,15)


# In[30]:


arr2


# In[31]:


arr2[0]


# In[32]:


arr2[-1]


# In[33]:


arr2[len(arr2)-1]


# In[34]:


len(arr2)


# In[35]:


arr2[8]


# In[36]:


arr2


# In[38]:


arr2[1:5]


# In[39]:


arr2[1:5:1]


# In[40]:


arr2[3:13:3]


# In[41]:


arr2[3:12:3]


# In[42]:


arr2[3:12:2]


# In[43]:


arr2[:9:2]


# In[44]:


arr2[4::1]


# In[45]:


arr2[4:]


# In[46]:


arr2[4::]


# In[47]:


arr2[::]


# In[48]:


arr2[:5] = 20


# In[49]:


arr2


# In[50]:


arr = np.arange(1,15)


# In[51]:


arr


# In[52]:


arr2 = arr


# In[53]:


arr2


# In[54]:


arr2[:5] = 25


# In[55]:


arr2


# In[56]:


arr


# In[57]:


arr = np.arange(1,15)


# In[58]:


arr


# In[59]:


arrCopy = arr.copy() # Değerler kopyalanıyor


# In[60]:


arrCopy[0:5] = 20


# In[61]:


arrCopy


# In[62]:


arr


# In[63]:


yeniDizi = np.arange(1,21)


# In[64]:


yeniDizi


# In[65]:


yeniDizi = yeniDizi.reshape(4,5)


# In[66]:


yeniDizi[0,0]


# In[67]:


yeniDizi


# In[72]:


yeniDizi[:,:2]


# In[75]:


yeniDizi[:2,:2]


# In[76]:


yeniDizi[1:3,:]


# # Numpy Arraylerin Filtrelenmesi

# In[77]:


arr = np.arange(1,10)


# In[78]:


arr


# In[79]:


arr > 2


# In[81]:


durumDegerleriDizisi = arr > 4


# In[82]:


durumDegerleriDizisi


# In[83]:


arr[durumDegerleriDizisi]


# In[84]:


arr[arr>4]


# In[85]:


#zeros


# In[86]:


np.zeros(5)


# In[87]:


np.zeros((9,9))


# In[88]:


#ones
np.ones(5)


# In[89]:


np.ones((9,9))


# In[3]:


#linspace
np.round(np.linspace(0,10,100),2)


# In[93]:


np.linspace(0,100,5)


# In[94]:


np.linspace(0,1,6)


# In[91]:


#eye


# In[92]:


np.eye(10)


# In[95]:


#random


# In[96]:


np.random.randn(4)


# In[4]:


dizi = np.random.randn(4,4)


# In[5]:


dizi


# In[6]:


np.round(dizi,2)


# In[112]:


np.random.randint(1,10)


# In[119]:


rastgeleDizim=np.random.randint(1,200,20)


# In[120]:


rastgeleDizim


# In[113]:


yeniDizi


# In[114]:


dizi


# In[115]:


#dizi metotları


# In[118]:


dizi.max()


# In[122]:


rastgeleDizim


# In[121]:


rastgeleDizim.max()


# In[123]:


dizi.min()


# In[124]:


rastgeleDizim.min()


# In[7]:


rastgeleDizim.argmax()


# In[ ]:




