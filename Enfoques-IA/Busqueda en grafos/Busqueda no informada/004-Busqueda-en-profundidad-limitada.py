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
C.add_child(E)

# Realizar la búsqueda en profundidad limitada desde el nodo A con límite de profundidad 2
target_node = 'E'
depth_limit = 2

if dls(A, target_node, depth_limit):
    print(f"El nodo {target_node} se encuentra dentro del límite de profundidad {depth_limit}.")
else:
    print(f"El nodo {target_node} no se encuentra dentro del límite de profundidad {depth_limit}.")

