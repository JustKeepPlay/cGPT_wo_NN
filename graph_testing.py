import customtkinter

def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

app = customtkinter.CTk()
app.title("Testing")
app.geometry("300x400")

radio_var = customtkinter.IntVar(value=0)
radiobutton_1 = customtkinter.CTkRadioButton(
                                                app, 
                                                text="CTkRadioButton 1", 
                                                command=radiobutton_event, 
                                                variable= radio_var, 
                                                value=1
                                            )
radiobutton_1.grid(row=0, column=0, padx=0, pady=0)
radiobutton_2 = customtkinter.CTkRadioButton(
                                                app, 
                                                text="CTkRadioButton 2",
                                                command=radiobutton_event, 
                                                variable= radio_var, 
                                                value=2
                                             )
radiobutton_2.grid(row=1, column=0, padx=0, pady=0)

app.mainloop()
