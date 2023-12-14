import networkx as nx
from collections import Counter

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (1, 4), (4, 5), (3, 5), (2, 4), (1, 2), (2, 3)])

# Use Counter to count edge occurrences (sort nodes within each edge)
sorted_edges = [tuple(sorted(edge)) for edge in G.edges()]
edge_counter = Counter(sorted_edges)

# Print the edge frequencies
print("Edge frequencies:")
for edge, frequency in edge_counter.items():
    print(f"{edge}: {frequency} occurrences")
