import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Graph_Learner import doc_graph

G = nx.DiGraph()
doc = doc_graph()

def create_evaluation_page(notebook):
    global evaluation_page
    evaluation_page = tk.Frame(notebook)
    notebook.add(evaluation_page, text="Evaluation Phase")

    # Create a button to trigger the Evaluation on the evaluation page
    evaluation_button = tk.Button(evaluation_page, text="Evaluate", command=create_network)
    evaluation_button.pack()


def create_network():
    G.add_edges_from(doc.edge_table)

    # Clear the previous network graph (if any)
    if hasattr(create_network, 'canvas'):
        create_network.canvas.get_tk_widget().destroy()

    # Create a new Matplotlib figure for the network graph
    fig, ax = plt.subplots()
    ax.set_title('Network Graph')

    pos = nx.kamada_kawai_layout(G)

    # Draw the network graph
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightgreen'
    )

    # Embed the Matplotlib network graph in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=evaluation_page)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Add the Matplotlib NavigationToolbar2Tk
    toolbar = NavigationToolbar2Tk(canvas, evaluation_page)
    toolbar.update()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
