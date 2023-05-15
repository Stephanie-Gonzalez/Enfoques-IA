# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import heapq

# Definición de la clase Nodo
class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
    
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

# Función de búsqueda en línea utilizando el algoritmo A*
def online_search(start_state, goal_state, get_successors, heuristic):
    open_list = []
    closed_set = set()
    
    # Se crea el nodo inicial
    start_node = Node(start_state, cost=0, heuristic=heuristic(start_state, goal_state))
    heapq.heappush(open_list, start_node)
    
    while open_list:
        # Se obtiene el nodo con menor costo de la lista abierta
        current_node = heapq.heappop(open_list)
        
        if current_node.state == goal_state:
            # Se ha alcanzado el estado objetivo
            return reconstruct_path(current_node)
        
        closed_set.add(current_node.state)
        
        # Se generan los sucesores del nodo actual
        successors = get_successors(current_node.state)
        
        for successor, cost in successors:
            if successor not in closed_set:
                # Se crea un nuevo nodo para el sucesor
                successor_node = Node(successor, parent=current_node,
                                      cost=current_node.cost + cost,
                                      heuristic=heuristic(successor, goal_state))
                heapq.heappush(open_list, successor_node)
    
    # No se encontró un camino hasta el estado objetivo
    return None

# Función para reconstruir el camino desde el nodo objetivo hasta el nodo inicial
def reconstruct_path(node):
    path = []
    current_node = node
    while current_node:
        path.append(current_node.state)
        current_node = current_node.parent
    path.reverse()
    return path

# Ejemplo de uso
# Grafo representado como un diccionario de sucesores y costos
graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 5), ('E', 4)],
    'C': [('F', 6)],
    'D': [('G', 7)],
    'E': [('G', 4)],
    'F': [],
    'G': []
}

# Función heurística (distancia Manhattan)
def heuristic(state, goal_state):
    return abs(ord(goal_state) - ord(state))

start_state = 'A'
goal_state = 'G'

# Función para obtener los sucesores de un estado en el grafo
def get_successors(state):
    return graph[state]

# Búsqueda en línea utilizando A*
path = online_search(start_state, goal_state, get_successors, heuristic)

if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró un camino hasta el estado objetivo.")

