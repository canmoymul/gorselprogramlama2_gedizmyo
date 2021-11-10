#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



x = np.arange(1,6)

y = np.arange(2,11,2)

fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.3,0.6,0.1,0.2])

axes1.plot(y,x)

axes1.set_xlabel("Dış Grafik X")
axes1.set_ylabel("Dış Grafik Y")
axes1.set_title("Dış Grafik")


axes2.plot(x,y)

axes2.set_xlabel("İç Grafik x")
axes2.set_ylabel("İç Grafik y")
axes2.set_title("İç Grafik")

plt.show()


# In[6]:


plt.subplot(2,2,1)
plt.plot(x,y,"blue")
plt.subplot(2,2,2)
plt.plot(y,x,"yellow")
plt.subplot(2,2,3)
plt.plot(y,y**2,"red")
plt.subplot(2,2,4)
plt.plot(x,x**2,"black")
plt.show()


# In[20]:


fig,axes = plt.subplots(nrows = 2,ncols = 1)

#for ax in axes:
    #ax.plot(x,y)
    
axes[0].plot(x,y)
axes[0].set_title("Birinci Grafik")
axes[1].plot(x,x**3)
axes[1].set_title("İkinci Grafik")
plt.tight_layout()


# In[23]:


fig,axes = plt.subplots(nrows = 2,ncols = 1,figsize=(8,6))

axes[0].plot(x,y,color = "red")
axes[0].set_title("İlk Grafik")
axes[1].plot(x,x**0.5,color="purple")
axes[1].set_title("İkinci Grafik")
plt.tight_layout()
plt.show()


# In[24]:


fig.savefig("Figure1.png")


# In[25]:


fig.savefig("Figure.pdf")


# In[39]:


fig = plt.figure(figsize =(6,4))
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x**0.5,color = "red",label = "X Karekök")
axes.plot(x,x**2,color = "blue", label = "X Kare")
axes.plot(x,x**3,color = "black", label = "X Küp")

axes.legend()

plt.show()


# In[54]:


fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x**2,color = "red",linestyle = ":",marker = "o",markersize=20,markerfacecolor = "black",markeredgecolor="yellow",markeredgewidth=3)


# In[55]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
x = np.arange(51)
y = np.arange(0,101,2)
z = x ** 3


# In[57]:


fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,y,color="red")

axes.set_xlabel("X Değerleri")
axes.set_ylabel("Y Değerleri")
axes.set_title("X ve Y Grafiği")

plt.show()


#  1. Figure Size'ı (8,6) olan bir figure Oluşturun
#  2. axes1 ve axes2 adında 2 adet axes oluşturun.(axes1 pozisyonu = [0,0.1,0.8,0.8], axes2          pozisyonu = [0.1,0.5,0.4,0.3])
#   3. axes1 üzerinde x vs z grafiğini, axes2 üzerinde x vs y grafiğini çizin ve aşağıdaki 
#     grafiğe benzer bir grafik oluşturun. 

# In[58]:


fig = plt.figure(figsize=(8,6))
axes1 = fig.add_axes([0,0.1,0.8,0.8])
axes2 = fig.add_axes([0.1,0.5,0.4,0.3])

axes1.plot(x,z,color="purple")
axes1.set_title("Dış Grafik - X ve Z Grafiği")
axes2.plot(x,y,color="red")
axes2.set_title("İç Grafik - X ve Y Grafiği")

plt.show()


# 1. 2 adet yanyana subplot oluşturun. (figsize=(10,6))
# 2. Birinci grafiğe (x,y) grafiğini , ikinci grafiğe (x,z) grafiğini çizin.
# 3. plot() fonksiyonunun parametrelerini vererek, grafiği aşağıdaki grafiğe benzer özelleştirin.

# In[60]:


fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(10,6))

axes[0].plot(x,y,color="red",lw=3,ls="--",marker ="o",markerfacecolor="black")
axes[0].set_xlabel("X Değerleri")
axes[0].set_ylabel("Y Değerleri")
axes[0].set_title("X ve Y Grafiği")


axes[1].plot(x,z,color="purple",lw=3,ls="-.")
axes[1].set_xlabel("X Değerleri")
axes[1].set_title("X ve Z Grafiği")


# In[61]:


x = np.random.randint(0,100,50)


# In[62]:


x


# In[63]:


plt.hist(x)


# In[64]:


plt.boxplot(x*2)


# In[67]:


plt.scatter(y,z)


# In[ ]:




