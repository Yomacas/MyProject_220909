#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib as plt
import numpy as np
import pandas as pd
import datetime as dt
import re


# In[ ]:





# # Archivo central para estimación de freq, Actuaría

# In[ ]:





# In[2]:


ExpAct_17_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2017_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
ExpAct_17_2= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2017_2.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
ExpAct_18_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2018_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
ExpAct_18_2= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2018_2.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
ExpAct_19_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2019_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
ExpAct_19_2= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2019_2.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
ExpAct_20_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2020_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
ExpAct_20_2= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2020_2.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
ExpAct_21_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2021_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
ExpAct_21_2= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2021_2.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
ExpAct_22_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Act_DB\IngUsuExp_2022_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)


# In[3]:


a1, a2, a3, a4, a5, a6 = ExpAct_17_1['Mes'].count(), ExpAct_17_2['Mes'].count(), ExpAct_18_1['Mes'].count(), ExpAct_18_2['Mes'].count(), ExpAct_19_1['Mes'].count(), ExpAct_19_2['Mes'].count(),
a1, a2, a3, a4, a5, a6


# In[4]:


a7, a8, a9, a10, a11 = ExpAct_20_1['Mes'].count(), ExpAct_20_2['Mes'].count(), ExpAct_21_1['Mes'].count(), ExpAct_21_2['Mes'].count(), ExpAct_22_1['Mes'].count()
a7, a8, a9, a10, a11


# In[5]:


ExpAct_22_1.dtypes


# In[6]:


ExpAct_Total = pd.concat([ExpAct_17_1, ExpAct_17_2, ExpAct_18_1, ExpAct_18_2, ExpAct_19_1, ExpAct_19_2, ExpAct_20_1, ExpAct_20_2, ExpAct_21_1, ExpAct_21_2, ExpAct_22_1],
                         axis = 0, ignore_index = False, keys = None, sort = False, copy = True)
ExpAct_Total['MesIng'].count()


# In[7]:


ExpAct_Total


# In[8]:


df_ExpAct = pd.DataFrame(ExpAct_Total)


# In[9]:


del [[ExpAct_17_1, ExpAct_17_2, ExpAct_18_1, ExpAct_18_2, ExpAct_19_1, ExpAct_19_2, ExpAct_20_1, ExpAct_20_2, ExpAct_21_1, ExpAct_21_2, ExpAct_22_1, ExpAct_Total]]


# In[10]:


df_ExpAct.describe()


# In[11]:


df_ExpAct['Periodo'] = (df_ExpAct['AnioIng'] * 100 + df_ExpAct['MesIng']).astype(float)


# In[12]:


df_ExpAct['Premium'] = (df_ExpAct['ValorPrima']/1000000).astype(float)
df_ExpAct['VrPOS'] = (df_ExpAct['ValorPos']/1000000).astype(float)
df_ExpAct['VrNC'] = (df_ExpAct['ValorNotas']/1000000).astype(float)
df_ExpAct['VrAdd'] = (df_ExpAct['ValorAdicional']/1000000).astype(float)
df_ExpAct['DtoPtoPag'] = (df_ExpAct['ValorDtoPtoPago']/1000000).astype(float)
df_ExpAct['P_NetPtoPag'] = (df_ExpAct['VrIngConDtoPtoPago']/1000000).astype(float)
df_ExpAct['P_GrossPtoPag'] = (df_ExpAct['VrIngSinDtoPtoPago']/1000000).astype(float)


# In[13]:


df_ExpAct['Parentesco'] = df_ExpAct['Parentesco'].str.strip()
df_ExpAct['Sexo'] = df_ExpAct['Sexo'].str.strip()
df_ExpAct['TipoContrato'] = df_ExpAct['TipoContrato'].str.strip()
df_ExpAct['nombreplan'] = df_ExpAct['nombreplan'].str.strip()
df_ExpAct['Tipo'] = df_ExpAct['Tipo'].str.strip()
df_ExpAct['ciudad'] = df_ExpAct['ciudad'].str.strip()


# In[14]:


