# my_dict = {}
# seq_list = ['1|2', '2|3', '3|4', '4|5', '5|6', '2|3']
# weight_list = [10, 20, 30, 40, 50, 20]

# # seq : weight

# for i in range(6):
#     if seq_list[i] in my_dict:
#         my_dict[seq_list[i]] += weight_list[i]
#     else:
#         my_dict[seq_list[i]] = weight_list[i]

# print(my_dict)
# print(my_dict['3|4'], " is ", type(my_dict['3|4']))

# import random 

# seq_list = {}
# list = []


# while seq_list[tuple(list)] is not None:
#     for j in range(5):
#         list.append(random.randint(1, 10))

#     if tuple(list) in seq_list:
#         seq_list[tuple(list)] = None
#     else:
#         seq_list[tuple(list)] = 1

#     list.clear()
    
# for key, value in seq_list.items():
#     print(f"{key}: {value}")

# print("This dick has: ", len(seq_list.keys()))

# import tkinter as tk

# class NumberIncrementerApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Number Incrementer")

#         self.number = 0

#         self.label = tk.Label(master, text=str(self.number))
#         self.label.pack(pady=10)

#         self.increment_button = tk.Button(master, text="Increment", command=self.increment_number)
#         self.increment_button.pack()

#     def increment_number(self):
#         self.number += 1
#         self.label.config(text=str(self.number))

# def main():
#     root = tk.Tk()
#     app = NumberIncrementerApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()

# my_dict = {}

# for i in range(5):
#     my_dict[i] = {}
#     for j in range(10):
#         my_dict[i][j] = {}
#         for k in range(3):
#             my_dict[i][j][k] = f"Value: {k}"
#         print(f"my_dict[{i}][{j}]]: {my_dict[i][j]}")
#     print("\n")

# import matplotlib.pyplot as plt
# import networkx as nx

# def create_dynamic_graph(number_sequences, conflicts):
#     G = nx.DiGraph()

#     for seq in number_sequences:
#         G.add_node(seq)

#     for conflict in conflicts:
#         seq1, seq2 = conflict
#         if G.has_edge(seq1, seq2):
#             # Resolve conflict by adjusting the edge weight
#             G[seq1][seq2]['weight'] += 1
#         else:
#             G.add_edge(seq1, seq2, weight=1)

#     return G

# def draw_dynamic_graph(G):
#     pos = nx.spring_layout(G)  # You can use other layout algorithms as well
#     labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8)
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
#     plt.show()

# # Example usage:
# number_sequences = [1, 2, 3, 4]
# conflicts = [(1, 2), (2, 3), (3, 4), (1, 4)]

# dynamic_graph = create_dynamic_graph(number_sequences, conflicts)
# draw_dynamic_graph(dynamic_graph)

# import random

# edges = [(1,2), (1,3), (1,4)]
# edges_amount = {}
# for edge in edges:
#     if edge not in edges_amount:
#         edges_amount[edge] = 1
#     else:
#         edges_amount[edge] += 1

# prob = []
# totalWeight = sum(edges_amount.values())

# for edge in edges_amount:
#     prob.append(edges_amount[edge] / totalWeight)


# amount = 500000
# one = 0
# two = 0
# three = 0
# for i in range(amount):
#     # edge = random.choices([_ for _ in edges_amount.keys()], prob)
#     edge = random.choice(edges)
#     if edge == (1,2):
#         one += 1
#     elif edge == (1,3):
#         two += 1
#     elif edge == (1,4):
#         three += 1
#     else:
#         continue

# total = one + two + three
# # Check if total is zero before performing division
# if total != 0:
#     print(f"(1,2): {one / total * 100}%")
#     print(f"(1,3): {two / total * 100}%")
#     print(f"(1,4): {three / total * 100}%")
# else:
#     print("No edges were selected.")


# data = {
#     1: ((1, 2), (1, 2)),
#     2: ((2, 3), (2, 4)),
#     3: ((3, 4),),
#     4: ((4, 5), (4, 6)),
#     6: ((6, 8),)
# }

# # Initialize an empty list to store the connected sequence
# connected_sequence = []

# # Iterate over the tuples in the dictionary and concatenate their elements
# for value in data.values():
#     for pair in set(value):
#         connected_sequence.extend(pair)

# print("Connected sequence:")
# print(connected_sequence)

# def find_sequences_in_list(number, lst):
#     sequences = []
#     for sublist in lst:
#         if all(num in sublist for num in number):
#             indices = [sublist.index(num) for num in number]
#             if indices == list(range(min(indices), max(indices) + 1)):
#                 sequences.append(sublist)
#     return sequences

# lst_data = [[1,2,3,4,5], [1,2,4,6,8], [1,3,5,7,9], [1,2,3,5,7,9,10]]
# number = [1, 2, 3]

# sequences = find_sequences_in_list(number, lst_data)

# if sequences:
#     print("Sequences", number, "are present in the list. Sequences:", sequences)
# else:
#     print("Sequences", number, "are not present in the list.")


import plotly.graph_objs as go
from plotly.offline import plot

# Create some sample data
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 13, 17, 18]

# Create a Plotly trace
trace = go.Scatter(x=x_values, y=y_values, mode='lines', name='Sample Data')

# Create a Plotly layout
layout = go.Layout(title='Sample Plot', xaxis=dict(title='X-axis'), yaxis=dict(title='Y-axis'))

# Create a Plotly figure
fig = go.Figure(data=[trace], layout=layout)

# Generate the HTML code for the plot
plot_html = plot(fig, output_type='div', include_plotlyjs=False)













    






    







