import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def display_network():
    # Create an empty graph
    G = nx.Graph()

    # Add selected nodes to the graph
    for i in range(1, 5):
        if checkbox_vars[i-1].get():
            G.add_node(i)

    # Add edges (customize this based on your network structure)
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

    # Draw the network
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', edge_color='gray')

    # Display the network in a Tkinter window
    canvas.draw()

def on_checkbox_change():
    display_network()

# Create a Tkinter window
root = tk.Tk()
root.title("Dynamic Network Display with Tkinter and NetworkX")

# Create checkboxes
checkbox_vars = []
checkboxes = []
for i in range(1, 5):
    var = tk.IntVar()
    checkbox_vars.append(var)
    checkbox = ttk.Checkbutton(root, text=f"Node {i}", variable=var, command=on_checkbox_change)
    checkboxes.append(checkbox)
    checkbox.grid(row=i, column=0, sticky=tk.W)

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(5, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=1, rowspan=5)

# Initial display
on_checkbox_change()

# Start the Tkinter event loop
root.mainloop()