df_ExpAct['Parentesco'] = df_ExpAct['Parentesco'].fillna('0')
df_ExpAct['Edad'] = df_ExpAct['Edad'].fillna(9999)
df_ExpAct['Sexo'] = df_ExpAct['Sexo'].fillna('0')
df_ExpAct['TipoContrato'] = df_ExpAct['TipoContrato'].fillna('0')
df_ExpAct['nombreplan'] = df_ExpAct['nombreplan'].fillna('0')
df_ExpAct['CodMatriz'] = df_ExpAct['CodMatriz'].fillna(9999)
df_ExpAct['Tipo'] = df_ExpAct['Tipo'].fillna('0')
df_ExpAct['ciudad'] = df_ExpAct['ciudad'].fillna('0')


# In[15]:


df_ExpAct['P_NetPtoPag'].sum()


# In[16]:


FecAnalysis = pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Work\FecPerAnalysis.csv', index_col = False, encoding='latin-1', sep = ';')


# In[17]:


df_FecAnalysis = pd.DataFrame(FecAnalysis)


# In[18]:


df_ExpAct = pd.merge(left = df_ExpAct, right = df_FecAnalysis, how = 'left', left_on = (['Periodo']), right_on = (['AñoMes_V']))


# In[19]:


df_ExpAct['FecIni_Per'] = pd.to_datetime(df_ExpAct['FecIni_Per'], errors='coerce', format = ('%d/%m/%Y'))
df_ExpAct['FecFin_Per'] = pd.to_datetime(df_ExpAct['FecFin_Per'], errors='coerce', format = ('%d/%m/%Y'))


# In[20]:


df_ExpAct_Agg = pd.DataFrame(df_ExpAct.groupby(['Periodo', 'FecIni_Per', 'FecFin_Per', 'numerocontrato', 'CarnetUsuario', 'Parentesco',
                                                'Edad', 'Sexo', 'TipoContrato', 'nombreplan', 'CodMatriz',
                                                'ciudad']).agg({'Premium':sum, 'P_NetPtoPag':sum, 'P_GrossPtoPag': sum}).astype(float).reset_index())
df_ExpAct_Agg


# In[21]:


df_ExpAct_Agg.dtypes


# In[22]:


del [[df_ExpAct]]


# In[24]:


df_ExpAct_Agg.loc[df_ExpAct_Agg['Premium'] <= 0, 'Conteo'] = 0
df_ExpAct_Agg.loc[df_ExpAct_Agg['Premium'] > 0, 'Conteo'] = 1


# In[25]:


# Estados apriori 
conditions = [
    (df_ExpAct_Agg['Premium'] < 0),
    (df_ExpAct_Agg['Premium'] == 0),
    (df_ExpAct_Agg['Premium'] > 0)
]
values = ['Cancel', 'Move_w/oP', 'Inforce']
df_ExpAct_Agg['TypePaid'] = np.select(conditions, values)
df_ExpAct_Agg.head()


# In[26]:


df_ExpAct_Agg['Periodo_1'] = df_ExpAct_Agg['Periodo'].apply(lambda x: (x - 89) if (x % 100) == 1 else (x - 1))
df_ExpAct_Agg.head()


# In[ ]:





# # Archivo que contiene las fechas de vigencia, área Técnica

# In[ ]:





# In[27]:


Exp_17_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2017_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Exp_17_2= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2017_2.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Exp_18_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2018_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Exp_18_2= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2018_2.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Exp_19_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2019_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Exp_19_2= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2019_2.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Exp_20_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2020_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Exp_20_2= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2020_2.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Exp_21_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2021_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Exp_21_2= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2021_2.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)
Exp_22_1= pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\ATec_DB\Usuarios_2022_1.csv', index_col = False, encoding='latin-1', sep = ';', low_memory = False)


# In[28]:


a12, a13, a14, a15, a16, a17 = Exp_17_1['MES'].count(), Exp_17_2['MES'].count(), Exp_18_1['MES'].count(), Exp_18_2['MES'].count(), Exp_19_1['MES'].count(), Exp_19_2['MES'].count()
a12, a13, a14, a15, a16, a17


# In[29]:


