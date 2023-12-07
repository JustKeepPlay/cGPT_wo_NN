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

    upload_button = tk.Button(learning_page, text="Upload File", command=upload_file)
    upload_button.pack()

    input_label = tk.Label(learning_page, text="Enter numbers (separated by space) or upload a file:")
    input_label.pack()

    entry = tk.Entry(learning_page)
    # entry.insert(0, "1,2,3")
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
    numbers = [int(num) for num in input_values.split(',')]
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
    global predict_page , pred_button , create_pred_graph, Pentry
    predict_page = tk.Frame(notebook)
    notebook.add(predict_page, text="Predict Phase")

    pred_input_label = tk.Label(predict_page, text="Enter the sequence:")
    pred_input_label.pack()

    Pentry = tk.Entry(predict_page)
    Pentry.pack()

    pred_button = tk.Button(predict_page, text="Predict", command=get_pred_num)
    pred_button.pack()

    create_pred_graph.ax = None
    create_pred_graph.canvas = None

def get_pred_num():
    pred_input = Pentry.get()
    nums = [int(num) for num in pred_input.split(',')]
    #print(nums)
    #output = doc.gen_next(numbers, 5)
    pred_num = []
    pred_num = doc.gen_next(doc.gen_next(nums.copy(),5))

    create_pred_graph(nums.copy(), pred_num , ax=create_pred_graph.ax, canvas=create_pred_graph.canvas)
    

def create_pred_graph(numbers, Pred_num, ax=None, canvas=None):
    if ax is None:
        fig, ax = plt.subplots()
    
    ax.clear()  # Clear the previous plot
     # Plot the input numbers in blue
    print('number :',numbers)
    print('Pred :',Pred_num)

    ax.plot(range(len(numbers)+2), Pred_num, linestyle=':', color='red')

    ax.plot(range(len(numbers)), numbers, marker='o', color='blue', label='Input Numbers')
    
    # Plot only the last element of the predicted number in red
    ax.plot(len(numbers)+1 , Pred_num[-1], marker='o', color='red', label='1st Predicted Number')

    ax.plot(len(numbers) , Pred_num[-2], marker='o', color='red', label='2nd Predicted Number')
    

    for x, y in zip(range(len(numbers)),numbers):
        plt.text(x, y, f'{y}', ha='right', va='bottom',c='blue')
    
    plt.text(len(numbers)+1, Pred_num[-1], f'{Pred_num[-1]}', ha='left', va='bottom', c='red')
    plt.text(len(numbers), Pred_num[-2], f'{Pred_num[-2]}', ha='left', va='bottom', c='red')



    # Set x-axis locator to integer values
    ax.locator_params(axis='y', integer=True)
    ax.locator_params(axis='x', integer=True)

    # Set or update labels and title
    ax.set_xlabel('Step')
    ax.set_ylabel('Value')
    ax.set_title('Prediction Graph')
    
    # Show legend
    ax.legend()

    if canvas:
        canvas.get_tk_widget().destroy()

    create_pred_graph.ax = ax
    create_pred_graph.canvas = FigureCanvasTkAgg(ax.figure, master=predict_page)
    create_pred_graph.canvas_widget = create_pred_graph.canvas.get_tk_widget()
    create_pred_graph.canvas_widget.pack()


# ------------------------------------------------------------------------------------------------------------
  

def create_evaluation_page(notebook):
    global evaluation_page, eva_node_entry, eva_friends_entry
    evaluation_page = tk.Frame(notebook)
    notebook.add(evaluation_page, text="Evaluation Phase")

    eva_node_label = tk.Label(evaluation_page, text="Node: ")
    eva_node_label.pack()
    eva_node_entry = tk.Entry(evaluation_page)
    eva_node_entry.pack()
    # eva_friends_label = tk.Label(evaluation_page, text="Neighbour: ")
    # eva_friends_label.pack()
    # eva_friends_entry = tk.Entry(evaluation_page)
    # eva_friends_entry.pack()

    # Create a button to trigger the Evaluation on the evaluation page
    evaluation_button = tk.Button(evaluation_page, text="Evaluate", command=create_network)
    evaluation_button.pack()

    # Initialize canvas variable
    create_evaluation_page.canvas = None
    create_evaluation_page.toolbar = None

# def get_node_edges(graph, node):
#     if graph.has_node(node):
#         edges = list(graph.edges(node))
#         return edges
#     else:
#         return None


def create_network():
    specified_node = eva_node_entry.get()
    G = nx.DiGraph()
    G.add_edges_from(doc.get_edge_table())

    # Create a new Matplotlib figure for the network graph
    fig, ax = plt.subplots()
    ax.set_title('Network Graph')

    # Clear the previous network graph (if any)
    if create_evaluation_page.canvas:
        create_evaluation_page.canvas.get_tk_widget().destroy()
    if create_evaluation_page.toolbar:
        create_evaluation_page.toolbar.destroy()


    try:
        if len(eva_node_entry.get()) == 0:
            pos = nx.kamada_kawai_layout(G)
            # Draw the network graph
            nx.draw(
                G,
                pos,
                with_labels=True,
                node_color='lightgreen'
            )
        else:
            specified_node = int(specified_node)
            if G.has_node(specified_node):
                pos = nx.spring_layout(G)
                # node_edges = get_node_edges(G, specified_node)
                # print(f"Edges connected to Node {specified_node}: {node_edges}")

                # # Create a subgraph with the specified edges
                # subgraph_edges = [(specified_node, neighbor) for neighbor in G.neighbors(specified_node)]
                # subgraph = G.subgraph(subgraph_edges)
                subgraph = nx.ego_graph(G, specified_node)

                # Draw the network graph
                nx.draw(
                    subgraph,
                    pos,
                    with_labels=True,
                    node_color='lightgreen'
                )
            else:
                ax.set_title('No node specified.')
            
    except:
        print("An exception error")

    # Embed the Matplotlib network graph in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=evaluation_page)
    create_evaluation_page.canvas = canvas  # Store canvas for future destruction
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Add the Matplotlib NavigationToolbar2Tk
    toolbar = NavigationToolbar2Tk(canvas, evaluation_page)
    create_evaluation_page.toolbar = toolbar  # Store toolbar for future destruction
    toolbar.update()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    

# ------------------------------------------------------------------------------------------------------------


def main():
    window = tk.Tk()
    window.geometry('800x700')
    window.title("Graph Learning GUI ")

    notebook = ttk.Notebook(window)

    create_learning_page(notebook)
    create_prediction_page(notebook)
    create_evaluation_page(notebook)

    notebook.pack(fill=tk.BOTH, expand=True)
    window.mainloop()

if __name__ == "__main__":
    main()