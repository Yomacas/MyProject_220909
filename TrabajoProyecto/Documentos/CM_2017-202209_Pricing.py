#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib as plt
import numpy as np
import pandas as pd
import datetime as dt
import re


# In[2]:


Data_CM_2017= pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\DB_Costo_2017.csv', index_col = False, encoding='latin-1', sep = '|', low_memory = False)
Data_CM_2018= pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\DB_Costo_2018.csv', index_col = False, encoding='latin-1', sep = '|', low_memory = False)
Data_CM_2019= pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\DB_Costo_2019.csv', index_col = False, encoding='latin-1', sep = '|', low_memory = False)
Data_CM_2020_1= pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\DB_Costo_202001-202007.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Data_CM_2020_2= pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\DB_Costo_202008-202012.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Data_CM_2021_1= pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\DB_Costo_202101-202106.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Data_CM_2021_2= pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\DB_Costo_202107-202109.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Data_CM_2021_3= pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\DB_Costo_202110-202112.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Data_CM_2022_1= pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\DB_Costo_202201-202205.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Data_CM_2022_2= pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\DB_Costo_202206-202212.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)


# In[3]:


Data_CM_2017['MesRad']=Data_CM_2017['ï»¿MesRad']
Data_CM_2018['MesRad']=Data_CM_2018['ï»¿MesRad']
Data_CM_2019['MesRad']=Data_CM_2019['ï»¿MesRad']


# In[4]:


a1, a2, a3, a4, a5 = Data_CM_2017['numrad'].count(), Data_CM_2018['numrad'].count(), Data_CM_2019['numrad'].count(), Data_CM_2020_1['numrad'].count(), Data_CM_2020_2['numrad'].count()
a1, a2, a3, a4, a5


# In[5]:


a6, a7, a8, a9, a10 = Data_CM_2021_1['numrad'].count(), Data_CM_2021_2['numrad'].count(), Data_CM_2021_3['numrad'].count(), Data_CM_2022_1['numrad'].count(), Data_CM_2022_2['numrad'].count()
a6, a7, a8, a9, a10


# In[6]:


Data_CM_2022_2.dtypes


# In[7]:


CM_Total = pd.concat([Data_CM_2017, Data_CM_2018, Data_CM_2019, Data_CM_2020_1, Data_CM_2020_2, Data_CM_2021_1, Data_CM_2021_2, Data_CM_2021_3, Data_CM_2022_1,
                      Data_CM_2022_2], axis = 0, ignore_index = False, keys = None, sort = False, copy = True)


# In[8]:


CM_Total['numrad'].count()


# In[9]:


CM_Total


# In[10]:


df_DC = pd.DataFrame(CM_Total)


# In[11]:


del [[Data_CM_2017, Data_CM_2018, Data_CM_2019, Data_CM_2020_1, Data_CM_2020_2, Data_CM_2021_1, Data_CM_2021_2, Data_CM_2021_3, Data_CM_2022_1, Data_CM_2022_2, CM_Total]]


# In[12]:


df_DC.drop(['ï»¿MesRad', 'Usuario Nuevo', 'RED', 'Tipo Red'], axis=1, inplace=True)


# In[13]:


df_DC


# In[14]:


df_DC['MesRad'] = pd.to_datetime(df_DC['MesRad'], errors='coerce', format = ('%d/%m/%Y'))
df_DC['FechaPrestacion'] = pd.to_datetime(df_DC['FechaPrestacion'], errors='coerce', format = ('%d/%m/%Y'))


# In[15]:


df_DC['AnioMes_Acc'] = ((df_DC['FechaPrestacion'].dt.year * 100) + df_DC['FechaPrestacion'].dt.month).astype(float)
df_DC['AnioMes_Rad'] = ((df_DC['MesRad'].dt.year * 100) + df_DC['MesRad'].dt.month).astype(float)
df_DC['Anio_Acc'] = (df_DC['FechaPrestacion'].dt.year).astype(float)
df_DC['Anio_Rad'] = (df_DC['MesRad'].dt.year).astype(float)


# In[16]:


df_DC['VrFac'] = df_DC['VrFacturado']/1000000
df_DC['GlosaAce'] = df_DC['GlosaAceptada']/1000000
df_DC['GlosaApp'] = df_DC['GlosaAplicada']/1000000
df_DC['CM'] = df_DC['CostoMedico']/1000000
df_DC['Ded'] = df_DC['Bonos']/1000000
df_DC['CMwoDed'] = df_DC['CostomenosBonos']/1000000


# In[17]:


df_DC['CM'].sum()


# In[18]:


df_DC['PE'] = df_DC['IPS'].str.contains('CRI-|BLUECARE|CLINICA AZUL', na = False)
df_DC['BC'] = df_DC['IPS'].str.contains('CRI-|BLUECARE', na = False)


# In[19]:


