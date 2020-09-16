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

G=nx.path_graph(4)

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())
nx.draw(G)
plt.savefig("path_graph1.png")
plt.show()