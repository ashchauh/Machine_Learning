
import numpy as np
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import sklearn



df1 = pd.read_csv(r'C:\Users\Ashish\Desktop\Test\Python_Codes\Datasets\BLI_23022018070840296.csv', thousands=',')


df2 = pd.read_csv(r'C:\Users\Ashish\Desktop\Test\Python_Codes\Datasets\weoreptc.aspx',thousands=',',delimiter='\t',encoding='latin1', na_values="n/a")

df2.head(5)
(df2.where(df2["Country"]=="Albania")).dropna()
(df2.where(df2["Country"]=="Albania")).dropna().set_index(["Units"]).rename(columns={"Scale": "Unit"} )
