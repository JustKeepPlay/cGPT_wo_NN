import tkinter as tk
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Graph_Learner

from Graph_Learner import doc_graph
import sys
import random


mynums = [x for x in range(50)]

g = doc_graph(5)
g.add_doc(mynums)

#out = g.gen_next([4,5,6],5)
#print(out)

#input part============================================
def get_numbers():
    # Get the input values from the entry widgets
    input_values = entry.get()

    # Convert the input string to a list of numbers
    numbers = [int(num) for num in input_values.split()]
    output = g.gen_next(numbers,5)
    result_label.config(text= f"Result: {output}")
    Create_Line_Graph(numbers)




#graph part=============================================
def Create_Line_Graph (numbers):
    # Create a line chart using Matplotlib
    fig, ax = plt.subplots()
    ax.plot(range(len(numbers)), numbers, marker='o')
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Input Numbers')


    # Embed the Matplotlib graph in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()


#graph part=============================================
    

# Create the main tkinter window
window = tk.Tk()
window.geometry('800x600')
window.title("Graph Creation Phase")

# Create a label and entry widget for input
input_label = tk.Label(window, text="Enter numbers (separated by space):")
input_label.pack()

entry = tk.Entry(window)
entry.pack()

# Create a button to trigger the calculation
calculate_button = tk.Button(window, text="Show", command=get_numbers)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Start the tkinter event loop
window.mainloop()

