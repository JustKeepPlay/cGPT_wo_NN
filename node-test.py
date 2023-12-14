import networkx as nx
import matplotlib.pyplot as plt

# Create a graph (you can replace this with your own graph)
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4), (4, 5)])

# Get the degree of each node
degrees = dict(G.degree())

# Count the frequency of each degree
degree_freq = {}
for degree in degrees.values():
    if degree in degree_freq:
        degree_freq[degree] += 1
    else:
        degree_freq[degree] = 1

# Print the frequency of edges based on the degree of their nodes
for edge in G.edges():
    edge_degree_freq = degree_freq[degrees[edge[0]]] + degree_freq[degrees[edge[1]]]
    print(f"Edge {edge} has a frequency of {edge_degree_freq}")

fig, axe = plt.subplots(figsize=(12,7))
axe.set_title(G.edges, loc='right')

# Draw the graph
pos = nx.spring_layout(G)  # You can use different layout algorithms
nx.draw(G, pos, ax=axe,with_labels=True, node_color='skyblue', node_size=700, font_size=10, font_color='black')

# Display the plot
plt.show()