a18, a19, a20, a21, a22 = Exp_20_1['MES'].count(), Exp_20_2['MES'].count(), Exp_21_1['MES'].count(), Exp_21_2['MES'].count(), Exp_22_1['MES'].count()
a18, a19, a20, a21, a22


# In[30]:


Exp_22_1.dtypes


# In[31]:


Exp_Total = pd.concat([Exp_17_1, Exp_17_2, Exp_18_1, Exp_18_2, Exp_19_1, Exp_19_2, Exp_20_1, Exp_20_2, Exp_21_1, Exp_21_2, Exp_22_1], axis = 0, ignore_index = False,
                      keys = None, sort = False, copy = True)
Exp_Total['Carnet'].count()


# In[32]:


Exp_Total


# In[33]:


df_Exp = pd.DataFrame(Exp_Total)


# In[34]:


del [[Exp_17_1, Exp_17_2, Exp_18_1, Exp_18_2, Exp_19_1, Exp_19_2, Exp_20_1, Exp_20_2, Exp_21_1, Exp_21_2, Exp_22_1, Exp_Total]]


# In[35]:


df_Exp['FECHA INI VIGENCIA'] = pd.to_datetime(df_Exp['FECHA INI VIGENCIA'], errors='coerce', format = ('%d/%m/%Y'))
df_Exp['FECHA FIN VIGENCIA'] = pd.to_datetime(df_Exp['FECHA FIN VIGENCIA'], errors='coerce', format = ('%d/%m/%Y'))
df_Exp['FECHA NACIMIENTO'] = pd.to_datetime(df_Exp['FECHA NACIMIENTO'], errors='coerce', format = ('%d/%m/%Y'))


# In[36]:


df_Exp['COD PARENT'] = df_Exp['COD PARENT'].str.strip()
df_Exp['SEXO'] = df_Exp['SEXO'].str.strip()
df_Exp['Nombre Plan'] = df_Exp['Nombre Plan'].str.strip()
df_Exp['TIPO CONTRATO'] = df_Exp['TIPO CONTRATO'].str.strip()
df_Exp['Ciudad'] = df_Exp['Ciudad'].str.strip()


# In[37]:


df_Exp['NUMERO CONTRATO'] = df_Exp['NUMERO CONTRATO'].fillna(98989898)
df_Exp['Carnet'] = df_Exp['Carnet'].fillna(98989898)
df_Exp['COD PARENT'] = df_Exp['COD PARENT'].fillna('0')
df_Exp['EDAD'] = df_Exp['EDAD'].fillna(9999)
df_Exp['SEXO'] = df_Exp['SEXO'].fillna('0')
df_Exp['TIPO CONTRATO'] = df_Exp['TIPO CONTRATO'].fillna('0')
df_Exp['Nombre Plan'] = df_Exp['Nombre Plan'].fillna('0')
df_Exp['CODMATRIZ'] = df_Exp['CODMATRIZ'].fillna(9999)
df_Exp['Ciudad'] = df_Exp['Ciudad'].fillna('0')
df_Exp['FECHA INI VIGENCIA'].fillna(value=pd.to_datetime('1/1/1900'), inplace=True)
df_Exp['FECHA FIN VIGENCIA'].fillna(value=pd.to_datetime('1/1/1900'), inplace=True)
df_Exp['FECHA NACIMIENTO'].fillna(value=pd.to_datetime('1/1/1900'), inplace=True)


# In[38]:


Meses = pd.read_csv(r'D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Work\Meses.csv', index_col = False, encoding='latin-1', sep = ';')


# In[39]:


df_Meses = pd.DataFrame(Meses)


# In[40]:


df_Exp = pd.merge(left = df_Exp, right = df_Meses, how = 'left', left_on = (['MES']), right_on = (['Mes_L']))


# In[41]:


df_Exp['AñoMes_Per'] = df_Exp['AÑO'] * 100 + df_Exp['Mes_N']


# In[42]:


df_Exp['Conteo1'] = 1
df_Exp['Conteo1'].sum()


# In[43]:


