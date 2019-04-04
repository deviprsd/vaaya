from tkinter import ttk


class Colors():
    primary = '#ABD3FB',
    secondary = '#CCE4F4',
    text = '#EBEFF2',
    pm_dark = '#92B8D9',
    pm_light = '#9CC4E8'

class Shraavani():
    def __init__(self):
        self.style = ttk.Style()
        self.palette = {
            'primary': '#ABD3FB',
            'secondary': '#CCE4F4',
            'text': '#EBEFF2',
            'pm_dark': '#92B8D9',
            'pm_light': '#9CC4E8'
        }

    def apply(self):
        self.style.theme_create('shraavani', parent='default', settings={
            ".": {"configure": {"background": Colors.primary,
                                "foreground": Colors.pm_dark,
                                "relief": "flat",
                                "highlightcolor": Colors.text}},
        })
        self.style.theme_use('shraavani')
