import sys
import tkinter as tk


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        title, icon = kwargs.get('title', 'Vaaya'), kwargs.get('icon', 'vaaya.png')
        kwargs.pop('title', None)
        kwargs.pop('icon', None)

        tk.Tk.__init__(self, *args, **kwargs)

        if sys.platform.startswith('win'):
            tk.Tk.iconbitmap(self, default=icon)
        else:
            tk.Tk.iconbitmap(self, bitmap='@'+icon)
        tk.Tk.wm_title(self, title)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
