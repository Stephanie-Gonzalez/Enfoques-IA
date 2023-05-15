# -*- coding: utf-8 -*-
"""
@author: sttep
"""
import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo vacío
graph = nx.DiGraph()

# Agregamos los nodos a la red de decisión
graph.add_node("Start")
graph.add_node("NodeA")
graph.add_node("NodeB")
graph.add_node("NodeC")
graph.add_node("End")

# Agregamos las aristas que representan las decisiones y resultados
graph.add_edge("Start", "NodeA", decision="Decision 1")
graph.add_edge("Start", "NodeB", decision="Decision 2")
graph.add_edge("NodeA", "NodeC", decision="Decision 3")
graph.add_edge("NodeB", "NodeC", decision="Decision 4")
graph.add_edge("NodeC", "End", decision="Decision 5")

# Dibujamos el grafo
pos = nx.spring_layout(graph)
edge_labels = nx.get_edge_attributes(graph, 'decision')
nx.draw_networkx(graph, pos, with_labels=True, node_size=1000)
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

# Mostramos el grafo
plt.axis('off')
plt.show()
