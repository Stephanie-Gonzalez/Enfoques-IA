# -*- coding: utf-8 -*-
"""

@author: sttep
"""
from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))  # Prioridad y nodo inicial

    while not queue.empty():
        cost, node = queue.get()
        if node == goal:
            # Se ha encontrado el objetivo
            return visited

        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            for neighbor, neighbor_cost in neighbors.items():
                if neighbor not in visited:
                    # Utilizamos la heurística para determinar la prioridad del siguiente nodo
                    priority = heuristic(neighbor, goal)
                    queue.put((priority, neighbor))

    return None  # No se encontró una solución


# Función heurística que estima la distancia entre un nodo y el objetivo
def heuristic(node, goal):
    # Aquí puedes implementar tu propia heurística según el problema
    # La heurística debe ser admissible (nunca sobreestimar el costo real)
    return 0  # Heurística trivial en este ejemplo


# Grafo de ejemplo representado como un diccionario
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 6},
    'D': {},
    'E': {'G': 1},
    'F': {},
    'G': {}
}

start_node = 'A'
goal_node = 'G'

result = greedy_best_first_search(graph, start_node, goal_node)
if result is None:
    print("No se encontró una solución.")
else:
    print("Se encontró una solución:", result)

