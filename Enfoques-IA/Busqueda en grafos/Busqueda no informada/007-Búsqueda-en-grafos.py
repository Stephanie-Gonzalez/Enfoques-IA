# -*- coding: utf-8 -*-
"""

@author: sttep
"""

from collections import deque

# Clase para representar los nodos del grafo
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Función de búsqueda en anchura (BFS)
def bfs_search(start, goal):
    queue = deque()  # Cola para almacenar los nodos a explorar
    visited = set()  # Conjunto para almacenar los nodos visitados
    queue.append(start)  # Agregar el nodo de inicio a la cola

    while queue:
        current_node = queue.popleft()  # Extraer el primer nodo de la cola

        if current_node == goal:  # Verificar si se encontró el objetivo
            return "Se encontró una solución"

        # Agregar los nodos vecinos no visitados a la cola
        for child in current_node.children:
            if child not in visited:
                queue.append(child)
                visited.add(child)

    return "No se encontró una solución"

# Crear los nodos del grafo
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

# Establecer las conexiones entre los nodos
A.add_child(B)
A.add_child(C)
B.add_child(D)
C.add_child(D)
D.add_child(E)

# Realizar la búsqueda en anchura desde el nodo A hasta el nodo E
start_node = A
goal_node = E

result = bfs_search(start_node, goal_node)
print(result)
