# -*- coding: utf-8 -*-
"""

@author: sttep
"""

# Clase para representar los nodos del grafo
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Función de búsqueda en profundidad limitada
def dls(node, target, depth_limit):
    if node.name == target:
        return True

    if depth_limit <= 0:
        return False

    for child in node.children:
        if dls(child, target, depth_limit - 1):
            return True

    return False

# Función de búsqueda en profundidad iterativa
def iddfs(root, target):
    depth_limit = 0
    while True:
        if dls(root, target, depth_limit):
            return True
        depth_limit += 1

        # Reiniciar el estado de visitado para la próxima iteración
        reset_visited(root)

# Función para reiniciar el estado de visitado de los nodos
def reset_visited(node):
    if node is None:
        return

    node.visited = False
    for child in node.children:
        reset_visited(child)

# Crear los nodos del grafo
node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')

# Establecer las conexiones entre los nodos
node_A.add_child(node_B)
node_A.add_child(node_C)
node_B.add_child(node_D)
node_C.add_child(node_E)

# Realizar la búsqueda en profundidad iterativa desde el nodo A buscando el nodo 'E'
target_node = 'E'

if iddfs(node_A, target_node):
    print(f"El nodo {target_node} se encontró.")
else:
    print(f"El nodo {target_node} no se encontró.")
