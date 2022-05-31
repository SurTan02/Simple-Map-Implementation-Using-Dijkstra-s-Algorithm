
import matplotlib.figure as fg
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
# tkinter._test()

edges = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

# edges = [[0, 4, 2, 0, 0, 0],
#          [4, 0, 1, 5, 0, 0],
#          [2, 1, 0, 8, 10, 0],
#          [0, 5, 8, 0, 2, 6],
#          [0, 0, 10, 2, 0, 3],
#          [0, 0, 0, 6, 3, 0]]
G =  nx.Graph()
# G.add_edge([('A','B'), ("A","C"), ("B","C")])
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for i in range (len(edges[0])):
    for j in range(i+1,len(edges[0])):
        if (edges[i][j] > 0):
            G.add_edge(arr[i], arr[j], weight = edges[i][j])
# G.add_edge('A','C', weight=7)
# G.add_edge('C','B', weight=3)
# G.add_edge('C','D', weight=2)
# G.add_edge('D','E', weight=1)
# G.add_edge('D','F', weight=5)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G,pos, node_size=300)
nx.draw_networkx_edges(G,pos, edgelist=G.edges(), edge_color="red")
nx.draw_networkx_labels(G, pos)
edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edge_labels(G, pos, edge_labels)
plt.show()
# plt.savefig("file1.png")

window = tk.Tk()
f = plt.Figure(figsize=(5, 5), dpi=100)

# create matplotlib canvas using figure `f` and assign to widget `window`
canvas =  FigureCanvasTkAgg(f, window)
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

# canvas.draw()
# get canvas as tkinter's widget and `gird` in widget `window`
# canvas.get_tk_widget().grid(row=..., column=...)
# canvas.show()

window.mainloop()