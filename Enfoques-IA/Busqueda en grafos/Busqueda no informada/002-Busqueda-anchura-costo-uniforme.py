# -*- coding: utf-8 -*-
"""

@author: sttep
"""
import heapq

# Función de búsqueda en anchura de costo uniforme para el problema del TSP
def tsp_uniform_cost_search(graph, start):
    visited = set()
    queue = []
    heapq.heappush(queue, (0, start, [start]))

    while queue:
        cost, node, path = heapq.heappop(queue)

        if len(path) == len(graph) and path[0] == path[-1]:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in graph[node].items():
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))

    return None  # No se encontró una solución

# Ejemplo de uso
graph = {
    'A': {'B': 2, 'C': 4, 'D': 7},
    'B': {'A': 2, 'C': 5, 'D': 6},
    'C': {'A': 4, 'B': 5, 'D': 3},
    'D': {'A': 7, 'B': 6, 'C': 3}
}

start_node = 'A'

path = tsp_uniform_cost_search(graph, start_node)

if path:
    print("La ruta más corta encontrada es:")
    print(" -> ".join(path))
else:
    print("No se encontró una solución.")
