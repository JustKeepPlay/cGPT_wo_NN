from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from customtkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Graph_Learner import doc_graph
import networkx as nx
import ast, os, random
import math
from CTkMenuBar import *

doc = doc_graph(5, 'rand')

class NumberSequenceFrame(ctk.CTkScrollableFrame):
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

            seq_scroll = ctk.CTkScrollableFrame(self, orientation="horizontal", height=25)
            seq_scroll.grid(row=length, column=0, padx=(0, 5), pady=(0, 5), sticky="nsew")

            checkbox = ctk.CTkCheckBox(seq_scroll, text=str(tuple(seq)), font=("Ariel", 20))
            checkbox.select()
            checkbox.grid(row=0, column=0, sticky="ew")
            self.checklists.append(checkbox)

            history_field = ctk.CTkTextbox(self, width=110, height=10, font=("Ariel", 30), activate_scrollbars=False)
            history_field.grid(row=length, column=1, padx=(0, 5), pady=(0, 5), sticky="nsew")
            history_field.insert("0.0", str(history))
            self.seq_history.append(history_field)

            count_label = ctk.CTkTextbox(self, width=110, height=10, font=("Ariel", 30), activate_scrollbars=False)
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
        
    
class PredictSequenceFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="grey30")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        self.saved_seq_generated_list = []
        self.generated_widgets = {}
    
    def add_generated_seq(self, seq):
        self.saved_seq_generated_list.append(seq)
        length = len(self.saved_seq_generated_list) - 1

        seq_no = ctk.CTkLabel(self, text=str(length+1), font=("Ariel", 30))
        seq_no.grid(row=length, column=0, sticky="we")
        seq_list = ctk.CTkScrollableFrame(self, orientation="horizontal", height=25)
        seq_list.grid(row=length, column=1, pady=(0, 5), sticky="we")
        seq_num = ctk.CTkLabel(seq_list, text=self.saved_seq_generated_list[-1], font=("Ariel", 20))
        seq_num.grid(row=0, column=0, sticky="we")

        # Store the widgets in a dictionary for later destruction
        self.generated_widgets[length] = (seq_no, seq_list, seq_num)

    def destroy_generated_widgets(self):
        for widgets in self.generated_widgets.values():
            for widget in widgets:
                widget.destroy()
        # Clear the generated widgets dictionary after destruction
        self.generated_widgets = {}

class UserDecisionFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="grey30", height=200)
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.var = ctk.IntVar()

        self.create_frame()

    def create_frame(self):
        # All generated sequence
        self.seq_gen = ctk.CTkEntry(self, font=("Ariel", 20))
        self.seq_gen.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)

        # To generate next
        self.gen_next = ctk.CTkEntry(self, font=("Ariel", 20))
        self.gen_next.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)

        self.accept_btn = ctk.CTkButton(self, text="Accept", command=lambda: self.var.set(1))
        self.accept_btn.grid(row=2, column=0, padx=10, pady=10)


class FactorSequenceFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="lightgreen")

class NetworkFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="grey30")
        
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

        plt.close()
        self.network_fig, ax = plt.subplots(figsize=(6, 4))
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue",
                font_color="black", font_size=10, edge_color="gray", linewidths=1, alpha=1, ax=ax)

        # Draw the graph in a Tkinter canvas
        canvas = FigureCanvasTkAgg(self.network_fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class BarChartFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="grey30")

    def draw_Bar_Chart(self):
        edge_weights = doc.edges_amount
        edge = dict(sorted(edge_weights.items(), key=lambda item: item[1]))
        try:
            if tab_view.get_sort_state():
                edges = [str(_) for _ in list(edge.keys())[-20:]]
                values = list(edge.values())[-20:]
            else:
                edges = [str(_) for _ in list(edge.keys())[:20]]
                values = list(edge.values())[:20]
        except Exception as e:
            print(e)

        # Destroy the existing canvas if it exists
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()
        
        self.bar_fig = Figure(figsize=(7, 5), dpi=100)
        ax = self.bar_fig.add_subplot(111)

        ax.clear()

        try:
            ax.barh(edges, values)
        except Exception as e:
            print(e)


        # Adding labels and title
        ax.set_xlabel('Weight')
        ax.set_ylabel('Edge')
        ax.set_title('Edges Frequency')


        # Draw the graph in a Tkinter canvas
        canvas = FigureCanvasTkAgg(self.bar_fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class F1Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="lightgreen")
        self.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self, text="F1", text_color="black").grid(row=0, column=0)

class ErrorRateFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="orange")
        self.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self, text="Error Rate Frame", text_color="black").grid(row=0, column=0)
        

class MyTabView(ctk.CTkTabview):

    def __init__(self, master):
        super().__init__(master)
        self.tab1 = self.add("Learning Tab")
        self.tab2 = self.add("Prediction Tab")
        self.tab3 = self.add("Evaluation Tab")

        self.seq_list = []

        self.create_learning_tab()
        self.create_prediction_tab()
        self.create_evaluation_tab()

        self.set("Learning Tab")

        self.sort_desc = True

    def create_learning_tab(self):
        upload_btn = ctk.CTkButton(self.tab1, text="Upload File", command=self.upload_file)
        upload_btn.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.seq_entry = ctk.CTkEntry(self.tab1)
        self.seq_entry.grid(row=1, column=0, padx=(0, 10), pady=(0, 10), ipadx=100)
        self.seq_entry.insert(0, "1,2,3,4,5")
        self.seq_entry.bind("<Return>", self.add_seq_enter)

        add_seq_btn = ctk.CTkButton(self.tab1, text="Add", width=30, command=self.get_seq)
        add_seq_btn.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        clear_entry_btn = ctk.CTkButton(self.tab1, text="Clear", width=30, command=self.clear_entry)
        clear_entry_btn.grid(row=1, column=2, pady=(0, 10), sticky="w")

        save_seq_btn = ctk.CTkButton(self.tab1, text="Save Sequence", fg_color="green", hover_color="darkgreen", command=self.save_sequence)
        save_seq_btn.grid(row=2, column=0, padx=(0, 10), pady=(0, 10), sticky="w")

        # self.train_btn = ctk.CTkButton(self.tab1, text="Train Data from checklist", command=self.train_data)
        # self.train_btn.grid(row=5, column=2, pady=(0, 10), sticky="e")

        self.number_seq_frame = NumberSequenceFrame(self.tab1)
        self.number_seq_frame.grid(row=5, column=0, pady=(0, 10), sticky="nsew", columnspan=3)
        self.tab1.grid_rowconfigure(5, weight=1) # Expand an entire of row 3 to fit the window

        ctk.CTkLabel(self.tab1, text="History", font=("Ariel", 20)).grid(row=4, column=0, sticky="e")
        ctk.CTkLabel(self.tab1, text="Amount", font=("Ariel", 20)).grid(row=4, column=2)

        select_all_cb = ctk.CTkCheckBox(self.tab1, text="Select All", font=("Ariel", 20), command=self.number_seq_frame.select_all)
        select_all_cb.select()
        select_all_cb.grid(row=3, column=0, padx=(0, 10), pady=(0, 10), sticky="w")

        self.create_network = ctk.CTkButton(self.tab1, text="Create Network", command=self.train_data)
        self.create_network.grid(row=3, column=2, padx=(0, 10), pady=(0, 10))

        # remove_seq_btn = ctk.CTkButton(self.tab1, text="Remove Sequence", fg_color="red", hover_color="darkred", command=self.remove_sequence)
        # remove_seq_btn.grid(row=6, column=0, padx=(0, 10), pady=(0, 10), sticky="w")

    def remove_sequence(self):
        print("Remove Sequence Button clicked!")


    def save_sequence(self):
        saved_sequences_dir = "Saved Sequences"
        os.makedirs(saved_sequences_dir, exist_ok=True)
        file_path = os.path.join(saved_sequences_dir, "Sequence_1.txt")
        counter = 1
        while True:
            if not os.path.exists(file_path):
                break
            counter += 1
            new_file_name = f"Sequence_{counter}.txt"
            file_path = os.path.join(saved_sequences_dir, new_file_name)
        try:
            with open(file_path, 'x') as file:
                checked_sequences = self.number_seq_frame.get_checklist()
                for seq in checked_sequences:
                    seq_str = ','.join(map(str, seq))
                    file.write(seq_str + '#\n')
            self.show_checkmark("List of sequences saved successfully.")
        except Exception as e:
            print(f"Error saving sequences: {e}")
   

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
        
        amount_of_seq = 10
        with open(file_name, 'w') as file:
            for i in range(amount_of_seq):
                sequence = self.generate_sequence()
                file.write(sequence + "\n")

        print(f"All sequences saved in {file_name}")

    def clear_entry(self):
        self.seq_entry.delete(0, ctk.END)

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
        canvas.get_tk_widget().grid(row=0, column=3, padx=(10, 0), pady=(0, 10), sticky="nsew", rowspan=6)
        self.tab1.grid_columnconfigure(3, weight=1) # Expand an entire of column 2 to fit the window

    def process_sequences(self, input_values):
        if '*' in input_values:
            # Split the string by '*'
            parts = input_values.split('*')

            # Extract the sequence and repeat count
            sequence = parts[0].split(',')
            multiplier = parts[1].replace('#', '')

            # Repeat the sequence and concatenate with #
            result = ','.join(sequence * int(multiplier))
            return result
        return input_values

    def show_error(self):
        # Show some error message
        CTkMessagebox(title="Error", message="Non-numerical Sequence not allowed.", icon="cancel")

    def isNumber(self, input_values):
        return all((i.strip().replace('.', '').isdigit() or i == '*' or i == "#" for i in item) for item in input_values.split(','))

    def get_seq(self):
        input_values = self.seq_entry.get()
        if self.isNumber(input_values):
            seq_after_process = self.process_sequences(input_values)
            try:
                seq = [int(num) for num in seq_after_process.split(',')]
                self.seq_list.append(seq)
                self.number_seq_frame.add_num_seq(seq, 5, 1)
            except Exception as e:
                print(f"Get Sequence error: {e}")
        else:
            self.show_error()
            
    def get_seq_from_upload(self, content_before_hash):
        if self.isNumber(content_before_hash):
            seq_after_process = self.process_sequences(content_before_hash)
            try:
                seq = [int(num) for num in seq_after_process.split(',')]
                self.seq_list.append(seq)
                history = random.randint(1, 10)
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

                for _ in range(count):
                    doc.add_doc(list(seq), history)
                # doc.add_doc(list(seq), history, count)
            self.draw_graph()
            self.show_checkmark("Sequence train successfully.")
            self.create_network.configure(state="normal")
        except Exception as e:
            print(e)

    def show_checkmark(self, msg):
        # Show some positive message with the checkmark icon
        CTkMessagebox(header=True, title="Success", message=msg,
                  icon="check", option_1="OK")

