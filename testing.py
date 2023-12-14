import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import networkx as nx

# Create a simple graph for illustration
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Create a Tkinter window
evaluation_page = tk.Tk()
evaluation_page.title("NetworkX Graph with Custom Toolbar")

# Create a Matplotlib figure and a NetworkX graph
fig, ax = plt.subplots()
nx.draw(G, with_labels=True, ax=ax)

# Create a canvas to embed Matplotlib figure in Tkinter window
canvas = FigureCanvasTkAgg(fig, master=evaluation_page)
canvas_widget = canvas.get_tk_widget()

# Create a custom toolbar similar to plt.show()
class CustomToolbar(NavigationToolbar2Tk):
    def __init__(self, canvas, parent):
        NavigationToolbar2Tk.__init__(self, canvas, parent)
        self._actions['Home'] = self.home_custom

    def home_custom(self, *args):
        # Add custom behavior for the Home button, if needed
        print("Custom Home Button Clicked")

# Add the custom toolbar to the Tkinter window
toolbar = CustomToolbar(canvas, evaluation_page)
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Run the Tkinter event loop
evaluation_page.mainloop()
