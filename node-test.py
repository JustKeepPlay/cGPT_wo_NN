import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)])

# Specify the node you want to focus on
specified_node = 3

# Create a subgraph containing only the specified node and its neighbors
subgraph_nodes = nx.ego_graph(G, specified_node)

# Draw the subgraph
pos = nx.spring_layout(G)  # You can use other layout algorithms as well
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue')
nx.draw(subgraph_nodes, pos, with_labels=True, font_weight='bold', node_color='red', node_size=800)

plt.show()
