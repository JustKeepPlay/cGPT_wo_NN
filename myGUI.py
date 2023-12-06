import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Graph_Learner import doc_graph
import networkx as nx

doc = doc_graph(5, 'wrand')

# ------------------------------------------------------------------------------------------------------------

def create_learning_page(notebook):
    global learning_page, entry, create_line_graph, result_label
    learning_page = tk.Frame(notebook)
    notebook.add(learning_page, text="Learning Phase")
    # def fibo (n):
    #     if n <=1:
    #         return n
    #     else:
    #         return fibo(n-1)+fibo(n-2)
    # fiboNum = [fibo(i) for i in range(30)]
    # doc.add_doc(fiboNum)    

    upload_button = tk.Button(learning_page, text="Upload File", command=upload_file)
    upload_button.pack()

    input_label = tk.Label(learning_page, text="Enter numbers (separated by space) or upload a file:")
    input_label.pack()

    entry = tk.Entry(learning_page)
    entry.pack()

    calculate_button = tk.Button(learning_page, text="Train", command=get_numbers)
    calculate_button.pack()

    result_label = tk.Label(learning_page, text="Result: ")
    result_label.pack()

    create_line_graph.ax = None
    create_line_graph.canvas = None

def create_line_graph(numbers, ax=None, canvas=None):
    if ax is None:
        fig, ax = plt.subplots()

    ax.clear()  # Clear the previous plot

    ax.plot(range(len(numbers)), numbers, marker='o')

    # Set x-axis locator to integer values
    ax.locator_params(axis='x', integer=True)
    ax.locator_params(axis='y', integer=True)

    # Set or update labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Input Numbers')

    if canvas:
        canvas.get_tk_widget().destroy()

    create_line_graph.ax = ax
    create_line_graph.canvas = FigureCanvasTkAgg(ax.figure, master=learning_page)
    create_line_graph.canvas_widget = create_line_graph.canvas.get_tk_widget()
    create_line_graph.canvas_widget.pack()

def get_numbers():
    input_values = entry.get()
    numbers = [int(num) for num in input_values.split(',')[:-1]]
    train(numbers, 5)
    # output = doc.gen_next(numbers, 5)
    result_label.config(text=f"Result: { numbers }")
    create_line_graph(numbers, ax=create_line_graph.ax, canvas=create_line_graph.canvas)

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            entry.delete(0, tk.END)
            entry.insert(0, content)

def train(seq, h):
    doc.add_doc(seq,h)  


# ------------------------------------------------------------------------------------------------------------

def create_prediction_page(notebook):
    predict_page = tk.Frame(notebook)
    notebook.add(predict_page, text="Predict Phase")
    # Add widgets and functionality for the prediction page as needed  

# ------------------------------------------------------------------------------------------------------------
  

def create_evaluation_page(notebook):
    global evaluation_page
    evaluation_page = tk.Frame(notebook)
    notebook.add(evaluation_page, text="Evaluation Phase")

    # Create a button to trigger the Evaluation on the evaluation page
    evaluation_button = tk.Button(evaluation_page, text="Evaluate", command=create_network)
    evaluation_button.pack()


def create_network():
    G = nx.DiGraph()
    print(doc.get_edge_table())
    G.add_edges_from(doc.get_edge_table())

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

# ------------------------------------------------------------------------------------------------------------


def main():
    window = tk.Tk()
    window.geometry('800x600')
    window.title("Graph Learning GUI ")

    notebook = ttk.Notebook(window)

    create_learning_page(notebook)
    create_prediction_page(notebook)
    create_evaluation_page(notebook)

    notebook.pack(fill=tk.BOTH, expand=True)
    window.mainloop()

if __name__ == "__main__":
    main()
