import numpy as np

def distancia_euclidiana(p1, p2):
    return np.sqrt(np.sum((p1-p2)**2))

class UnionFind:
    def __init__(self, n):
        self.padre=list(range(n))

    def encontrar(self, x):
        if self.padre[x]!=x:
            self.padre[x]=self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        raizX=self.encontrar(x)
        raizY=self.encontrar(y)
        if raizX!=raizY:
            self.padre[raizY]=raizX

def kruskal_clusterizacion(puntos, umbral):
    n=len(puntos)
    aristas=[]
    
    for i in range(n):
        for j in range(i+1, n):
            dist=distancia_euclidiana(puntos[i], puntos[j])
            aristas.append((dist, i, j))
    
    aristas.sort()  # Ordenar las distancias de menor a mayor
    uf=UnionFind(n)
    clusters=[]

    for dist, i, j in aristas:
        if dist>umbral:
            break
        if uf.encontrar(i)!=uf.encontrar(j):
            uf.unir(i, j)

    for i in range(n):
        raiz=uf.encontrar(i)
        if raiz not in clusters:
            clusters.append(raiz)

    return clusters

# Datos para la clusterizacion
datos=np.array([[1, 1], [2, 2], [6, 6], [7, 7]])
umbral=3 

clusters=kruskal_clusterizacion(datos, umbral)
print(f"Clusters formados: {clusters}")