df_Exp_Agg = pd.DataFrame(df_Exp.groupby(['AñoMes_Per', 'NUMERO CONTRATO', 'Carnet', 'FECHA INI VIGENCIA',
                                          'FECHA FIN VIGENCIA']).agg({'Conteo1':sum}).astype(float).reset_index())
#'FecIni_Per', 'FecFin_Per', 
df_Exp_Agg.head()


# In[44]:


df_Exp_Agg['Conteo1'].sum()


# In[ ]:





# # Obtener el máximo de AñoMes_Per y fechas de vigencia de los que no cruzan

# In[ ]:





# In[ ]:


#df_Exp['Key_1'] = df_Exp['NUMERO CONTRATO'].astype(str) + "_" + df_Exp['Carnet'].astype(str)


# In[ ]:


#df_Exp1 = pd.DataFrame(df_Exp.groupby(['Key_1', 'AñoMes_Per', 'FECHA INI VIGENCIA', 'FECHA FIN VIGENCIA']).agg({'Conteo':sum}).astype(float).reset_index())
#df_Exp1.head()


# In[ ]:


#cols = ['AñoMes_Per', 'FECHA INI VIGENCIA', 'FECHA FIN VIGENCIA']
#df_Exp1[cols] = df_Exp1[cols].fillna(np.inf)  # replace NaN with largest value
#df_Exp1 = df_Exp1.groupby('Key_1', as_index=False)[cols].max()  # Get Max Per Group
#df_Exp1[cols] = df_Exp1[cols].replace(np.inf, np.nan)  # Return to NaN
#df_Exp1


# In[ ]:


#df_Exp1 = df_Exp1.reset_index()
#df_Exp1.to_csv('D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Results_202211\Exp_NAN_202209_NoCruxMax.txt', sep = ';', encoding = 'utf-8', index = False)


# In[ ]:


#del [[df_Exp]]


# In[ ]:





# # Cruce para obtener las fechas de vigencia en el archivo central

# In[ ]:





# In[45]:


df_ExpPreliminary = pd.merge(left = df_ExpAct_Agg, right = df_Exp_Agg, how = 'left', left_on = (['Periodo', 'numerocontrato', 'CarnetUsuario']),
                             right_on = (['AñoMes_Per', 'NUMERO CONTRATO', 'Carnet']))


# In[46]:


df_ExpPreliminary


# In[47]:


df_ExpPreliminary['Periodo'].count()


# In[48]:


df_ExpPreliminary['FECHA INI VIGENCIA'].isna().sum()


# In[49]:


df_1 = pd.DataFrame(df_ExpPreliminary[df_ExpPreliminary['FECHA INI VIGENCIA'].isna()])
df_1


# In[50]:


df_1.drop(['AñoMes_Per', 'NUMERO CONTRATO', 'Carnet', 'FECHA INI VIGENCIA', 'FECHA FIN VIGENCIA', 'Conteo1'], axis=1, inplace=True)
df_1.head()


# In[51]:


df_ExpFinal = pd.merge(left = df_1, right = df_Exp_Agg, how = 'left',
                       left_on = (['Periodo_1', 'numerocontrato', 'CarnetUsuario']),
                       right_on = (['AñoMes_Per', 'NUMERO CONTRATO', 'Carnet']))


# In[52]:


df_ExpFinal


# In[53]:


df_ExpFinal['FECHA INI VIGENCIA'].isna().sum()


# In[ ]:





# # Se eliminan los registros sin coherencia en la identificación del carnet y de las fechas de inicio y fin de vigencia

# In[ ]:





# In[54]:


df_ExpFinal = df_ExpFinal.dropna(subset=['FECHA INI VIGENCIA', 'FECHA FIN VIGENCIA'])
df_ExpFinal['Periodo'].count()


# In[55]:


df_ExpPreliminary = df_ExpPreliminary.dropna(subset=['FECHA INI VIGENCIA', 'FECHA FIN VIGENCIA'])
df_ExpPreliminary['Periodo'].count()


# In[56]:


df_ExpT = pd.concat([df_ExpPreliminary, df_ExpFinal], axis = 0, ignore_index = False, keys = None, sort = False, copy = True)
df_ExpT['Periodo'].count()


# In[57]:


