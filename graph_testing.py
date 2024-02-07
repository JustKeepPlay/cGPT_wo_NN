import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges without explicitly adding nodes
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 1)])

# Define a list of colors for nodes
color_list = ['red', 'blue', 'green', 'yellow', 'orange']

# Draw the graph with nodes colored according to the color_list
nx.draw(G, with_labels=True, node_color=color_list)
plt.show()
