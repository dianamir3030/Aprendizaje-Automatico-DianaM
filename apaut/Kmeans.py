import warnings

# Silenciar advertencias 
warnings.filterwarnings("ignore", category=UserWarning)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

clientes = pd.DataFrame({"saldo" : [50000, 45000, 48000, 43500, 47000, 52000,
                                    20000, 26000, 25000, 23000, 21400, 18000,
                                    8000, 12000, 6000, 14500, 12600, 7000],
                         "transacciones" : [25, 20, 16, 23, 25, 18, 
                                            23, 22, 24, 21, 27, 18, 8, 3, 6, 4, 9, 3]})

escalador = MinMaxScaler().fit(clientes.values)

clientes = pd.DataFrame(escalador.transform(clientes.values),
                       columns = ["saldo", "transacciones"])

kmeans = KMeans(n_clusters=3).fit(clientes.values) #fit es para que se ajuste a los datos

clientes["cluster"] = kmeans.labels_  #Asigna un cluster a cada cliente y agrega la columna

# print(kmeans.cluster_centers_, kmeans.inertia_) Permite ver la posicion de los centroides y el valor de la inercia
#La inercia nos dice que tan pegados estan los clientes de los centroides, entre más pegados es mejor (Identificas mejor los cluster)

# Instrucciones para graficar los cluster
plt.figure(figsize=(6, 5), dpi= 100) #Indica el tamaño y resolucion de la figura

colores = ["red", "blue", "orange", "black", "purple", "pink", "brown"] #colores que usa para graficar

#Par de graficas de dispersion, Una grafica cada cluster usando colores y la otra grafica los centroides
for cluster in range(kmeans.n_clusters):
    plt.scatter(clientes[clientes["cluster"] == cluster]["saldo"],
                clientes[clientes["cluster"] == cluster]["transacciones"],
                marker="o", s=180, color=colores[cluster], alpha=0.5)

    plt.scatter(kmeans.cluster_centers_[cluster][0],
                kmeans.cluster_centers_[cluster][1],
                marker="P", s=280, color=colores[cluster])

#Detalles de la grafica (Matplotlib)
plt.title("Clientes",fontsize=20)
plt.xlabel("Saldo en cuenta de ahorros (pesos)", fontsize=15)
plt.ylabel("Veces que uso la tarjeta de credito", fontsize=15)
plt.text(1.15, 0.2, "K = %i" % kmeans.n_clusters, fontsize=25)
plt.text(1.15, 0, "Inercia = %0.2f" % kmeans.inertia_, fontsize=25)
plt.xlim(-0.1,1.1)
plt.ylim(-0.1,1.1)
plt.show()

del clientes["cluster"]