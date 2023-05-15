# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import math

# Función de heurística: distancia de Manhattan
def manhattan_distance(current, goal):
    x1, y1 = current
    x2, y2 = goal
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance

# Función de heurística: distancia euclidiana
def euclidean_distance(current, goal):
    x1, y1 = current
    x2, y2 = goal
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Ejemplo de uso de las heurísticas
start = (0, 0)
goal = (5, 5)

# Calcular la distancia de Manhattan entre el punto de inicio y el objetivo
manhattan_dist = manhattan_distance(start, goal)
print("Distancia de Manhattan:", manhattan_dist)

# Calcular la distancia euclidiana entre el punto de inicio y el objetivo
euclidean_dist = euclidean_distance(start, goal)
print("Distancia euclidiana:", euclidean_dist)
