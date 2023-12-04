import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Graph_Learner import doc_graph

def create_line_graph(numbers, ax=None, canvas=None):
    if ax is None:
        fig, ax = plt.subplots()
        ax.set_xlabel('Index')
        ax.set_ylabel('Values')
        ax.set_title('Input Numbers')

    ax.plot(range(len(numbers)), numbers, marker='o')

    if canvas:
        canvas.get_tk_widget().destroy()

    canvas = FigureCanvasTkAgg(ax.figure, master=learning_page)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

def get_numbers():
    input_values = entry.get()
    numbers = [int(num) for num in input_values.split(',')]
    output = doc.gen_next(numbers, 5)
    result_label.config(text=f"Result: {output}")
    create_line_graph(numbers, ax=create_line_graph.ax, canvas=create_line_graph.canvas)

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            entry.delete(0, tk.END)
            entry.insert(0, content)

def create_learning_page(notebook):
    global learning_page, entry, create_line_graph, result_label, doc
    learning_page = tk.Frame(notebook)
    notebook.add(learning_page, text="Learning Phase")
    def fibo (n):
        if n <=1:
            return n
        else:
            return fibo(n-1)+fibo(n-2)
    # fiboNum = [fibo(i) for i in range(30)]
    num = [i for i in range(5)]
    doc = doc_graph(5, 'wrand')
    # doc.add_doc(fiboNum)
    doc.add_doc(num)

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
