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

from collections import defaultdict
import random

# Sequences to learn from
sequences = [
    [76,86,2,77,30,4,18,26,52,95,21,88,62,92,54,90,65,1,91,6,56,56,31,79,41,64,82,53,100,35,72,38,5,34,92,91,37,66,1,96,5,81],
    [29,100,70,25,100,32,23,65,71,42,65,29,78,17,46,58,10,10,80,58,96,1,99,38],
    [40,72,51,69,52,69,30,62,51,93,78,64,31,12,95,13,73,78,62,69,80,19,46,87,52,6,72,75,97,31,7,92,91,48,13,52,33,50,52,33,29,13,89,3,96,21,67,71,17,87,26,83,82,4,18,10,29,4,82,48,55,55,50,2,73,27,73,12,16,34,92,30,19,68,56,80,64,65,34,64,50,72],
    [84,19,29,66,80,96,41,81,38,56,100,6,50,10,34,79,43,64,7,96,58,87,97,38,7,94,98,59,89,22,100,92,38,45,82,24,4,84,78,12,45,92,35,84,48,33,44,62,62,34,35,55,31,1],
    [45,24,40,17,60,100,94,8,96,73,68,18,28,14,69,51,12,17,69,80,35,72,17,94,14,39,86,25,91,74],
    [72,31,41,36,34,73,40,25,29,72,49,43,57,11,36,79,64,35,53,95,23],
    [48,87,70,95,37,86,19,34,59,83,4,43,70,7,37,93,7,100,5,66,15,62,99,30,74,76,46,66,37,20,49,25,15,63,25,46,60,22,56,81,33,6,17,96,2,86,59,98,96,44,82,83,29,44,38,34,29,32,33,41,26,89,87,53,72,60,89,22,19,25,50,28,20,36,92,19,21,88,47,92,18,14,9,96,76,18,77,17],
    [59,84,93,20,25,22,68,85,13,69,17,89,27,73,27,33,28,69,32,3,96,6,46,47,51,32,81,1,53,93,9,100,38,7,55,46,31],
    [84,60,81,98,74,71,5,81,57,87,87,99,81,42,61,15,91,70,78,55,24,90,16,97,5,46,84,43,40,34,73,9,11,55,35,46,98,66,24,76,3,64],
    [12,3,64,41,27,73,55,75,3,34,59,6,71,40,34,80,27,93,89,77,41,64,65,42,91,43,12,73,68,68,8,12,53,66,83,8,2,48,68],
    [44,85,37,65,13,73,75,8,11,75,17,44,16,78,100,18,51],
    [62,67,28,93,43,42,17,83,34,94,2,75,48,96,77,82,39,14,10,59,42,26,56,2,8,9,9,74,39,66,10,27,79,90,21,16,21,62,83,13,41,69,35,90,14,38,77,49,96,13,5,42,80,56,95,86,1,41,91,68,22,57,56,3,93,31,69,18,97,75,76,42,100,19,42,62,59,69,60,80,45,28,11,93,2,89,46,88,71,31,58,75,31,24,72,72],
    [99,92,17,29,59,8,36,27,12,49,90,97,42,84,89,9,90,25,62,13,8,82,63,87,20,59,59,63,98,98],
    [93,30,96,4,30,9,79,70,52],
    [9,45,25,51,57,68,100,10,84,53,75,37,31],
    [60,18,6,75,49,57,41,50,42,1,56,8,89,100,81,59,54,65,37,87,15,41,83,57,38,64,20,56,97,62,87,32,18,95,43,36,16,26,55,97,46,25,95,47,33,31,7,13,69,43,74,20,53,12,83,23,59,22,67,62,81,100,14,27,34,65,98,5,94,57,59,60,99,28,97,96,44,76,39,25,95,61],
    [34,7,55,35,78,61],
    [38,4,91,76,48,59,46,69,52,18,31,27,41,76,4,11,43,44,77,85,57,45,84,41,97,17,97,29,38,21,83,25,13,96,8,20,80,43,37,89,73,98,16,45,23,24,79,42,73,73,75,94,23,55,25,3,7,7,21,62,71,33,4,65,79,81,65,13,72,47,71,16,27,42,81,74,48,61,79,79,35,91,32,64,39,44,74,95,15,82,46,29,36,37,14,83,32,84],
    [65,97,74,11,72,44,71,92,27,72,18,37,19,30,17,73,51,26,15,59,51,80,1,75,86,45,65,37,87,39,93,36,47,91,3,61,61,53,15,31,64,99,63,36,1,48,100,14,18,90],
    [45,68,13,48,96,45,88,96,25,30,23,60,37,74,89,82,23,11,55,62,24,9,50,15,32,74,44,50,81,80,17,98,98,71,70,39,68,97,5,60,81,69,47,32,38,34,98,1,90],
    [4,51,32,20,42,7,91,43,69,39,33,87,20,43,33,42,14,78,76,37,57,37,96,91,56,90,85,6,71,1,69,94,87,80,51,48,56,89,44,67,94,78,60,59,78,23,19,96,68,91,84,56,15,75,50,52,10,22,49,7,56,2,48,48,28,32,41,54,82,88,31,100,39,87,81,32,60,54,16],
    [85,30,76,66,85,28,24,71,63,46,65,26,14,9,13,95,82,41,97,43,93,34,71,28,51,42,45,35,75,100,48,45,30,24,52,98,33,25,4,79,51,15,25,86,90,38,45,36,87,62,12,100,28,95,14,30,37,91,25,41,66,62,93,68,34,84,20,98,27,23,10,88,47,76,13,67,21,95,45,90,70,84,27,60,5,54,9,20,20,21,5,17,93,54],
    [40,10,15,53,21,93,6,71,57,3,69,50,4,28,22,13,26,65,1,82,4,60,19,10,94,26,38,3,18,44,79,60,95,64,26,20,36,32,18,60,10,23,94,5,85,53,98,98,49,57,11,82,71,49,96,7,41,43,47,37,81,51,49,9,80,42,58,61,53,70,45,43,5,62,75,12,15,100,2,88,65,98,60,7,10,74,45,50,5,62,30,38,50,86,90,83],
    [1,99,31,94,11,22,77,59,82,59,84,59,91,59,65,30,17],
    [53,39,68,31,42,45,19,27,94,84,49,38,94,73,94,31,39,99,11,17,69,28,96,43,63,10,17,39,60,4,83,48,73,39,61,90,76,39,40,27,41,65,83,55,31,41,80,82,7,43,71,98,82,56,61,90,20,100,17,33,39,52,96,85,28,57,71,79,41,83,1,74,57,68,86,59,38,20,1,69,36,49,75,77,64,58],
    [61,100,14,52,47,63,88,80,93,14,85,22,2,6,99,1,52,4,68,87,25,88,71,98,33,55,91,51,46,42,13,64,94,47,54,32,66,72,95,79],
    [38,7,61,68,49,94,32,20,6,89,48,84,4,65,5,67,81,46,16,22,70,88,22,39,76,50,21,76,8,46,5,3,98,91,52,12,97,62,77,46,100,36,92,31,10,3,16,79,17,30,84,54,8,7,69,30,44,12,88,99,71,25,88,98,89,86,39,42,44,55],
    [16,66,45,46,71,18,36,32,12,25,47,11,64,89,64,81,40,48,10,9,70,82,14,97,87,87,43,9,85,14,86,31,29,79,5,98,84,17,44,7,44,89,51,18,95,96,63,7,49,61,5,23,99,95,51,42,68,4,98,89,9,68,96,90,45,40,50,44,3,42,15,11,72,17,81,15,55,98,41,54,10,17,16,80,55,7,55],
    [36,29,94,8,1,72,82,24,93,66,85,39,38,57,71,73,37,79,99,1,76,82,98,15,47,9,18,80,37,57,25,45,45,70,8,49,8,83,10,67,97,43,71,94,49,16,39,1,97,90,88,28,12,46,52,89,6,67,10,39,28,89,93,17,69,3,50,27,79,65,13,89,83,3,52,83,79,51,37,36,69,67,79,32,92,92,83,25,27,43,95,93,25],
    [93,25,22,95,1,75,66,81,70,89,58,50,82,23,42,76,47,5,12,44,26,93,4,49,61,97,3,56,49,82,93,57,12,86,82,36,54,28,62,87,77,92,59,40,7,70,4,42,35,16,97,33,1,25,65,30,99,47,18,71,64,55,42],
]

