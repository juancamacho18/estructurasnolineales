class UnionFind:
    def __init__(self, n):
        self.padre=list(range(n))
        self.rango=[0]*n

    def encontrar(self, x):
        if self.padre[x]!=x:
            self.padre[x]=self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        raizX = self.encontrar(x)
        raizY = self.encontrar(y)

        if raizX!=raizY:
            if self.rango[raizX]>self.rango[raizY]:
                self.padre[raizY]=raizX
            elif self.rango[raizX]<self.rango[raizY]:
                self.padre[raizX]=raizY
            else:
                self.padre[raizY]=raizX
                self.rango[raizX]+=1

def kruskal(grafo, n, mapeo):
    aristas=[]
    uf=UnionFind(n)

    for u in grafo:
        for v, costo in grafo[u].items():
            aristas.append((costo, mapeo[u], mapeo[v]))

    aristas.sort()  # Ordenar las aristas por peso
    mst=[]
    costo_total=0

    for peso, u, v in aristas:
        if uf.encontrar(u)!=uf.encontrar(v):
            uf.unir(u, v)
            mst.append((u, v, peso))
            costo_total+=peso

    return mst, costo_total

# Grafo de rutas eléctricas
grafo_electricidad={
    'Casa1': {'Casa2': 3, 'Casa3': 4},
    'Casa2': {'Casa1': 3, 'Casa4': 5},
    'Casa3': {'Casa1': 4, 'Casa4': 2},
    'Casa4': {'Casa2': 5, 'Casa3': 2}
}

nodos=list(grafo_electricidad.keys())
mapeo={nodo: i for i, nodo in enumerate(nodos)}
aristas_seleccionadas, costo_total=kruskal(grafo_electricidad, len(nodos), mapeo)

# Mostrar el resultado
print("Arbol de Expansion Minima (MST):")
for arista in aristas_seleccionadas:
    u, v, peso=arista
    casa_u=nodos[u]
    casa_v=nodos[v]
    print(f"{casa_u}-{casa_v} ({peso})")

print(f"\nCosto total: {costo_total}")
