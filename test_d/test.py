# import networkx as nx
# import matplotlib.pyplot as plt
#
# G=nx.Graph()
# G.add_node("a")
# G.add_nodes_from(["b","c"])
#
# G.add_edge(1,2)
# edge = ("d", "e")
# G.add_edge(*edge)
# edge = ("a", "b")
# G.add_edge(*edge)
#
# print("Nodes of graph: ")
# print(G.nodes())
# print("Edges of graph: ")
# print(G.edges())
#
# # G.add_edges_from([("a","c"),("c","d")])
#
# nx.draw(G)
# plt.show() # display

import networkx as nx
import matplotlib.pyplot as plt
import graph_calc

g = nx.Graph()


def add_vertices(graph, vertices):
    for el in vertices:
        graph.add_node(el)


def add_edges(graph, edges):
    for el in edges:
        graph.add_edge(el[0], el[1])


initial_sequence = [1, 2, 3, 4, 5, 6, 7, 10, 9, 8]
array = []

vertices = graph_calc.Vertices(initial_sequence, array)
# print(array)

v = graph_calc.parse_to_vertices(array)
e = graph_calc.parse_to_edges(array)
# print(e)
add_vertices(g, v)
add_edges(g, e)

nx.draw(g)
plt.savefig("path_graph1.png")
plt.show()
