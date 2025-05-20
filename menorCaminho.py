

import heapq

def dijkstra(grafo, inicio, destino):
    """
    Encontra o menor caminho entre dois nós em um grafo usando o algoritmo de Dijkstra.

    Args:
        grafo: Um dicionário de adjacências representando o grafo. 
               Chaves são nós, valores são listas de tuplas (vizinho, peso).
        inicio: O nó de partida.
        destino: O nó de destino.

    Returns:
        Um tuplo contendo o caminho mais curto (lista de nós) e o custo total (inteiro).
    """

    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]  # (distancia, no)
    caminho_anterior = {}

    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)

        if no_atual == destino:
            caminho = []
            no_corrente = destino
            while no_corrente:
                caminho.insert(0, no_corrente)
                no_corrente = caminho_anterior.get(no_corrente)
            return caminho, distancia_atual

        if distancia_atual > distancias[no_atual]:
            continue  # já encontramos uma distância menor para este nó

        for vizinho, peso in grafo[no_atual]:
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho_anterior[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return None, None  # Não há caminho
'''
# Exemplo de uso:
grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8)],
    'D': [('B', 5), ('C', 8)],
    'E': [('B', 9)],
    'F': [('D', 7)],
}

inicio = 'A'
destino = 'A'

caminho, custo = dijkstra(grafo, inicio, destino)

if caminho:
    print(f"Caminho mais curto de {inicio} para {destino}: {caminho}")
    print(f"Custo total: {custo}")
else:
    print(f"Não existe caminho entre {inicio} e {destino}")
'''