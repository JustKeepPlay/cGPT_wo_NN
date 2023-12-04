import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_evaluation_page(notebook):
    evaluation_page = tk.Frame(notebook)
    notebook.add(evaluation_page, text="Evaluation Phase")
    # Add widgets and functionality for the evaluation page as needed


def create_directed_graph():
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes
    G.add_nodes_from([1, 2, 3, 4])

    # Add directed edges
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 1)

    # Plot the directed graph
    fig, ax = plt.subplots()
    nx.draw(G, with_labels=True, ax=ax)
    
    # Embed the Matplotlib graph in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=evaluation_page)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

def create_evaluation_page(notebook):
    global evaluation_page
    evaluation_page = tk.Frame(notebook)
    notebook.add(evaluation_page, text="Evaluation Phase")

    # Add widgets and functionality for the evaluation page as needed
    create_directed_graph()