df_DC['Anio_Acc'] = df_DC['Anio_Acc'].fillna(0)
df_DC['AnioMes_Acc'] = df_DC['AnioMes_Acc'].fillna(0)
df_DC['AnioMes_Rad'] = df_DC['AnioMes_Rad'].fillna(0)
df_DC['CarnetUsuario'] = df_DC['CarnetUsuario'].fillna(0)
df_DC['Sexo'] = df_DC['Sexo'].fillna(0)
df_DC['Edad'] = df_DC['Edad'].fillna(0)
df_DC['RangoEtareo'] = df_DC['RangoEtareo'].fillna(0)
df_DC['PlanCosto'] = df_DC['PlanCosto'].fillna(0)
df_DC['NombrePlancosto'] = df_DC['NombrePlancosto'].fillna(0)
df_DC['NAP'] = df_DC['NAP'].fillna(0)
df_DC['TipoServicioAgrupado'] = df_DC['TipoServicioAgrupado'].fillna(0)
df_DC['TipoServicio'] = df_DC['TipoServicio'].fillna(0)
df_DC['TipoContrato'] = df_DC['TipoContrato'].fillna(0)
df_DC['codmatriz'] = df_DC['codmatriz'].fillna(0)
df_DC['Codips'] = df_DC['Codips'].fillna(0)
df_DC['IPS'] = df_DC['IPS'].fillna(0)
df_DC['NAP'] = df_DC['NAP'].fillna(0)
df_DC['Area'] = df_DC['Area'].fillna(0)
df_DC['Ambito'] = df_DC['Ambito'].fillna(0)
df_DC['SucursalRad'] = df_DC['SucursalRad'].fillna(0)
df_DC['SucursalContrato'] = df_DC['SucursalContrato'].fillna(0)
df_DC['PE'] = df_DC['PE'].fillna(0)
df_DC['TipoCosto'] = df_DC['TipoCosto'].fillna(0)
df_DC['PatologiaAC'] = df_DC['PatologiaAC'].fillna(0)


# In[20]:


df_DC['CM'].sum()


# In[21]:


df_DC.loc[df_DC['Codips'] == 25173, 'Codips'] = 73004


# In[22]:


df_DC['IPS'] = df_DC['IPS'].str.strip()


# In[23]:


df_DC['IPS'] = df_DC['IPS'].fillna('0')


# In[24]:


#df_DC_IPS = pd.DataFrame(df_DC.groupby(['Codips', 'IPS', 'Anio_Rad']).agg({'CM':sum}).astype(float).reset_index())


# In[25]:


#df_DC_IPS = df_DC_IPS.reset_index()
#df_DC_IPS.to_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_202209\Results\IPS_Fully.txt', sep = ';', encoding = 'utf-8', index = False)


# In[26]:


#Level_IPS = pd.read_csv('D:\RODRIY21\A_DB\DB_CostoMedico\A_DB_CM_Test\IPS_Codes.csv',index_col = False, encoding='latin-1', sep = ';')


# In[27]:


#df_LevelIPS = pd.DataFrame(Level_IPS)


# In[28]:


#df_DC_1 = pd.merge(left = df_DC, right = df_LevelIPS, how = 'left', left_on = (['Codips', 'IPS']), right_on = (['Codips_Origen', 'IPS_Origen']))


# In[29]:


#df_DC_1['New_IPS'] = df_DC_1['New_IPS'].fillna(0)
#df_DC_1['Level_IPS'] = df_DC_1['Level_IPS'].fillna(0)


# In[30]:


#df_DC_1['CM'].sum()


# In[31]:


df_DC_TSA = pd.DataFrame(df_DC.groupby(['Ambito', 'TipoServicioAgrupado']).agg({'CM':sum}).astype(float).reset_index())
df_DC_TSA


# In[33]:


df_DC_TSA = df_DC_TSA.reset_index()
df_DC_TSA.to_csv('D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Results_202211\TSA_Amb_Fully.txt', sep = ';', encoding = 'utf-8', index = False)


# In[32]:


Tipo_Servicio = pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Work\TSA_Fully.csv',index_col = False, encoding='latin-1', sep = ';')
df_TServ_F = pd.DataFrame(Tipo_Servicio)


# In[33]:


df_DC_1 = pd.merge(left = df_DC, right = df_TServ_F, how = 'left', left_on = (['TipoServicioAgrupado']), right_on = (['TSA']))


# In[34]:


df_DC_1['TSA'] = df_DC_1['TSA'].fillna(0)
df_DC_1['T_ServFinal'] = df_DC_1['T_ServFinal'].fillna(0)


# In[35]:


df_DC_2 = pd.DataFrame(df_DC_1.groupby(['AnioMes_Acc', 'CarnetUsuario', 'Edad', 'Sexo', 'NAP', 'TSA', 'NombrePlancosto', 'SucursalContrato',
                                        'TipoContrato', ]).agg({'CM':sum, 'Ded':sum}).astype(float).reset_index())
df_DC_2


# In[36]:


df_DC_2['CM'].sum()


# In[37]:


df_DC_2.loc[df_DC_2['CM'] <= 0, 'Conteo'] = 0 
df_DC_2.loc[df_DC_2['CM'] > 0, 'Conteo'] = 1


# In[38]:


df_CM = pd.DataFrame(df_DC_2.loc[df_DC_2['AnioMes_Acc'] > 201612])
df_CM


# In[43]:


df_1 = pd.DataFrame(df_CM.loc[df_DC_2['Conteo'] == 0])
df_1


# In[44]:


df_1['Conteo'].sum()


# In[45]:


df_1 = df_1.reset_index()
df_1.to_csv('D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Results_202211\CM_Neg_202209.txt', sep = ';', encoding = 'utf-8', index = False)


# In[42]:


df_CM['Conteo'].sum()


# In[46]:


df_CM.drop(df_CM.loc[df_CM['Conteo'] == 0].index, inplace=True)
df_CM['Conteo'].count()


# In[48]:


df_CM = df_CM.reset_index()
df_CM.to_csv('D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Results_202211\CM_2017-202209.txt', sep = ';', encoding = 'utf-8', index = False)


# In[ ]:




