import warnings

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Silenciar advertencias 
warnings.filterwarnings("ignore", category=UserWarning)

inercias = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k).fit(clientes.values) #Crea k modelos de kmeans para diferente num de clusters
    inercias.append(kmeans.inertia_) #Almacena la inercia de cada modelo

plt.figure(figsize=(6, 5), dpi=100)
plt.scatter(range(2, 10), inercias, marker="o", s=180, color="purple")
plt.xlabel("Numero de clusters", fontsize=25)
plt.ylabel("Inercia", fontsize=25)
plt.show()