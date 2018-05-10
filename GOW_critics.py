
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
from scipy import stats



# In[2]:


notas = pd.read_csv(r'./gow_critics_notas.csv')


# Vamos a contar las notas mínimas y notas máximas.

# In[3]:


cont_min = 0
cont_max = 0

arr_notas = np.array(notas)
arr_max = np.nanmax(arr_notas)
arr_min = np.amin(arr_notas)


# In[4]:


for nota_juego in arr_notas:
    if nota_juego == arr_min:
        cont_min += 1
    elif nota_juego == arr_max:
        cont_max += 1


# In[5]:


print("De un total de ", len(arr_notas), " notas:")
print("La nota mínima es: ", arr_min)
print("Cantidad de notas mínimas: ", cont_min)
print("La nota máxima es: ", arr_max)
print("Cantidad de notas máximas: ", cont_max)


# Media Normal

# In[6]:


print("La media sin redondear es:", np.mean(arr_notas))
print("La media redondeada es:", np.round_(np.mean(arr_notas), decimals=0))


# Moda

# In[7]:


notas_moda = stats.mode(arr_notas)
print("La nota que más se repite es:", notas_moda[0])


# Mediana (valor central del grupo de datos)

# In[10]:


notas_mediana = np.median(arr_notas)
print("La mediana de las notas es: ", notas_mediana)


# Otros tipos de media

# In[11]:


media_truncada = stats.tmean(arr_notas, (arr_min + 1, arr_max -1))
print("La media truncada de las notas es:", media_truncada)


# In[12]:


med_trunc_porc = stats.trim_mean(arr_notas, 0.1)
print("La media truncada sacando el 10% de cada extremo:", med_trunc_porc)


# Media Armónica

# In[29]:


med_armonica = stats.hmean(arr_notas)
print("La media armónica de las notas es:", med_armonica)


# Media Winsorizada (reemplazamos un porcentaje de las notas extremas por su nota más cercana)

# In[35]:


notas_winsorizadas = stats.mstats.winsorize(arr_notas, limits=0.05) #Detenerse mejor en esta parte.
med_winsorizada = np.mean(notas_winsorizadas)
print("La media con las notas winsorizadas es:", med_winsorizada)


# Media geométrica

# In[37]:


med_geo = stats.gmean(arr_notas)
print("La media geométrica de las notas es:", med_geo)


# Bonus: Media eliminando solo las notas 100.

# In[42]:


print("Bonus -> Media sin las notas 100: ", stats.tmean(arr_notas, (arr_min , arr_max -1)))

