import tkinter as tk
from tkinter import ttk


class MoodActivity(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Visit Page 1")
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2")
        button2.pack()