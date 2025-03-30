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

# Grafo de telecomunicaciones
grafo_telecomunicaciones = {
    'Lima': {'Arequipa': 5, 'Trujillo': 3},
    'Arequipa': {'Lima': 5, 'Cusco': 2},
    'Trujillo': {'Lima': 3, 'Chiclayo': 4},
    'Cusco': {'Arequipa': 2},
    'Chiclayo': {'Trujillo': 4}
}

aristas_seleccionadas, costo_total = prim(grafo_telecomunicaciones, 'Lima')
print("Arbol de Expansion Minima (MST):")
for arista in aristas_seleccionadas:
    print(f"{arista[0]}-{arista[1]} ({arista[2]})")

print(f"\nCosto total: {costo_total}")
