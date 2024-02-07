import tkinter as tk
from CTkMessagebox import CTkMessagebox
import customtkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Graph_Learner import doc_graph
import networkx as nx
import ast, os, random
import math

doc = doc_graph(5, 'rand')

class NumberSequenceFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="grey30")
        self.seq_list = []
        self.count_labels = []
        self.seq_history = []
        self.checklists = []
        self.checked_checklists = []
        # self.seq_scroll_list = []

        self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)

    def select_all(self):
        # Check if all checklists are currently selected
        all_selected = all(checklist.get() for checklist in self.checklists)

        # If all are selected, deselect all; otherwise, select all
        for checklist in self.checklists:
            if all_selected:
                checklist.deselect()
            else:
                checklist.select()

    # def remove_seq(self):
    #     try:
    #         checked_sequences = self.get_checklist()
    #         for seq in checked_sequences:
    #             if seq in 

    #     except Exception as e:
    #         print(e)

    def add_num_seq(self, seq, history=5, amount=1):
        if seq in self.seq_list:
            # If sequence already exists, find the index and update count_label
            index = self.seq_list.index(seq)
            count_label = self.count_labels[index]
            # count = int(count_label.cget("text"))
            count = int(count_label.get("0.0", "end"))
            count += 1
            # count_label.configure(text=str(count))
            count_label.delete("0.0", "end")
            count_label.insert("0.0", str(count))
        else:
            # If sequence doesn't exist, create a new entry
            self.seq_list.append(seq)
            length = len(self.seq_list) - 1

            self.grid_columnconfigure(0, weight=2)
            self.grid_columnconfigure((1,2), weight=1)

            seq_scroll = customtkinter.CTkScrollableFrame(self, orientation="horizontal", height=25)
            seq_scroll.grid(row=length, column=0, padx=(0, 5), pady=(0, 5), sticky="nsew")

            checkbox = customtkinter.CTkCheckBox(seq_scroll, text=str(tuple(seq)), font=("Ariel", 20))
            checkbox.select()
            checkbox.grid(row=0, column=0, sticky="ew")
            self.checklists.append(checkbox)

            history_field = customtkinter.CTkTextbox(self, width=110, height=10, font=("Ariel", 30), activate_scrollbars=False)
            history_field.grid(row=length, column=1, padx=(0, 5), pady=(0, 5), sticky="nsew")
            history_field.insert("0.0", str(history))
            self.seq_history.append(history_field)

            count_label = customtkinter.CTkTextbox(self, width=110, height=10, font=("Ariel", 30), activate_scrollbars=False)
            count_label.grid(row=length, column=2, padx=(0, 5), pady=(0, 5), sticky="nsew")
            count_label.insert("0.0", str(amount))
            self.count_labels.append(count_label)  # Added count_label to count_labels list

    def get_checklist(self):
        self.checked_checklists.clear()

        for checklist in self.checklists:
            if checklist.get() == 1:
                # print(checklist.cget("text"), " Type: ", type(checklist.cget("text")))
                try:
                    self.checked_checklists.append(ast.literal_eval(checklist.cget("text")))
                except:
                    print("error")
        return self.checked_checklists
        
    
class PredictSequenceFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="grey30")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        self.saved_seq_generated_list = []
    
    def add_generated_seq(self, seq):
        self.saved_seq_generated_list.append(seq)
        length = len(self.saved_seq_generated_list) - 1

        seq_no = customtkinter.CTkLabel(self, text=str(length+1), font=("Ariel", 30))
        seq_no.grid(row=length, column=0, sticky="we")
        seq_list = customtkinter.CTkScrollableFrame(self, orientation="horizontal", height=25)
        seq_list.grid(row=length, column=1, pady=(0, 5), sticky="we")
        seq_num = customtkinter.CTkLabel(seq_list, text=self.saved_seq_generated_list[-1], font=("Ariel", 20))
        seq_num.grid(row=0, column=0, sticky="we")

class FactorSequenceFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="lightgreen")


class MainSequenceFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="lightyellow")

class NetworkFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="yellow")
        
    def draw_network(self):
        # Create a graph
        G = nx.DiGraph()
        edge_weights = doc.edges_amount
        edge = dict(sorted(edge_weights.items(), key=lambda item: item[1]))
        try:
            if tab_view.get_sort_state():
                print("Desc")
                edges = [_ for _ in list(edge.keys())[-10:]]
            else:
                print("Asec")
                edges = [_ for _ in list(edge.keys())[:10]]
        except Exception as e:
            print(e)

        G.add_edges_from(edges)
        # Draw the graph
        pos = nx.kamada_kawai_layout(G)

        # Destroy the existing canvas if it exists
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()
        
        fig, ax = plt.subplots(figsize=(6, 4))
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue",
                font_color="black", font_size=10, edge_color="gray", linewidths=1, alpha=1, ax=ax)

        # Draw the graph in a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class BarChartFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="lightblue")

    def draw_Bar_Chart(self):
        edge_weights = doc.edges_amount
        edge = dict(sorted(edge_weights.items(), key=lambda item: item[1]))

        try:
            if tab_view.get_sort_state():
                edges = [str(_) for _ in list(edge.keys())[-10:]]
                values = list(edge.values())[-10:]
            else:
                edges = [str(_) for _ in list(edge.keys())[:10]]
                values = list(edge.values())[:10]
        except Exception as e:
            print(e)

        # Destroy the existing canvas if it exists
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()
        
        fig = Figure(figsize=(7, 5), dpi=100)
        ax = fig.add_subplot(111)

        ax.clear()

        try:
            ax.barh(edges, values)
        except Exception as e:
            print(e)

        # Adding labels and title
        ax.set_xlabel('Values')
        ax.set_ylabel('Edges')
        ax.set_title('Horizontal Bar Chart')


        # Draw the graph in a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class F1Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="lightgreen")
        self.grid_columnconfigure(0, weight=1)
        customtkinter.CTkLabel(self, text="F1", text_color="black").grid(row=0, column=0)

class ErrorRateFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="orange")
        self.grid_columnconfigure(0, weight=1)
        customtkinter.CTkLabel(self, text="Error Rate Frame", text_color="black").grid(row=0, column=0)
        

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

        doc.add_doc([1,2,3,4,5,6,7,8,9], 5)
        doc.add_doc([9,8,7,6,5,4,3,2,1], 6)
        doc.add_doc([1,3,5,7,9,11,13,15], 3)
        # doc.add_doc([1,3], 5)
        self.set("Prediction Tab")

        self.sort_desc = True

    def create_learning_tab(self):
        upload_btn = customtkinter.CTkButton(self.tab1, text="Upload File", command=self.upload_file)
        upload_btn.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.seq_entry = customtkinter.CTkEntry(self.tab1)
        self.seq_entry.grid(row=1, column=0, padx=(0, 10), pady=(0, 10), ipadx=100)
        self.seq_entry.insert(0, "1,2,3,4,5")
        self.seq_entry.bind("<Return>", self.add_seq_enter)

        add_seq_btn = customtkinter.CTkButton(self.tab1, text="Add", width=30, command=self.get_seq)
        add_seq_btn.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        clear_entry_btn = customtkinter.CTkButton(self.tab1, text="Clear", width=30, command=self.clear_entry)
        clear_entry_btn.grid(row=1, column=2, pady=(0, 10), sticky="w")

        remove_seq_btn = customtkinter.CTkButton(self.tab1, text="Remove Sequence", fg_color="red", hover_color="darkred", command=self.remove_sequence)
        remove_seq_btn.grid(row=5, column=0, padx=(0, 10), pady=(0, 10), sticky="w")

        save_seq_btn = customtkinter.CTkButton(self.tab1, text="Save Sequence", fg_color="green", hover_color="darkgreen", command=self.save_sequence)
        save_seq_btn.grid(row=2, column=0, padx=(0, 10), pady=(0, 10), sticky="w")

        # self.train_btn = customtkinter.CTkButton(self.tab1, text="Train Data from checklist", command=self.train_data)
        # self.train_btn.grid(row=5, column=2, pady=(0, 10), sticky="e")

        self.number_seq_frame = NumberSequenceFrame(self.tab1)
        self.number_seq_frame.grid(row=4, column=0, pady=(0, 10), sticky="nsew", columnspan=3)
        self.tab1.grid_rowconfigure(4, weight=1) # Expand an entire of row 3 to fit the window

        select_all_cb = customtkinter.CTkCheckBox(self.tab1, text="Select All", font=("Ariel", 20), command=self.number_seq_frame.select_all)
        select_all_cb.select()
        select_all_cb.grid(row=3, column=0, padx=(0, 10), pady=(0, 10), sticky="w")

        self.create_network = customtkinter.CTkButton(self.tab1, text="Create Network", command=self.train_data)
        self.create_network.grid(row=3, column=2, padx=(0, 10), pady=(0, 10))

    def remove_sequence(self):
        print("Remove Sequence Button clicked!")


    def save_sequence(self):
        print("Save Sequence Button clicked!")
            

    def add_seq_enter(self, event):
        self.get_seq()

    def generate_sequence(self):
        # Generate a random number between 1 and 20 for the length of the sequence
        sequence_length = random.randint(1, 100)

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
        
        amount_of_seq = 25
        with open(file_name, 'w') as file:
            for i in range(amount_of_seq):
                sequence = self.generate_sequence()
                file.write(sequence + "\n")

        print(f"All sequences saved in {file_name}")

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
        canvas.get_tk_widget().grid(row=0, column=3, padx=(10, 0), pady=(0, 10), sticky="nsew", rowspan=5)
        self.tab1.grid_columnconfigure(3, weight=1) # Expand an entire of column 2 to fit the window


    def process_sequences(self, sequences):
            result = []

            for sequence in sequences:
                current_sequence = []
                i = 0

                while i < len(sequence):
                    item = sequence[i]
                    if item.isdigit():
                        current_sequence.append(int(item))
                    elif item == '*':
                        # Multiply the current sequence
                        result.append(current_sequence * int(sequence[i + 1]))
                        # Skip the next item (the multiplier)
                        i += 1
                        # Reset the current sequence
                        current_sequence = []
                    elif item == '#':
                        # End the sequence
                        if current_sequence:
                            result.append(current_sequence)
                            current_sequence = []
                    i += 1

            return result


        # Example usage with multiple sequences

    def process_txt_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    elements = []
                    current_element = ""
                    for char in line:
                        if char in (',', '#', '*'):
                            if current_element:
                                elements.append(current_element)
                            if char != ',':
                                elements.append(char)
                            current_element = ""
                        else:
                            current_element += char
                    if current_element:
                        elements.append(current_element)
                    
                    self.get_seq_from_upload(current_element)

    def show_error(self):
        # Show some error message
        CTkMessagebox(title="Error", message="Non-numerical Sequence not allowed.", icon="cancel")

    def isNumber(self, input_values):
        return all(item.strip().replace('.', '').isdigit() for item in input_values.split(','))


    def get_seq(self):
        input_values = self.seq_entry.get()
        if self.isNumber(input_values):
            try:
                seq = [int(num) for num in input_values.split(',')]
                self.seq_list.append(seq)
                self.number_seq_frame.add_num_seq(seq, 5, 1)
            except Exception as e:
                print(f"Get Sequence error: {e}")
        else:
            self.show_error()
            
    def get_seq_from_upload(self, content_before_hash):
        if self.isNumber(content_before_hash):
            try:
                seq = [int(num) for num in content_before_hash.split(',')]
                self.seq_list.append(seq)
                history = random.randint(1, 100)
                amount = random.randint(1, 5)
                self.number_seq_frame.add_num_seq(seq, history=history, amount=amount)
            except Exception as e:
                print(e)
        else:
            self.show_error()

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
                        self.get_seq_from_upload(content_before_hash)  # Assuming get_numbers() is a method in your class
                    else:
                        self.get_seq_from_upload(content_before_hash)

    def train_data(self):
        self.create_network.configure(state="disabled")
        try:
            checked_sequences = self.number_seq_frame.get_checklist()
            for seq in checked_sequences:
                index = self.number_seq_frame.seq_list.index(list(seq))
                count = int(self.number_seq_frame.count_labels[index].get("0.0", "end"))
                history = int(self.number_seq_frame.seq_history[index].get("0.0", "end"))

                print(f"{seq}: {history}")
                for _ in range(count):
                    doc.add_doc(list(seq), history)
            self.draw_graph()
            self.show_checkmark()
            self.create_network.configure(state="normal")
        except Exception as e:
            print(e)

    def show_checkmark(self):
        # Show some positive message with the checkmark icon
        CTkMessagebox(header=True, title="Success", message="Sequence successfully trained.",
                  icon="check", option_1="OK")

