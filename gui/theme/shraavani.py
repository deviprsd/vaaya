from tkinter import ttk
import tkinter as tk


class Colors:
    primary = '#ABD3FB'
    secondary = '#CCE4F4'
    re_prim = '#abd5fe'
    text = '#EBEFF2'
    pm_dark = '#92B8D9'
    pm_light = '#9CC4E8'


class Shraavani:
    def __init__(self):
        self.style = ttk.Style()

    def apply(self):
        self.style.theme_create('shraavani', parent='default', settings={
            ".": {"configure": {"background": Colors.primary,
                                "foreground": Colors.text,
                                "relief": "flat",
                                "highlightcolor": Colors.pm_dark}},
            "Splash.Label": {"configure": {"background": Colors.re_prim}}
        })
        self.style.theme_use('shraavani')
