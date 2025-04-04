def floyd_warshall(graph, n):
    dist=[[float('inf')]*n for _ in range(n)]
    next_node=[[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i==j:
                dist[i][j]=0
            elif (i, j) in graph:
                dist[i][j]=graph[(i, j)]
                next_node[i][j]=j  

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
                    next_node[i][j]=next_node[i][k]  

    return dist, next_node

# Funcion para reconstruir la ruta mas corta entre dos nodos
def reconstruct_path(next_node, start, end):
    path=[]
    if next_node[start][end]==-1:
        return path 
    current=start
    while current!=end:
        path.append(current)
        current=next_node[current][end]
    path.append(end)
    return path
    
def distance_matrix(dist, node_names):
    print("\nMatriz de distancias:")
    print("    " + "   ".join([node_names[i] for i in range(len(node_names))]))  
    for i in range(len(dist)):
        row=[node_names[i]] + [f"{dist[i][j]:3}" if dist[i][j] != float('inf') else "INF" for j in range(len(dist[i]))]
        print("   ".join(row))

def main():
    print("Red de fibra optica")
    graph = {
        (0, 1): 10,  # CD1 → CD2= 10 ms CD=Centro de Datos
        (1, 2): 5,  # CD2 → CD3= 5 ms
        (2, 3): 8,  # CD3 → CD4= 8 ms
        (0, 3): 30   # CD1 → CD4= 30 ms
    }

    n=4 
    node_names={0: 'CD1', 1: 'CD2', 2: 'CD3', 3: 'CD4'}
    origen=int(input("Ingrese el nodo de origen Centro 1(0), Centro 2(1), Centro 3(2), Centro 4(3): "))
    destino=int(input("Ingrese el nodo de destino Centro 1(0), Centro 2(1), Centro 3(2), Centro 4(3): "))
    
    if origen<0 or origen>=n or destino<0 or destino>=n:
        print("Error, nodo no valido")
        return
    

    dist, next_node=floyd_warshall(graph, n)
    distance_matrix(dist, node_names)
    distance=dist[origen][destino]
    path=reconstruct_path(next_node, origen, destino)

    if distance==float('inf'):
        print(f"No hay una ruta directa entre {node_names[origen]} y {node_names[destino]}.")
    else:
        path_in_letters=[node_names[node] for node in path]
        print(f"La ruta del {node_names[origen]} a {node_names[destino]} es: {path_in_letters} con una latencia de {distance} ms.")

if __name__ == '__main__':
    main()
