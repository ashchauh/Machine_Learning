
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
import pandas as pd


# In[12]:


df1 = pd.read_csv(r'C:\Users\Ashish\Desktop\Test\Python_Codes\Datasets\BLI_23022018070840296.csv', thousands=',')


# In[13]:


df2 = pd.read_csv(r'C:\Users\Ashish\Desktop\Test\Python_Codes\Datasets\weoreptc.aspx',thousands=',',delimiter='\t',encoding='latin1', na_values="n/a")


# In[14]:


df2.head(5)


# In[21]:


(df2.where(df2["Country"]=="Albania")).dropna()


# In[26]:


(df2.where(df2["Country"]=="Albania")).dropna().set_index(["Units"]).rename(columns={"Scale": "Unit"} )

