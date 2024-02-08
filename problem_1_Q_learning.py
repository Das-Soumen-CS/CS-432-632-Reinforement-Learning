import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd


G = nx.Graph()

G.add_edge("1", "3", weight=1)
G.add_edge("1", "5", weight=1)
G.add_edge("2", "3", weight=1)
G.add_edge("3", "1", weight=1)
G.add_edge("3", "4", weight=1)
G.add_edge("3", "2", weight=1)
G.add_edge("4", "0", weight=1)
G.add_edge("4", "3", weight=1)
G.add_edge("4", "5", weight=1)
G.add_edge("5", "1", weight=1)
G.add_edge("5", "4", weight=1)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=4)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()

# create distance matrix
R_matrix = np.array([[0,-1,-1,-1,1,-1], [-1,0,-1,1,-1,-1], [-1,-1,0,1,-1,-1],[-1,1,1,0,1,-1],[-1,-1,-1,1,0,1],[1,-1,-1,-1,1,0]])
print(R_matrix)

for i in R_matrix:
    source=R_matrix[i]
    print(source)
    pass