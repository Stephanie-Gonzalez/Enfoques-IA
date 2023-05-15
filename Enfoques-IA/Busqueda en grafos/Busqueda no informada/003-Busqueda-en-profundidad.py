# -*- coding: utf-8 -*-
"""

@author: sttep
"""

# Clase para representar los nodos del grafo
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

# Función de búsqueda en profundidad
def dfs(node):
    node.visited = True
    print(node.name)

    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs(neighbor)

# Crear los nodos del grafo
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

# Establecer las conexiones entre los nodos
A.add_neighbor(B)
A.add_neighbor(D)
B.add_neighbor(C)
D.add_neighbor(E)

# Realizar la búsqueda en profundidad desde el nodo A
dfs(A)


