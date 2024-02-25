# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure

# # Define your sequences
# list_1 = [1, 2, 3, 4, 5]
# list_2 = [1, 2, 3, 2, 1]
# list_3 = [1, 3, 5, 7, 9]

# # Define x-axis values (assuming they are steps)
# steps = range(len(list_1))

# # Create a Tkinter window
# root = tk.Tk()
# root.title("Line Graphs with Tkinter")

# # Create a function to draw a graph for a given sequence
# def draw_graph(sequence, ax):
#     ax.plot(steps, sequence)
#     ax.set_xlabel('Step')
#     ax.set_ylabel('Value')

# # Create a figure and subplots for each sequence
# fig = Figure(figsize=(5, 4), dpi=100)
# ax1 = fig.add_subplot(311)
# ax2 = fig.add_subplot(312)
# ax3 = fig.add_subplot(313)

# # Draw each graph
# draw_graph(list_1, ax1)
# draw_graph(list_2, ax2)
# draw_graph(list_3, ax3)

# # Create canvas to display the plots in Tkinter
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.draw()
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# # Run the Tkinter event loop
# tk.mainloop()

tuple_list = [(1, 2), (2, 3), (3, 4), (2, 3)]
flattened_list = list(set(item for sublist in tuple_list for item in sublist))
print(flattened_list)
