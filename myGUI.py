import tkinter as tk
import customtkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Graph_Learner import doc_graph
import networkx as nx
import ast
import os
import random

doc = doc_graph(5, 'wrand')

# ------------------------------------------------------------------------------------------------------------

# def create_learning_page(notebook):
#     global learning_page, entry, create_line_graph, result_label
#     learning_page = tk.Frame(notebook)
#     notebook.add(learning_page, text="Learning Phase")    

#     upload_button = tk.Button(learning_page, text="Upload File", command=upload_file)
#     upload_button.pack()

#     input_label = tk.Label(learning_page, text="Enter numbers (separated by comma) or upload a file:")
#     input_label.pack()

#     entry = tk.Entry(learning_page)
#     # entry.insert(0, "1,2,3")
#     entry.pack()

#     calculate_button = tk.Button(learning_page, text="Train", command=get_numbers)
#     calculate_button.pack()

#     result_label = tk.Label(learning_page, text="Result: ")
#     result_label.pack()

#     create_line_graph.ax = None
#     create_line_graph.canvas = None

# def create_line_graph(numbers, ax=None, canvas=None):
#     if ax is None:
#         fig, ax = plt.subplots()

#     ax.clear()  # Clear the previous plot

#     ax.plot(range(len(numbers)), numbers, marker='o')

#     # Set x-axis locator to integer values
#     ax.locator_params(axis='x', integer=True)
#     ax.locator_params(axis='y', integer=True)

#     # Set or update labels and title
#     ax.set_xlabel('Index')
#     ax.set_ylabel('Values')
#     ax.set_title('Input Numbers')

#     if canvas:
#         canvas.get_tk_widget().destroy()

#     create_line_graph.ax = ax
#     create_line_graph.canvas = FigureCanvasTkAgg(ax.figure, master=learning_page)
#     create_line_graph.canvas_widget = create_line_graph.canvas.get_tk_widget()
#     create_line_graph.canvas_widget.pack()

# def get_numbers():
#     input_values = entry.get()
#     numbers = [int(num) for num in input_values.split(',')]
#     train(numbers, 5)
#     # output = doc.gen_next(numbers, 5)
#     result_label.config(text=f"Result: { numbers }")
#     create_line_graph(numbers, ax=create_line_graph.ax, canvas=create_line_graph.canvas)

# def upload_file():
#     file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
#     if file_path:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             entry.delete(0, tk.END)
#             entry.insert(0, content)

# def train(seq, h):
#     doc.add_doc(seq,h)  


# ------------------------------------------------------------------------------------------------------------

def create_prediction_page(notebook):
    global predict_page , pred_button , create_pred_graph, Pentry, Eentry
    predict_page = tk.Frame(notebook)
    notebook.add(predict_page, text="Predict Phase")

    pred_input_label = tk.Label(predict_page, text="Enter the sequence:")
    pred_input_label.pack()

    Pentry = tk.Entry(predict_page)
    Pentry.pack()

    element_label = tk.Label(predict_page, text="How many to predict:")
    element_label.pack()

    Eentry = tk.Entry(predict_page, width=10)
    Eentry.pack()

    pred_button = tk.Button(predict_page, text="Predict", command=get_pred_num)
    pred_button.pack()

    create_pred_graph.ax = None
    create_pred_graph.canvas = None

def get_pred_num():
    pred_input = Pentry.get()
    element = Eentry.get()
    nums = [int(num) for num in pred_input.split(',')]
    num = nums.copy()
    ele = int(element)
    
    pred_num = []

    for i in range(ele):
        pred_num = doc.gen_next(nums,5)

    print(pred_num)

    create_pred_graph(num, pred_num ,ele, ax=create_pred_graph.ax, canvas=create_pred_graph.canvas)
    