df_Valid = df_ExpT.loc[((df_ExpT['TypePaid'] == 'Cancel') | (df_ExpT['TypePaid'] == 'Move_w/oP'))]
df_Valid


# In[58]:


df_Valid = df_Valid.reset_index()
df_Valid.to_csv('D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Results_202211\Exp_PremNeg_202209_Valid.txt', sep = ';', encoding = 'utf-8', index = False)


# In[ ]:


# Se valida


# In[71]:


conditions = [
    (df_ExpT['FECHA INI VIGENCIA'] <= df_ExpT['FecIni_Per']) & (df_ExpT['FECHA FIN VIGENCIA'] >= df_ExpT['FecFin_Per']),
    (df_ExpT['FECHA INI VIGENCIA'] <= df_ExpT['FecIni_Per']) & (df_ExpT['FECHA FIN VIGENCIA'] >= df_ExpT['FecIni_Per']) & (df_ExpT['FECHA FIN VIGENCIA'] <= df_ExpT['FecFin_Per']),
    (df_ExpT['FECHA INI VIGENCIA'] >= df_ExpT['FecIni_Per']) & (df_ExpT['FECHA INI VIGENCIA'] <= df_ExpT['FecFin_Per']) & (df_ExpT['FECHA FIN VIGENCIA'] >= df_ExpT['FecFin_Per']),
    (df_ExpT['FECHA INI VIGENCIA'] >= df_ExpT['FecIni_Per']) & (df_ExpT['FECHA FIN VIGENCIA'] <= df_ExpT['FecFin_Per']),
    (df_ExpT['FECHA FIN VIGENCIA'] < df_ExpT['FecIni_Per']),
    (df_ExpT['FECHA INI VIGENCIA'] > df_ExpT['FecFin_Per'])
]
values = ['1', '2', '3', '4', '5', '6']
df_ExpT['Range_0'] = np.select(conditions, values)
df_ExpT.head()


# In[73]:


def Exposure(df_ExpT):
    if (df_ExpT['Range_0'] == '1'):
        return abs((df_ExpT['FecFin_Per'] - df_ExpT['FecIni_Per']).days + 1) / 30.4375
    elif (df_ExpT['Range_0'] == '2'):
        return abs((df_ExpT['FECHA FIN VIGENCIA'] - df_ExpT['FecIni_Per']).days + 1) / 30.4375 
    elif (df_ExpT['Range_0'] == '3'):
        return abs((df_ExpT['FecFin_Per'] - df_ExpT['FECHA INI VIGENCIA']).days + 1) / 30.4375
    elif (df_ExpT['Range_0'] == '4'):
        return abs((df_ExpT['FECHA FIN VIGENCIA'] - df_ExpT['FECHA INI VIGENCIA']).days + 1) / 30.4375
    elif (df_ExpT['Range_0'] == '5'):
        return (0)
    elif (df_ExpT['Range_0'] == '6'):
        return (0)
df_ExpT['Exposure'] = df_ExpT.apply(Exposure, axis = 1)


# In[86]:


df_ExpT


# In[75]:


a, b, c, d = df_ExpT['Exposure'].sum(), df_ExpT['Exposure'].mean(), df_ExpT['Exposure'].min(), df_ExpT['Exposure'].max()
a, b, c, d


# In[81]:


df_ExpT.loc[df_ExpT['TypePaid'] == 'Inforce', 'Mult'] = 1
df_ExpT.loc[df_ExpT['TypePaid'] != 'Inforce', 'Mult'] = 0


# In[85]:


df_ExpT['Exp_F'] = df_ExpT['Mult'] * df_ExpT['Exposure']


# In[87]:


a, b, c, d = df_ExpT['Exp_F'].sum(), df_ExpT['Exp_F'].mean(), df_ExpT['Exp_F'].min(), df_ExpT['Exp_F'].max()
a, b, c, d


# In[88]:


df_ExpT = df_ExpT.reset_index()
df_ExpT.to_csv('D:\RODRIY21\A_DB\DB_Usuarios\DB_Exposure\Results_202211\Exp_2017-202209.txt', sep = ';', encoding = 'utf-8', index = False)


# In[ ]:




