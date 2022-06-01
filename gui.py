import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from solver import *
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
# import os


def open_file(root, pict_label):
    file = askopenfile(parent=root, mode="rb", title="Choose a file", filetypes=[("Text files", "*txt")])
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
    
    
    
    srcList(root, arr, G)
    
def drawGraph(adj_matrix, arr):
    G =  nx.Graph()
    for i in range (len(adj_matrix[0])):
        for j in range(i+1,len(adj_matrix[0])):
            if (adj_matrix[i][j] > 0):
                G.add_edge(arr[i], arr[j], weight = adj_matrix[i][j])
    

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G,pos, node_size=300)
    nx.draw_networkx_edges(G,pos, edgelist=G.edges(), edge_color="red")
    nx.draw_networkx_labels(G, pos)
    edge_labels = nx.get_edge_attributes(G, "weight")

    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    # plt.show()
    # plt.draw()
    plt.savefig("img1.png", dpi=100)
    plt.close()
    showImg("img1.png")

def showImg(img):
    pict = ImageTk.PhotoImage(Image.open(img))
    
    # pict_label = tk.Label(image = pict)
    pict_label.config(image = pict)
    pict_label.image = pict


def srcList(root, option, G):
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
                            command= lambda:show(root,valSrc, valDst, G), 
                            bg="#20bebe",
                            fg="white",
                            font=("Raleway", 15),
                            height=2,
                            width=10).grid(column=2, row=3)

def show(root, valSrc, valDst, G):
    info_label.config(text="")
    info_label.config(text= "Lintasan dari "+ valSrc.get() + " Menuju " + valDst.get(), font=("Raleway", 15))

    _, cost, path = G.Dijkstra(valSrc.get(), valDst.get())
    solution = "".join(path) + " dengan cost " + str(cost)
    # myLabel = tk.Label(root, text=valSrc.get() + "->" + valDst.get(), font=("Raleway", 15))

    # solution_label.config(text = "")
    solution_label.config(text = solution)
    # solution_label.grid(column= 2, row = 5)

    

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=600)
canvas.grid( columnspan=5, rowspan= 5)



    # pict_label = tk.Label(image = pict)
pict_label = tk.Label()
pict_label.grid(column=2, row=0)
# pict_label.grid(column=1, row=0)

#instruction
instruction = tk.Label(root, text="Select a txt file on your computer", font = "Raleway")
instruction.grid(column=2, row=1)

#Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command = lambda:open_file(root, pict_label), font ="Raleway", bg="#20bebe", fg="white", height=3, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=2)

# label solution
info_label = tk.Label(root, font=("Raleway", 15))
info_label.grid(column= 2, row = 4)

solution_label = tk.Label(root, font=("Raleway", 15))
solution_label.grid(column= 2, row = 5)

root.mainloop()