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
            
            
    # def get_pred_num(self):
    #     try:
    #         self.temp_gen_seq = []
    #         history = int(self.history_field.get())
    #         self.number = [int(num) for num in self.number_field.get().split(',')]
    #         generate = int(self.gen_field.get())
            
    #         for i in range(10):
    #             gen_num = doc.gen_next_n(self.number.copy(), generate, history)
    #             self.temp_gen_seq.append(gen_num)
    #         self.temp_gen_seq = set(map(tuple,self.temp_gen_seq))
    #         self.temp_gen_seq = list(map(list,self.temp_gen_seq))
    #         print('the seq gen is : ',self.temp_gen_seq)

    #         try:
    #             self.pred_seq_frame.saved_seq_generated_list.clear()
    #             # for key, value in doc.edges_amount.items():
    #             #     self.pred_seq_frame.add_generated_seq(f"{key}: {value}")
    #             for key, value in doc.edge_table.items():
    #                 self.pred_seq_frame.add_generated_seq(f"{key}: {value}")
    #         except Exception as e:
    #             print("Seq list problem")

    #         # Destroy the existing canvas if it exists
    #         if hasattr(self, 'canvas'):
    #             self.canvas.get_tk_widget().destroy()


    #         fig = Figure(figsize=(5,4), dpi=100)
    #         ax = fig.add_subplot(111)

    #         ax.clear()
    #         for i in range(len(self.temp_gen_seq)):
    #             ax.plot(range(len(self.temp_gen_seq[i])), self.temp_gen_seq[i], linestyle=':', color='red',marker='o')
    #             for j, val in enumerate(self.temp_gen_seq[i]):
    #                 ax.text(j, val, str(val), color='red', ha='right', va='bottom')
    #         for j, val in enumerate(self.number):
    #             ax.text(j, val, str(val), color='blue', ha='right', va='bottom')  # Display the value on each marker
    #         ax.plot(range(len(self.number)), self.number, marker='o', color='blue')
        
    #         ax.set_title("Graph_Learner")
    #         ax.set_ylabel("Number")
    #         ax.set_xlabel("Step")

    #         canvas = FigureCanvasTkAgg(fig, master=self.tab2)
    #         canvas.draw()
    #         canvas.get_tk_widget().grid(row=1, column=4, pady=(10, 0), sticky="nsew", columnspan=4)
    #         # canvas.get_tk_widget().grid(row=2, column=0, pady=(10, 0), sticky="nsew", columnspan=8)
    #         # canvas.get_tk_widget().grid(row=1, column=0, pady=(10, 0), sticky="nsew", columnspan=8)
            
    #     except Exception as e:
    #         print(e)