import random
from collections import defaultdict

# Define a function to learn from sequences and generate the next number
def learn_and_generate(sequences):
    # Initialize a dictionary to store the frequency of each number following a sequence
    frequency_dict = defaultdict(lambda: defaultdict(int))
    
    # Learn from sequences
    for sequence in sequences:
        history = []  # Initialize history for each sequence
        for number in sequence:
            if history:  # If history exists, consider the last number in history for the sequence
                frequency_dict[tuple(history)][number] += 1
                if len(history) > 1:
                    history.pop(0)  # Remove the oldest number from history
            history.append(number)  # Add the current number to history
    
    # Function to generate the next number in the sequence based on history
    def generate_next_number(history):
        next_number_frequency = frequency_dict.get(tuple(history), {})
        
        if not next_number_frequency:
            return None  # If no number follows the history, return None
        
        # Choose the next number randomly based on the frequencies
        total_frequency = sum(next_number_frequency.values())
        rand_val = random.randint(1, total_frequency)
        
        for number, freq in next_number_frequency.items():
            rand_val -= freq
            if rand_val <= 0:
                return number
    
    # Generate the next numbers for each sequence based on its history
    next_numbers = []
    for sequence in sequences:
        history = list(sequence)[:-1]  # Initialize history for each sequence based on the sequence itself
        next_number = generate_next_number(history)
        next_numbers.append(next_number)
    
    return next_numbers

next_numbers = learn_and_generate(sequences)
print("Generated next numbers:", next_numbers)











    






    







