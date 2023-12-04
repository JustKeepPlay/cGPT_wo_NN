import tkinter as tk
from tkinter import ttk
from learning_page import create_learning_page
from prediction_page import create_prediction_page
from evaluation_page import create_evaluation_page

def main():
    window = tk.Tk()
    window.geometry('800x600')
    window.title("Graph Learning GUI ")

    notebook = ttk.Notebook(window)

    create_learning_page(notebook)
    create_prediction_page(notebook)
    create_evaluation_page(notebook)

    notebook.pack(fill=tk.BOTH, expand=True)
    window.mainloop()

if __name__ == "__main__":
    main()
