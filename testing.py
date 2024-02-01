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

list = [1,2,3,4,5]

for i in range(len(list) - 1, 0, -1):
    print(list[i])