def create_pred_graph(numbers, Pred_num, ele, ax, canvas):
    exd_num = Pred_num[len(Pred_num)-ele:]
    print('number :',numbers)
    print('Pred :',Pred_num)
    print('extended :',exd_num)

    # if ax is None:
    fig, ax = plt.subplots()
    
    ax.clear()  # Clear the previous plot

     # Plot the input numbers in blue
    ax.plot(range(len(Pred_num)), Pred_num, linestyle=':', color='red')

    ax.plot(range(len(numbers)), numbers, marker='o', color='blue')
    
    # Plot only the last element of the predicted number in red
    
    for i in range(ele):
        ax.plot(len(numbers)+i , exd_num[i], marker='o', color='red')
        plt.text(len(numbers)+i, exd_num[i], f'{exd_num[i]}', ha='right', va='bottom', c='red')
        print('x=',len(numbers)+i,' y=',exd_num[i])

    for x, y in zip(range(len(numbers)),numbers):
        plt.text(x, y, f'{y}', ha='right', va='bottom',c='blue')  

    # Set x-axis locator to integer values
    ax.locator_params(axis='y', integer=True)
    ax.locator_params(axis='x', integer=True)

    # Set or update labels and title
    ax.set_xlabel('Step')
    ax.set_ylabel('Value')
    ax.set_title('Prediction Graph')
    
    # Show legend
    #ax.legend()

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
    print(doc.get_edge_table())

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
class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master, fg_color="yellow")

        self.title = customtkinter.CTkLabel(self, text=title, fg_color="grey30", corner_radius=20)
        self.title.grid(row=0, column=0)

class NumberSequenceFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="grey30")
        # self.variable = customtkinter.StringVar()
        self.seq_list = []
        self.checklists = []

        self.grid_columnconfigure(0, weight=1)

    def add_num_seq(self, seq):

        self.seq_list.append(seq)
        length = len(self.seq_list) - 1

        # for i, seq_num in enumerate(self.seq_list):
        #     seq_scroll = customtkinter.CTkScrollableFrame(self, orientation="horizontal", height=50)
        #     seq_scroll.grid(row=i, column=0, pady=(0, 5), sticky="we")
        #     checkbox = customtkinter.CTkCheckBox(seq_scroll, text=str(tuple(seq_num)), font=("Ariel", 40))
        #     checkbox.grid(row=i, column=0, pady=(0, 5), sticky="we")
        #     self.checklists.append(checkbox)

        seq_scroll = customtkinter.CTkScrollableFrame(self, orientation="horizontal", height=25)
        seq_scroll.grid(row=length, column=0, pady=(0, 5), sticky="we")
        checkbox = customtkinter.CTkCheckBox(seq_scroll, text=str(tuple(seq)), font=("Ariel", 20))
        checkbox.grid(row=length, column=0, pady=(0, 5), sticky="we")
        self.checklists.append(checkbox)

    def get_checklist(self):
        checked_checklists = []
        for checklist in self.checklists:
            if checklist.get() == 1:
                print(checklist.cget("text"), " Type: ", type(checklist.cget("text")))
                try:
                    checked_checklists.append(ast.literal_eval(checklist.cget("text")))
                except:
                    print("error")
        return checked_checklists
            
    

