# -*- coding: utf-8 -*-
"""

@author: sttep
"""

from queue import PriorityQueue

def A_star_search(graph, start, goal, heuristic):
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
                    # Costo acumulado desde el inicio hasta el vecino
                    g = cost + neighbor_cost
                    # Estimación heurística desde el vecino hasta el objetivo
                    h = heuristic(neighbor, goal)
                    # Prioridad total: g + h
                    priority = g + h
                    queue.put((priority, neighbor))

    return None  # No se encontró una solución


def AO_star_search(graph, start, goal, heuristic, max_open_nodes):
    visited = set()
    open_nodes = PriorityQueue()
    open_nodes.put((0, start))  # Prioridad y nodo inicial

    while not open_nodes.empty():
        cost, node = open_nodes.get()
        if node == goal:
            # Se ha encontrado el objetivo
            return visited

        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            for neighbor, neighbor_cost in neighbors.items():
                if neighbor not in visited:
                    # Costo acumulado desde el inicio hasta el vecino
                    g = cost + neighbor_cost
                    # Estimación heurística desde el vecino hasta el objetivo
                    h = heuristic(neighbor, goal)
                    # Prioridad total: g + h
                    priority = g + h
                    open_nodes.put((priority, neighbor))
            
            # Control del número máximo de nodos abiertos
            if open_nodes.qsize() > max_open_nodes:
                break

    return None  # No se encontró una solución


# Ejemplo de grafo de búsqueda representado como un diccionario
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

# Función heurística que estima la distancia entre un nodo y el objetivo
def heuristic(node, goal):
    # Aquí puedes implementar tu propia heurística según el problema
    # La heurística debe ser admissible (nunca sobreestimar el costo real)
    return 0  # Heurística trivial en este ejemplo

# Ejemplo de búsqueda A*
result_a_star = A_star_search(graph, start_node, goal_node, heuristic)
if result_a_star is None:
    print("No se encontró una solución con A*.")
else:
    print("Se encontró una solución con A*:", result_a_star)

# Ejemplo de búsqueda AO*
max_open_nodes = 5  # Número máximo de nodos abiertos permitidos
result_ao_star = AO_star_search(graph, start_node, goal_node, heuristic, max_open_nodes)
if result_ao_star is None:
    print("No se encontró una solución con AO*.")
else:
    print("Se encontró una solución con AO*:", result_ao_star)
