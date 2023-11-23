# Import necessary libraries
import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Graph_Learner import doc_graph

# Generate a list of numbers from 0 to 49
mynums = [x for x in range(50)]

# Create an instance of the 'doc_graph' class and add the list of numbers
g = doc_graph(5)
g.add_doc(mynums)

# Function to retrieve numbers from the input and update the result label and graph
def get_numbers():
    # Get the input values from the entry widget
    input_values = entry.get()

    # Convert the input string to a list of numbers
    numbers = [int(num) for num in input_values.split()]

    # Generate the next set of numbers using the 'gen_next' method from 'doc_graph'
    output = g.gen_next(numbers, 5)

    # Update the result label with the generated output
    result_label.config(text=f"Result: {output}")

    # Create or update the line graph based on the input numbers
    create_line_graph(numbers)

# Function to open a file dialog and load the content into the entry widget
def upload_file():
    # Open a file dialog and get the selected file path
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    # If a file is selected, read its content and update the entry widget
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            entry.delete(0, tk.END)
            entry.insert(0, content)

# Function to create or update the line graph based on the input numbers
def create_line_graph(numbers):
    # Clear the previous graph (if any)
    if hasattr(create_line_graph, 'ax'):
        create_line_graph.ax.clear()
    else:
        # Create a new line chart using Matplotlib for the first time
        fig, ax = plt.subplots()
        ax.set_xlabel('Index')
        ax.set_ylabel('Values')
        ax.set_title('Input Numbers')
        create_line_graph.ax = ax

    # Draw the new graph
    create_line_graph.ax.plot(range(len(numbers)), numbers, marker='o')

    # Embed the Matplotlib graph in the Tkinter window
    if hasattr(create_line_graph, 'canvas'):
        create_line_graph.canvas.get_tk_widget().destroy()

    create_line_graph.canvas = FigureCanvasTkAgg(create_line_graph.ax.figure, master=learning_page)
    canvas_widget = create_line_graph.canvas.get_tk_widget()
    canvas_widget.pack()

# Main part of the program

# Create the main Tkinter window
window = tk.Tk()
window.geometry('800x600')
window.title("Graph Creation Phase")

# Create a notebook for navigation between pages
notebook = ttk.Notebook(window)

# Create a page for the Learning Phase
learning_page = tk.Frame(notebook)
notebook.add(learning_page, text="Learning Phase")

# Create a button to upload a file
upload_button = tk.Button(learning_page, text="Upload File", command=upload_file)
upload_button.pack()

# Create a label and an entry widget for input on the graph page
input_label = tk.Label(learning_page, text="Enter numbers (separated by space) or upload a file:")
input_label.pack()

entry = tk.Entry(learning_page)
entry.pack()

# Create a button to trigger the calculation on the graph page
calculate_button = tk.Button(learning_page, text="Show", command=get_numbers)
calculate_button.pack()

# Create a label to display the result on the graph page
result_label = tk.Label(learning_page, text="Result: ")
result_label.pack()

# Create pages for Prediction and Evaluation Phases
predict_page = tk.Frame(notebook)
notebook.add(predict_page, text="Predict Phase")

evaluation_page = tk.Frame(notebook)
notebook.add(evaluation_page, text="Evaluation Phase")

# Pack the notebook to fill the available space in the window
notebook.pack(fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
window.mainloop()