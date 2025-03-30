import heapq

def prim(grafo, inicio):
    nodos_conectados=set([inicio]) 
    aristas=[]  
    costo_total=0  
    monticulo_minimo=[]
    for vecino, costo in grafo[inicio].items():
        heapq.heappush(monticulo_minimo, (costo, inicio, vecino))

    while monticulo_minimo:
        costo, nodo_origen, nodo_destino=heapq.heappop(monticulo_minimo)

        if nodo_destino in nodos_conectados:
            continue

        nodos_conectados.add(nodo_destino)
        aristas.append((nodo_origen, nodo_destino, costo))
        costo_total+=costo

        for vecino, costo in grafo[nodo_destino].items():
            if vecino not in nodos_conectados:
                heapq.heappush(monticulo_minimo, (costo, nodo_destino, vecino))

    return aristas, costo_total

# Grafo de PCB
grafo_pcb={
    'Componente1': {'Componente2': 4, 'Componente3': 2},
    'Componente2': {'Componente1': 4, 'Componente4': 3},
    'Componente3': {'Componente1': 2, 'Componente4': 5},
    'Componente4': {'Componente2': 3, 'Componente3': 5}
}

aristas_seleccionadas, costo_total = prim(grafo_pcb, 'Componente1')
print("Arbol de Expansion Minima (MST):")
for arista in aristas_seleccionadas:
    print(f"{arista[0]}-{arista[1]} ({arista[2]})")

print(f"\nCosto total: {costo_total}")