class MyTabView(customtkinter.CTkTabview):

    def __init__(self, master):
        super().__init__(master)
        self.tab1 = self.add("Learning Tab")
        self.tab2 = self.add("Prediction Tab")
        self.tab3 = self.add("Evaluation Tab")

        self.seq_list = []

        self.create_learning_tab()
        self.create_prediction_tab()
        self.create_evaluation_tab()

    def generate_sequence(self):
        # Generate a random number between 1 and 20 for the length of the sequence
        sequence_length = random.randint(1, 20)

        # Generate a sequence of positive integers
        sequence = [str(random.randint(1, 100)) for _ in range(sequence_length)]

        # Join the sequence with commas and add '#' at the end
        sequence_str = ",".join(sequence) + "#"

        return sequence_str
    
    def make_seq_file(self):
        # Create "train_data" directory if it doesn't exist
        train_data_dir = "train_data"
        os.makedirs(train_data_dir, exist_ok=True)

        # Save all 10 sequences in a single text file inside "train_data" directory
        file_name = os.path.join(train_data_dir, "sequences.txt")
        
        with open(file_name, 'w') as file:
            for i in range(10):
                sequence = self.generate_sequence()
                file.write(sequence + "\n")

        print(f"All sequences saved in {file_name}")


    def create_learning_tab(self):
        # self.learning_frame = MyFrame(self.tab1, "Learning Phase")
        # self.learning_frame.grid(row=0, column=0)
            
        upload_btn = customtkinter.CTkButton(self.tab1, text="Upload File", command=self.upload_file)
        upload_btn.grid(row=1, column=0, pady=(0, 10), sticky="w")

        self.seq_entry = customtkinter.CTkEntry(self.tab1)
        self.seq_entry.grid(row=0, column=0, padx=0, pady=(0, 10), ipadx=100)

        train_btn = customtkinter.CTkButton(self.tab1, text="Add Sequence", command=self.get_numbers)
        train_btn.grid(row=0, column=1, padx=(10, 0), pady=(0, 10), sticky="w")

        clear_entry_btn = customtkinter.CTkButton(self.tab1, text="Clear Input", command=self.clear_entry)
        clear_entry_btn.grid(row=1, column=1, padx=(10, 0), pady=(0, 10), sticky="w")

        self.number_seq_frame = NumberSequenceFrame(self.tab1)
        self.number_seq_frame.grid(row=2, column=0, pady=(0, 10), sticky="nsew", columnspan=2)
        self.tab1.grid_rowconfigure(2, weight=1) # Expand an entire of row 3 to fit the window

        self.create_network = customtkinter.CTkButton(self.tab1, text="Create Network", command=self.draw_graph)
        self.create_network.grid(row=0, column=2, padx=(10, 0), sticky="nw")

        # self.text_box = customtkinter.CTkTextbox(self.tab1, fg_color="white", font=("Ariel", 40), text_color="Black")
        # self.text_box.grid(row=1, column=2, padx=(10, 0), pady=(0, 10), sticky="nsew", rowspan=3)
        
        # self.draw_graph()

    def clear_entry(self):
        self.seq_entry.delete(0, tk.END)

    def draw_graph(self):
        # Create a graph
        G = nx.DiGraph()

        # Connect nodes in each sequence
        for seq in self.number_seq_frame.get_checklist():
            if len(seq) > 1:
                G.add_edges_from(zip(seq, seq[1:]))
            else:
                G.add_node(seq[0])  # Add a single node if the sequence has only one element

        # Draw the graph
        pos = nx.kamada_kawai_layout(G)
        
        fig, ax = plt.subplots(figsize=(6, 4))
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue",
                font_color="black", font_size=10, edge_color="gray", linewidths=1, alpha=0.7, ax=ax)

        # Draw the graph in a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.tab1)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=2, padx=(10, 0), pady=(0, 10), sticky="nsew", rowspan=3)
        self.tab1.grid_columnconfigure(2, weight=1) # Expand an entire of column 2 to fit the window



    def get_numbers(self):
        input_values = self.seq_entry.get()
        numbers = [int(num) for num in input_values.split(',')]
        self.seq_list.append(numbers)
        self.number_seq_frame.add_num_seq(numbers)
        # self.number_seq_frame = NumberSequenceFrame(self.tab1, self.seq_list)
        # self.number_seq_frame.grid(row=2, column=0, pady=(0, 10), sticky="nsew", columnspan=2)

        # self.display_number_network()  
        # self.train_data(numbers, 5)


    # def upload_file(self):
    #     file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    #     if file_path:
    #         with open(file_path, 'r') as file:
    #             content = file.read()
    #             self.seq_entry.delete(0, tk.END)
    #             self.seq_entry.insert(0, content)
    #             self.seq_entry.delete(0, tk.END)
        
    def get_numbers_from_upload(self, content_before_hash):
        numbers = [int(num) for num in content_before_hash.split(',')]
        self.seq_list.append(numbers)
        self.number_seq_frame.add_num_seq(numbers)
        
    def upload_file(self):
        self.make_seq_file()
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                for line in file:
                    # Check if the line contains '#' character
                    if '#' in line:
                        # Extract content before '#'
                        content_before_hash = line.split('#')[0].strip()
                        # Perform the get_number() module here
                        self.get_numbers_from_upload(content_before_hash)  # Assuming get_numbers() is a method in your class
                    else:
                        self.get_numbers_from_upload(content_before_hash)
                        


    def train_data(self, seq, h):
        doc.add_doc(seq, h)

# ---------------------

    def create_prediction_tab(self):
        # self.prediction_frame = MyFrame(self.tab2, "Prediction Phase")
        # self.prediction_frame.grid(row=0, column=0, padx=0, pady=0)
        ...

    def create_evaluation_tab(self):
        # self.evaluation_frame = MyFrame(self.tab3, "Evaluation Phase")
        # self.evaluation_frame.grid(row=0, column=0, padx=0, pady=0)
        ...

    
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Graph Learner GUI")
        self.geometry("1920x1080")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        customtkinter.set_appearance_mode("dark")

        self.tab_view = MyTabView(self)
        self.tab_view.grid(row=0, column=0, ipadx=1920, ipady=1080, padx=20, pady=(5, 20))


def main():
    # window = tk.Tk()
    # window.geometry('800x700')
    # window.title("Graph Learning GUI ")

    # notebook = ttk.Notebook(window)

    # create_learning_page(notebook)
    # create_prediction_page(notebook)
    # create_evaluation_page(notebook)

    # notebook.pack(fill=tk.BOTH, expand=True)
    # window.mainloop()

    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()