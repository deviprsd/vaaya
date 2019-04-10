import tkinter as tk
from tkinter import ttk


def get_element_details(style):
    print('element: %s' % style)
    print('option: %s' % str(s.element_options(style)))
    layout = s.layout(style)
    for elem, elem_dict in layout:
        get_sub_element_details(elem, elem_dict)
    print(layout)


def get_sub_element_details(elem, _dict, depth=1):
    print('%selement: %s' % (''.join(['\t' for i in range(depth)]), elem))
    for key in _dict:
        if key != 'children':
            print('%s%s: %s' % (''.join(['\t' for i in range(depth+1)]), key, _dict[key]))
    print('%soption: %s' % (''.join(['\t' for i in range(depth+1)]), s.element_options(elem)))
    if 'children' in _dict:
        for child, child_dict in _dict['children']:
            get_sub_element_details(child, child_dict, depth+1)


root = tk.Tk()
widget = ttk.Spinbox(root, text='test')
widget.grid(sticky='nesw')

style = widget.winfo_class()

s = ttk.Style()
"""print(s.element_names())

print(s.theme_use())
print('normal theme')
get_element_details(style)

print('\nclam theme')
s.theme_use('clam')
print(s.element_names())
get_element_details(style)"""

s.theme_use('default')

for d in dir(ttk):
    if not d.startswith('T') or not d.startswith('_') or d[0].islower():
        try:
            get_element_details('T' + d)
        except tk.TclError:
            pass