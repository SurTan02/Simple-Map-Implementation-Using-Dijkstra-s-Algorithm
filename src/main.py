import networkx as nx
import util as my_nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import matplotlib.pyplot as plt
from solver import *
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
# import os


def open_file(root):
    file = askopenfile(parent=root, mode="rb", title="Choose a file", filetypes=[("Text files", "*txt")])
    if (file):
        mtrx = open(file.name,"r")

        adj_matrix=[] # Menyimpan matrix
        for line in mtrx.readlines():
            adj_matrix.append( [ int (x) for x in line.split(' ') ] )
        
        arr = []
        for i in range (len (adj_matrix[0])):
            arr.append(chr(ord("A") + i))
        
        G = Graph(len(adj_matrix[0]))
        G.adj_matrix = adj_matrix

        drawGraph(adj_matrix, arr)
        optionPicker(root, arr, G)
    
def drawGraph(adj_matrix, arr):
    G =  nx.DiGraph()
    for i in range (len(adj_matrix[0])):
        for j in range(len(adj_matrix[0])):
            if (adj_matrix[i][j] > 0):
                G.add_weighted_edges_from([(arr[i], arr[j], adj_matrix[i][j])])
                
    pos = nx.spring_layout(G, seed=5)
    _, ax = plt.subplots()

    nx.draw_networkx_nodes(G,pos, node_size=250, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)
    
    curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
    straight_edges = list(set(G.edges()) - set(curved_edges))
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges)
    arc_rad = 0.25
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges, connectionstyle=f'arc3, rad = {arc_rad}')
    
    edge_labels = nx.get_edge_attributes(G, "weight")
    curved_edge_labels = {edge: edge_labels[edge] for edge in curved_edges}
    straight_edge_labels = {edge: edge_labels[edge] for edge in straight_edges}
    my_nx.my_draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=curved_edge_labels,rotate=False,rad = arc_rad)
    nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=straight_edge_labels,rotate=False)
    
    plt.savefig("img1.png", dpi=100)
    plt.close()
    showImg("img1.png")

# Digunakan untuk menampilkan graph
def showImg(img):
    pict = ImageTk.PhotoImage(Image.open(img))
    pict_label.config(image = pict)
    pict_label.image = pict

# Digunakan untuk memilih src, dst, dan solve
def optionPicker(root, option, G):
    valSrc = tk.StringVar()
    valDst = tk.StringVar()
    valSrc.set(option[0])
    valDst.set(option[0])

    dropSrc = tk.OptionMenu(root, valSrc, *option)
    dropSrc.grid(column=1, row=2)
    dropSrc.config (
                    bg="#20bebe",
                    fg="white",
                    font=("Raleway", 15)
                    )

    dropDst = tk.OptionMenu(root, valDst, *option)
    dropDst.grid(column=3, row=2)
    dropDst.config (
                    bg="#20bebe",
                    fg="white",
                    font=("Raleway", 15)
                    )

    solveButton = tk.Button(root, 
                            text="Solve", 
                            command= lambda:show(valSrc, valDst, G), 
                            bg="#20bebe",
                            fg="white",
                            font=("Raleway", 15),
                            height=1,
                            width=10).grid(column=2, row=3)

def show(valSrc, valDst, G):
    info_label.config(text="")
    info_label.config(text= "Lintasan dari "+ valSrc.get() + " Menuju " + valDst.get(), font=("Raleway", 15))

    start = time.time()
    cost, path, iteration = G.Dijkstra(valSrc.get(), valDst.get())
    end = time.time()
    res = "{:.5f}".format((end-start)*1000)

    solution = ">".join(path) + " dengan cost " + str(cost)

    solution_label.config(text = solution)
    
    iteration_label.config(text = "Banyak Iterasi " + str(iteration.index(valDst.get()) + 1))
    time_label.config(text = str(res) + "ms")

    

root = tk.Tk()
root.maxsize(width=960, height=720)
root.minsize(width=960, height=720)

canvas = tk.Canvas(root, width=960, height=720)
canvas.grid( columnspan=5, rowspan= 7)
     
pict_label = tk.Label()
pict_label.grid(column=2, row=0)

#instruction
instruction = tk.Label(root, text="Select a txt file on your computer", font = "Raleway")
instruction.grid(column=2, row=1)

#Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command = lambda:open_file(root), font =("Raleway",15), bg="#20bebe", fg="white", height=1, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=2)

# label solution
info_label = tk.Label(root, font=("Raleway", 15))
info_label.grid(column= 2, row = 4)

solution_label = tk.Label(root, font=("Raleway", 15))
solution_label.grid(column= 2, row = 5)

time_label = tk.Label(root, font=("Raleway", 15))
time_label.grid(column= 1, row = 3)

iteration_label = tk.Label(root, font=("Raleway", 15))
iteration_label.grid(column= 3, row = 3)

root.mainloop()