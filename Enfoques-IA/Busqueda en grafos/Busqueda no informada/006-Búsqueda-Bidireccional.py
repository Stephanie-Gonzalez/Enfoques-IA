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

# Función de búsqueda bidireccional
def bidirectional_search(start, goal):
    # Estructuras de datos para la búsqueda desde el inicio y el objetivo
    forward_queue = [start]
    backward_queue = [goal]
    forward_visited = {start}
    backward_visited = {goal}

    while forward_queue and backward_queue:
        # Búsqueda desde el inicio
        current_forward = forward_queue.pop(0)

        # Expandir sucesores desde el estado actual
        for child in current_forward.children:
            if child not in forward_visited:
                forward_queue.append(child)
                forward_visited.add(child)

                # Verificar si el estado actual se encuentra en la búsqueda hacia atrás
                if child in backward_visited:
                    return "Se encontró una solución"

        # Búsqueda desde el objetivo
        current_backward = backward_queue.pop(0)

        # Expandir predecesores desde el estado actual
        for parent in current_backward.parents:
            if parent not in backward_visited:
                backward_queue.append(parent)
                backward_visited.add(parent)

                # Verificar si el estado actual se encuentra en la búsqueda hacia adelante
                if parent in forward_visited:
                    return "Se encontró una solución"

    return "No se encontró una solución"

# Crear los nodos del grafo
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

# Establecer las conexiones entre los nodos
A.add_child(B)
B.add_child(C)
C.add_child(D)
D.add_child(E)

# Realizar la búsqueda bidireccional desde el nodo A hasta el nodo E
start_node = A
goal_node = E

result = bidirectional_search(start_node, goal_node)
print(result)