# ---------------------
        
    def create_prediction_tab(self):
        self.switch_var = ctk.StringVar(value="off")
        self.tab2.grid_rowconfigure(1, weight=1)
        self.tab2.grid_columnconfigure(7, weight=1)

        number_label = ctk.CTkLabel(self.tab2, text="Sequence: ")
        number_label.grid(row=0, column=0, padx=(0, 10))
        self.number_field = ctk.CTkEntry(self.tab2)
        self.number_field.grid(row=0, column=1, padx=(0, 10), ipadx=20)
        self.number_field.insert(0, "1,2")
        self.number_field.bind("<Return>", self.gen_seq_enter)

        history_label = ctk.CTkLabel(self.tab2, text="History: ")
        history_label.grid(row=0, column=2, padx=(0, 10))
        self.history_field = ctk.CTkEntry(self.tab2)
        self.history_field.grid(row=0, column=3, padx=(0, 10), ipadx=20)
        self.history_field.insert(0, "5")
        self.history_field.bind("<Return>", self.gen_seq_enter)

        gen_label = ctk.CTkLabel(self.tab2, text="Generation Amount: ")
        gen_label.grid(row=0, column=4, padx=(0, 10))
        self.gen_field = ctk.CTkEntry(self.tab2)
        self.gen_field.grid(row=0, column=5, padx=(0, 10), ipadx=20)
        self.gen_field.insert(0, "3")
        self.gen_field.bind("<Return>", self.gen_seq_enter)

        gen_btn = ctk.CTkButton(self.tab2, text="Generate", command=self.generate_by_switch)
        gen_btn.grid(row=0, column=6, padx=(0, 10))

        self.switch = ctk.CTkSwitch(self.tab2, text="Switch Graph/Network", command=self.generate_by_switch,
                                        variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.grid(row=0, column=7, sticky="e")

        self.pred_seq_frame = PredictSequenceFrame(self.tab2)
        self.pred_seq_frame.grid(row=1, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew", columnspan=4, rowspan=3)

        self.all_route_frame = ctk.CTkScrollableFrame(self.tab2)
        self.all_route_frame.grid(row=1, column=4, padx=(0, 10), pady=(10, 0), ipady=500, sticky="nsew", columnspan=4, rowspan=2)
        self.all_route_frame.grid_rowconfigure(0, weight=1)
        self.all_route_frame.grid_columnconfigure(0, weight=1)
        
        self.gen_next_frame = ctk.CTkFrame(self.tab2)
        self.gen_next_frame.grid(row=3, column=4, padx=(0, 10), pady=(10, 0), sticky="sew", columnspan=4)
        self.gen_next_frame.grid_rowconfigure(0, weight=1)
        self.gen_next_frame.grid_columnconfigure(0, weight=1)

        self.user_decision_frame = UserDecisionFrame(self.tab2)
        self.user_decision_frame.grid(row=3, column=0, padx=(0, 10), pady=(10, 0), sticky="sew", columnspan=4)

        # factor_seq_frame = FactorSequenceFrame(self.tab2)
        # factor_seq_frame.grid(row=1, column=0, pady=(10, 0), sticky="nsew", columnspan=8)

        # main_seq_frame = MainSequenceFrame(self.tab2)
        # main_seq_frame.grid(row=3, column=0, pady=(10, 0), sticky="nsew", columnspan=8)

    def gen_seq_enter(self, event):
        try:
            self.generate_by_switch()
        except Exception as e:
            print(e)

    def is_sequence_in_lists(self, num_list):
        print(f"Check if in list: {num_list}")
        for lst in self.generated_list:
            if all(item in lst for item in num_list):
                print("Sequence exists")
                return True
        print("Sequence does not exists")
        return False

    def gen_next_by_one(self):
        try:
            self.history = int(self.history_field.get())
            self.number = [int(num) for num in self.number_field.get().split(',')]
            self.generate = int(self.gen_field.get())
            step = self.generate

            self.num = self.number.copy()

            fig, ax = plt.subplots(figsize=(6,4), dpi=100)

            self.gen_num = []
            self.user_decision_frame.accept_btn.configure(state="normal")
            for i in range(step):
                # Destroy the existing canvas if it exists
                if hasattr(self.gen_next_frame, 'canvas'):
                    self.gen_next_frame.canvas.get_tk_widget().destroy()

                self.gen_num = doc.gen_next(self.num.copy(), self.history)
                print('the seq gen is : ',self.gen_num)
                    
                self.user_decision_frame.var.set(0)
                
                self.user_decision_frame.seq_gen.configure(state="normal")
                self.user_decision_frame.gen_next.configure(state="normal")
                self.user_decision_frame.seq_gen.delete(0, 'end')
                self.user_decision_frame.gen_next.delete(0, 'end')

                self.user_decision_frame.seq_gen.insert(0, str(self.gen_num[:-1]))
                self.user_decision_frame.gen_next.insert(0, str(self.gen_num[-1]))
                self.user_decision_frame.seq_gen.configure(state="disable")
                # self.user_decision_frame.gen_next.configure(state="disable")
                
                try:
                    # Draw all the plot as red
                    ax.plot(range(1, len(self.gen_num) + 1, 1), self.gen_num, linestyle=':', color='red',marker='o')
                    for i, value in enumerate(self.gen_num):
                        ax.text(i + 1, value, str(value), color='red', ha='right', va='bottom')

                    # Draw the initial plot as blue
                    ax.plot(range(1, len(self.num) + 1, 1), self.num, marker='o', color='blue')
                    for i, value in enumerate(self.num):
                        ax.text(i + 1, value, str(value), color='blue', ha='right', va='bottom')  # Display the value on each marker
                except Exception as e:
                    print(f"Error plotting graph: {e}")

                canvas = FigureCanvasTkAgg(fig, master=self.gen_next_frame)
                self.gen_next_frame.canvas = canvas
                canvas.draw()
                canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

                self.generate_all_possible_route()
                self.user_decision_frame.accept_btn.wait_variable(self.user_decision_frame.var)

                try:
                    self.num = self.gen_num[:-1]
                    print(f"self.num: {self.num}")
                    self.num.extend([int(i) for i in self.user_decision_frame.gen_next.get().split(',')])
                    print(f"self.num after extend: {self.num}")

                    if (not self.is_sequence_in_lists(self.num)):
                        print(f"{self.num} not in learning")
                        doc.add_doc(self.num, self.history)
                        self.seq_list.append(self.num)
                        self.generate_all_possible_route()
                        self.show_checkmark("Sequence train successfully.")
                    else:
                        # Destroy the existing canvas if it exists
                        if hasattr(self.gen_next_frame, 'canvas'):
                            self.gen_next_frame.canvas.get_tk_widget().destroy()
                        
                        ax.plot(range(1, len(self.num) + 1, 1), self.num, marker='o', color='blue')
                        for i, value in enumerate(self.num):
                            ax.text(i + 1, value, str(value), color='blue', ha='right', va='bottom')  # Display the value on each marker

                        canvas = FigureCanvasTkAgg(fig, master=self.gen_next_frame)
                        self.gen_next_frame.canvas = canvas
                        canvas.draw()
                        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

                except Exception as e:
                    print(f"Error get input from entry to num: {e}")

                ax.set_title(f"Graph_Learner")
                ax.set_ylabel("Number")
                ax.set_xlabel("Step")

            self.user_decision_frame.var.set(0)
            self.user_decision_frame.seq_gen.configure(state="normal")
            self.user_decision_frame.gen_next.configure(state="normal")
            self.user_decision_frame.seq_gen.delete(0, 'end')
            self.user_decision_frame.gen_next.delete(0, 'end')
            self.user_decision_frame.seq_gen.configure(state="disable")
            # self.user_decision_frame.gen_next.configure(state="disable")

            self.user_decision_frame.accept_btn.configure(state="disable")
            # Draw the initial plot as blue
            self.show_checkmark("GraphLeaner successfully generated.")
        except Exception as e:
            print(e)
            
    # def get_pred_num(self):
    #     self.history = int(self.history_field.get())
    #     self.number = [int(num) for num in self.number_field.get().split(',')]
    #     self.generate = int(self.gen_field.get())

    #     try:
    #         # Destroy the existing canvas if it exists
    #         if hasattr(self.gen_next_frame, 'canvas'):
    #             self.gen_next_frame.canvas.get_tk_widget().destroy()

    #         fig, ax = plt.subplots(figsize=(6,4), dpi=100)

    #         self.gen_num = []
    #         self.gen_num = doc.gen_next_n(self.number.copy(), self.generate, self.history)

    #         print('the seq gen is : ',self.gen_num)
            
    #         try:
    #             # Draw all the plot as red
    #             ax.plot(range(1, len(self.gen_num) + 1, 1), self.gen_num, linestyle=':', color='red',marker='o')
    #             for i, value in enumerate(self.gen_num):
    #                 ax.text(i + 1, value, str(value), color='red', ha='right', va='bottom')

    #             # Draw the initial plot as blue
    #             ax.plot(range(1, len(self.number) + 1, 1), self.number, marker='o', color='blue')
    #             for i, value in enumerate(self.number):
    #                 ax.text(i + 1, value, str(value), color='blue', ha='right', va='bottom')  # Display the value on each marker
    #         except Exception as e:
    #             print(f"Error: {e}")

    #         ax.set_title(f"Graph_Learner")
    #         ax.set_ylabel("Number")
    #         ax.set_xlabel("Step")

    #         canvas = FigureCanvasTkAgg(fig, master=self.gen_next_frame)
    #         self.gen_next_frame.canvas = canvas
    #         canvas.draw()
    #         canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    #     except Exception as e:
    #         print(e)

    def generate_all_possible_route(self):
        try:
            self.pred_seq_frame.destroy_generated_widgets()
            self.pred_seq_frame.saved_seq_generated_list.clear()

            unique_sublists = []

            if unique_sublists:
                unique_sublists.clear()

            # Convert each sublist to a tuple and create a set to remove duplicates
            unique_sublists = list(map(tuple, self.seq_list))
            unique_sublists = list(set(unique_sublists))

            # Convert unique sublists back to lists
            unique_sublists = [list(sublist) for sublist in unique_sublists]

            self.generated_list = []

            if self.generated_list:
                self.generated_list.clear()

            # steps = len(self.number) + self.generate
            steps = len(self.num) + 1

            for seq in unique_sublists:
                if len(seq) >= steps:
                    if all(num in seq for num in self.num):
                        start_index = seq.index(self.num[0]) if self.num[0] in seq else -1
                        if start_index != -1 and seq[start_index:start_index + len(self.num)] == self.num:
                            self.generated_list.append(seq[start_index:])
                            self.pred_seq_frame.add_generated_seq(str(self.generated_list[-1]))
                            
        except Exception as e:
            print(f"Seq list problem: {e}")

        # Destroy the existing canvas if it exists
        if hasattr(self.all_route_frame, 'canvas'):
            self.all_route_frame.canvas.get_tk_widget().destroy()

        fig = Figure(figsize=(6,4), dpi=100)
        ax = []
        row = len(self.generated_list)
        column = 1
        for irow, seq in enumerate(self.generated_list):
            ax.append(fig.add_subplot(row, column, irow + 1))
            try:
                ax[-1].plot(range(1, steps + 1, 1), seq[:steps], marker='o', color='blue')
                for i, (step, value) in enumerate(zip(range(1, len(seq) + 1), seq)):
                    ax[-1].text(step, value, str(value), color='blue', ha='right', va='bottom')  # Display the value on each marker
            except Exception as e:
                print(f"error: {e}")
                

            ax[-1].set_title(f"Graph_Learner {irow + 1}", loc='left')
            ax[-1].set_ylabel("Number")
            ax[-1].set_xlabel("Step")

        # Adjust spacing between subplots
        fig.subplots_adjust(hspace=0.5) # Increase the vertical gap between subplots

        canvas = FigureCanvasTkAgg(fig, master=self.all_route_frame)
        self.all_route_frame.canvas = canvas
        canvas.draw()
        # canvas.get_tk_widget().grid(row=1, column=4, pady=(10, 0), sticky="nsew", columnspan=4)
        if len(self.generated_list) <= 3:
            canvas.get_tk_widget().grid(row=0, column=0, sticky="new", ipady=len(self.generated_list) * 25)
        else:
            canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew", ipady=len(self.generated_list) * 75)


    def generate_by_switch(self):
        
        # if self.switch_var.get() == "off":
        #     self.get_pred_num()
        #     self.generate_all_possible_route()
        # else:
        #     if not self.gen_num:
        #         self.get_pred_num()
        #         self.draw_network_from_gen()
        #     else:
        #         self.draw_network_from_gen()
        if self.switch_var.get() == "off":
            self.gen_next_by_one()
            self.user_decision_frame.seq_gen.configure(state="normal")
            self.user_decision_frame.seq_gen.delete(0, 'end')
            self.user_decision_frame.gen_next.delete(0, 'end')
            self.user_decision_frame.gen_next.configure(state="disable")
            self.user_decision_frame.accept_btn.configure(state="disable")
            # self.generate_all_possible_route()
        else:
            if not self.gen_num:
                self.draw_network_from_gen()
            else:
                self.draw_network_from_gen()

    def draw_network_from_gen(self):
        # Create a graph
        G = nx.DiGraph()

        if len(self.gen_num) > 1:
            edges = []
            for seq in self.gen_num:
                edges.extend(list(zip(seq[:-1], seq[1:])))
            G.add_edges_from(edges)
        else:
            for seq in self.gen_num:
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
        if hasattr(self.all_route_frame, 'canvas'):
            self.all_route_frame.canvas.get_tk_widget().destroy()
            
        # Draw the graph
        # pos = nx.kamada_kawai_layout(G)
        pos = nx.spring_layout(G, k=2/math.sqrt(G.order()))
        
        fig, ax = plt.subplots(figsize=(6, 4))
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=color_list,
                font_color="black", font_size=10, edge_color="gray", linewidths=1, alpha=0.7, ax=ax, connectionstyle="arc3,rad=0.1")

        # Draw the graph in a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.all_route_frame)
        canvas.draw()
        # canvas.get_tk_widget().grid(row=1, column=4, pady=(10, 0), sticky="nsew", columnspan=4)
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

# --------------------------------------------------------------------------

    def create_evaluation_tab(self):
        # self.tab3.grid_rowconfigure((1,2), weight=1)
        # self.tab3.grid_columnconfigure((0,1), weight=1)

        self.tab3.grid_rowconfigure(1, weight=1)
        self.tab3.grid_columnconfigure((0, 1), weight=1)

        self.network_frame = NetworkFrame(self.tab3)
        self.network_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.bar_chart_frame = BarChartFrame(self.tab3)
        self.bar_chart_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # self.f1_frame = F1Frame(self.tab3)
        # self.f1_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # self.error_rate_frame = ErrorRateFrame(self.tab3)
        # self.error_rate_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        eva_btn = ctk.CTkButton(self.tab3, text="Evaluate", command=self.evaluated)
        eva_btn.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.sort_btn = ctk.CTkButton(self.tab3, text="Ascending", command=self.set_sort_state)
        self.sort_btn.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        ctk.CTkButton(
            self.tab3, text="Save as image", 
            fg_color="green", 
            hover_color="darkgreen", 
            command=lambda: self.save_image(self.network_frame.network_fig, "Network")
        ).grid(row=2, column=0, padx=(0, 10), pady=(0, 10))

        ctk.CTkButton(
            self.tab3, text="Save as image", 
            fg_color="green", hover_color="darkgreen", 
            command=lambda: self.save_image(self.bar_chart_frame.bar_fig, "Barchart")
        ).grid(row=2, column=1, padx=(0, 10), pady=(0, 10))

    def save_image(self, fig, name):
        saved_sequences_dir = name + " Images"
        os.makedirs(saved_sequences_dir, exist_ok=True)
        file_path = os.path.join(saved_sequences_dir, f"{name}_1.png")
        counter = 1
        while True:
            if not os.path.exists(file_path):
                break
            counter += 1
            new_file_name = f"{name}_{counter}.png"
            file_path = os.path.join(saved_sequences_dir, new_file_name)
        try:
            fig.savefig(file_path)
            self.show_checkmark(f"{name} image saved successfully.")
        except Exception as e:
            print(f"Error saving image: {e}")

    def evaluated(self):
        self.network_frame.draw_network()
        self.bar_chart_frame.draw_Bar_Chart()

    def isDesc(self):
        if self.sort_desc:
            self.sort_btn.configure(text="Descending")
        else:
            self.sort_btn.configure(text="Ascending")

        self.sort_desc = not self.sort_desc
    
    def get_sort_state(self):
        return self.sort_desc
    
    def set_sort_state(self):
        self.isDesc()
        self.bar_chart_frame.draw_Bar_Chart()
        self.network_frame.draw_network()

def change_theme(theme):
    ctk.set_appearance_mode(theme)

    if (ctk.get_appearance_mode() == "Dark"):
        color = "grey30"
    else:
        color="grey70"

    tab_view.number_seq_frame.configure(fg_color=color)
    tab_view.pred_seq_frame.configure(fg_color=color)
    tab_view.user_decision_frame.configure(fg_color=color)
    tab_view.network_frame.configure(fg_color=color)
    tab_view.bar_chart_frame.configure(fg_color=color)

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Graph Learner GUI")
        self.geometry("1920x1080")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")

        menubar = CTkMenuBar(self)
        theme_btn = menubar.add_cascade("Theme")

        theme_dropdown = CustomDropdownMenu(widget=theme_btn)
        theme_dropdown.add_option(option="Dark", command=lambda: change_theme("dark"))
        theme_dropdown.add_option(option="Light", command=lambda: change_theme("light"))

        global tab_view
        tab_view = MyTabView(self)
        tab_view.pack(ipadx=1920, ipady=1080, padx=20, pady=(5, 20))

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()