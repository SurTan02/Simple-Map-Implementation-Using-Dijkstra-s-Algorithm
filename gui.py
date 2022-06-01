import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from solver import *
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk
from util import *

root = tk.Tk()

# canvas = tk.Canvas(root, width=768, height=640)
# canvas.grid(columnspan=3, rowspan=3)

canvas = tk.Canvas(root, width=800, height=600)
canvas.grid( columnspan=5, rowspan= 5)

# create matplotlib canvas using figure `f` and assign to widget `window`
# gambar

pict_label = tk.Label()
pict_label.grid(column=2, row=0)
# pict_label = tk.Label(image = "")
# pict_label.grid(column=1, row=0)

#instruction
instruction = tk.Label(root, text="Select a txt file on your computer", font = "Raleway")
instruction.grid(column=2, row=1)

#Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command = lambda:open_file(root, pict_label, canvas), font ="Raleway", bg="#20bebe", fg="white", height=3, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=2)



root.mainloop()