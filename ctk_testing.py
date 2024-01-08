import customtkinter

class MyCheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, fg_color="green")
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
    
class MyRadioButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, fg_color="lightblue")
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()
    
    def set(self, value):
        self.variable.set(value)

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, width=1920, height=1080, fg_color="red")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.add("tab 1")
        self.add("tab 2")

        values_1 = []
        options_1 = []

        for i in range(10):
            values_1.append(f'Value {i + 1}')
            options_1.append(f'Option {i + 1}')

        # self.checkbox_frame = MyCheckboxFrame(self, "Values", values_1=["Value 1", "Value 2", "Value 3"])
        self.checkbox_frame_1 = MyCheckboxFrame(self.tab("tab 1"), "Values", values=values_1)
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        # self.radiobutton_frame = MyRadioButtonFrame(self, "Options", values_1=["Option 1", "Option 2"])
        self.radiobutton_frame_1 = MyRadioButtonFrame(self.tab("tab 1"), "Options", values=options_1)
        self.radiobutton_frame_1.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self.tab("tab 1"), text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        values_2 = []
        options_2 = []

        for i in range(5):
            values_2.append(f'Super Value {i + 1}')
            options_2.append(f'Other Option {i + 1}')

        # self.checkbox_frame = MyCheckboxFrame(self, "Values", values_2=["Value 1", "Value 2", "Value 3"])
        self.checkbox_frame_2 = MyCheckboxFrame(self.tab("tab 2"), "Values", values=values_2)
        self.checkbox_frame_2.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        # self.radiobutton_frame = MyRadioButtonFrame(self, "Options", values_2=["Option 1", "Option 2"])
        self.radiobutton_frame_2 = MyRadioButtonFrame(self.tab("tab 2"), "Options", values=options_2)
        self.radiobutton_frame_2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self.tab("tab 2"), text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        if self.get() == "tab 1":
            print("checkbox_frame_1: ", self.checkbox_frame_1.get())
            print("radiobutton_frame_1: ", self.radiobutton_frame_1.get())
        elif self.get() == "tab 2":
            print("checkbox_frame_2: ", self.checkbox_frame_2.get())
            print("radiobutton_frame_2: ", self.radiobutton_frame_2.get())

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("my app")
        self.geometry("800x600")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.tab_view = MyTabView(self)
        self.tab_view.grid(row=0, column=0, padx=0, pady=0)

app = App()
app.mainloop()