# ---------------------
        
        
    def create_prediction_tab(self):
        self.switch_var = customtkinter.StringVar(value="off")

        self.tab2.grid_rowconfigure(1, weight=2)
        # self.tab2.grid_rowconfigure((2,3), weight=1)
        self.tab2.grid_columnconfigure(7, weight=1)

        number_label = customtkinter.CTkLabel(self.tab2, text="Sequence: ")
        number_label.grid(row=0, column=0, padx=(0, 10))
        self.number_field = customtkinter.CTkEntry(self.tab2)
        self.number_field.grid(row=0, column=1, padx=(0, 10), ipadx=20)
        self.number_field.insert(0, "1,2,3,4,5")
        self.number_field.bind("<Return>", self.gen_seq_enter)

        history_label = customtkinter.CTkLabel(self.tab2, text="History: ")
        history_label.grid(row=0, column=2, padx=(0, 10))
        self.history_field = customtkinter.CTkEntry(self.tab2)
        self.history_field.grid(row=0, column=3, padx=(0, 10), ipadx=20)
        self.history_field.insert(0, "4")
        self.history_field.bind("<Return>", self.gen_seq_enter)

        gen_label = customtkinter.CTkLabel(self.tab2, text="Generation Amount: ")
        gen_label.grid(row=0, column=4, padx=(0, 10))
        self.gen_field = customtkinter.CTkEntry(self.tab2)
        self.gen_field.grid(row=0, column=5, padx=(0, 10), ipadx=20)
        self.gen_field.insert(0, "3")
        self.gen_field.bind("<Return>", self.gen_seq_enter)

        gen_btn = customtkinter.CTkButton(self.tab2, text="Generate", command=self.choose_event)
        gen_btn.grid(row=0, column=6, padx=(0, 10))

        self.switch = customtkinter.CTkSwitch(self.tab2, text="Switch Graph/Network", command=self.choose_event,
                                        variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.grid(row=0, column=7, sticky="e")

        self.pred_seq_frame = PredictSequenceFrame(self.tab2)
        self.pred_seq_frame.grid(row=1, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew", columnspan=4)

        # factor_seq_frame = FactorSequenceFrame(self.tab2)
        # factor_seq_frame.grid(row=1, column=0, pady=(10, 0), sticky="nsew", columnspan=8)

        # main_seq_frame = MainSequenceFrame(self.tab2)
        # main_seq_frame.grid(row=3, column=0, pady=(10, 0), sticky="nsew", columnspan=8)

    def gen_seq_enter(self, event):
        try:
            self.choose_event()
        except Exception as e:
            print(e)

    # def get_pred_num(self):
    #     try:
    #         history = int(self.history_field.get())
    #         number = [int(num) for num in self.number_field.get().split(',')]
    #         generate = int(self.gen_field.get())

    #         gen_num = doc.gen_next_n(number.copy(), generate, history)

    #         try:
    #             self.pred_seq_frame.saved_seq_generated_list.clear()
    #             # for key, value in doc.edges_amount.items():
    #             #     self.pred_seq_frame.add_generated_seq(f"{key}: {value}")
    #             for key, value in doc.edge_table.items():
    #                 self.pred_seq_frame.add_generated_seq(f"{key}: {value}")
    #         except Exception as e:
    #             print("Seq list problem")


    #         fig = Figure(figsize=(5,4), dpi=100)
    #         ax = fig.add_subplot(111)

    #         ax.clear()

    #         # To plot Y-Axis
    #         num_y = []
    #         gen_y = []

    #         try:
    #             # Seperate input and generated as num_y and gen_y
    #             for item in gen_num:
    #                 if item in number:
    #                     num_y.append(item)
    #                 else:
    #                     gen_y.append(item)
    #         except Exception as e:
    #             print(f"num_y, gen_y (Error): {e}")
            
    #         # To plot X-Axis
    #         num_x = [item for item in range(1, len(num_y) + 1)] # [1, 2, 3, ..., N + 1] ; N = length of the input and + 1 because it start with 1
    #         gen_x = [item for item in range(len(gen_num) - len(gen_y) + 1, len(gen_num) + 1)] # [N + 1, ..., M + 1]
            

    #         print(f"step_x: {num_x}, num_y: {num_y}")
    #         print(f"gen_step_x: {gen_x}, gen_y: {gen_y}")

    #         ax.plot(num_x, num_y, 'b') # Blue line
    #         ax.plot(gen_x, gen_y, 'r') # Red line

    #         ax.plot([num_x[-1], gen_x[0]], [num_y[-1], gen_y[0]], 'r') # Connect input sequence and generated sequence together with red line

    #         ax.plot(num_x, num_y, 'bo')
    #         ax.plot(gen_x, gen_y, 'ro')

    #         ax.set_title("Graph_Learner")
    #         ax.set_ylabel("Number")
    #         ax.set_xlabel("Step")

    #         canvas = FigureCanvasTkAgg(fig, master=self.tab2)
    #         canvas.draw()
    #         canvas.get_tk_widget().grid(row=1, column=4, pady=(10, 0), sticky="nsew", columnspan=4)
            
    #     except Exception as e:
    #         print(e)
            
    def get_pred_num(self):
        try:
            self.temp_gen_seq = []
            history = int(self.history_field.get())
            self.number = [int(num) for num in self.number_field.get().split(',')]
            generate = int(self.gen_field.get())
            
            for i in range(10):
                gen_num = doc.gen_next_n(self.number.copy(), generate, history)
                self.temp_gen_seq.append(gen_num)
            self.temp_gen_seq = set(map(tuple,self.temp_gen_seq))
            self.temp_gen_seq = list(map(list,self.temp_gen_seq))
            print('the seq gen is : ',self.temp_gen_seq)

            # try:
            #     self.pred_seq_frame.saved_seq_generated_list.clear()
            #     # for key, value in doc.edges_amount.items():
            #     #     self.pred_seq_frame.add_generated_seq(f"{key}: {value}")
            #     for key, value in doc.edge_table.items():
            #         self.pred_seq_frame.add_generated_seq(f"{key}: {value}")
            # except Exception as e:
            #     print("Seq list problem")

            # Destroy the existing canvas if it exists
            if hasattr(self, 'canvas'):
                self.canvas.get_tk_widget().destroy()


            fig = Figure(figsize=(5,4), dpi=100)
            ax = fig.add_subplot(111)

            ax.clear()
            for i in range(len(self.temp_gen_seq)):
                ax.plot(range(len(self.temp_gen_seq[i])), self.temp_gen_seq[i], linestyle=':', color='red',marker='o')
                for j, val in enumerate(self.temp_gen_seq[i]):
                    ax.text(j, val, str(val), color='red', ha='right', va='bottom')
            for j, val in enumerate(self.number):
                ax.text(j, val, str(val), color='blue', ha='right', va='bottom')  # Display the value on each marker
            ax.plot(range(len(self.number)), self.number, marker='o', color='blue')
        
            ax.set_title("Graph_Learner")
            ax.set_ylabel("Number")
            ax.set_xlabel("Step")

            canvas = FigureCanvasTkAgg(fig, master=self.tab2)
            canvas.draw()
            canvas.get_tk_widget().grid(row=1, column=4, pady=(10, 0), sticky="nsew", columnspan=4)
            # canvas.get_tk_widget().grid(row=2, column=0, pady=(10, 0), sticky="nsew", columnspan=8)
            # canvas.get_tk_widget().grid(row=1, column=0, pady=(10, 0), sticky="nsew", columnspan=8)
            
        except Exception as e:
            print(e)

    def choose_event(self):
        if self.switch_var.get() == "off":
            self.get_pred_num()
        else:
            if self.temp_gen_seq:
                self.get_pred_num()
                self.draw_network_from_gen()
            else:
                self.draw_network_from_gen()

    def draw_network_from_gen(self):
        # Create a graph
        G = nx.DiGraph()

        if len(self.temp_gen_seq) > 1:
            edges = []
            for seq in self.temp_gen_seq:
                edges.extend(list(zip(seq[:-1], seq[1:])))
            G.add_edges_from(edges)
        else:
            for seq in self.temp_gen_seq:
                G.add_edges_from(list(zip(seq[:-1], seq[1:])))

        color_list = []
        print(G.nodes())
        for num in G.nodes():
            if num in self.number:
                color_list.append('skyblue')
            else:
                color_list.append('red')
        print(color_list)

        # Destroy the existing canvas if it exists
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()
            
        # Draw the graph
        # pos = nx.kamada_kawai_layout(G)
        pos = nx.spring_layout(G, k=2/math.sqrt(G.order()))
        
        fig, ax = plt.subplots(figsize=(6, 4))
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=color_list,
                font_color="black", font_size=10, edge_color="gray", linewidths=1, alpha=0.7, ax=ax, connectionstyle="arc3,rad=0.1")

        # Draw the graph in a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.tab2)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=4, pady=(10, 0), sticky="nsew", columnspan=4)

    def create_evaluation_tab(self):
        self.tab3.grid_rowconfigure((1,2), weight=1)
        self.tab3.grid_columnconfigure((0,1), weight=1)

        self.network_frame = NetworkFrame(self.tab3)
        self.network_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.bar_chart_frame = BarChartFrame(self.tab3)
        self.bar_chart_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.f1_frame = F1Frame(self.tab3)
        self.f1_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.error_rate_frame = ErrorRateFrame(self.tab3)
        self.error_rate_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        eva_btn = customtkinter.CTkButton(self.tab3, text="Evaluate", command=self.evaluated)
        eva_btn.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.sort_btn = customtkinter.CTkButton(self.tab3, text="Descending", command=self.set_sort_state)
        self.sort_btn.grid(row=0, column=1, padx=10, pady=10, sticky="e")

    def evaluated(self):
        self.network_frame.draw_network()
        self.bar_chart_frame.draw_Bar_Chart()

    def isDesc(self):
        if self.sort_desc:
            self.sort_btn.configure(text="Ascending")
        else:
            self.sort_btn.configure(text="Descending")
    
    def get_sort_state(self):
        return self.sort_desc
    
    def set_sort_state(self):
        self.sort_desc = not self.sort_desc
        self.isDesc()
        self.bar_chart_frame.draw_Bar_Chart()
        self.network_frame.draw_network()

    
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Graph Learner GUI")
        self.geometry("1920x1080")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        customtkinter.set_appearance_mode("dark")

        global tab_view
        tab_view = MyTabView(self)
        tab_view.grid(row=0, column=0, ipadx=1920, ipady=1080, padx=20, pady=(5, 20))


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