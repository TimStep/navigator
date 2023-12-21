import customtkinter as ct
from готовоквыходу import PreparationForVisualization
import math
INF = math.inf

ct.set_appearance_mode('dark')
ct.set_default_color_theme('dark-blue')
root = ct.CTk()
root.geometry('700x1000')
root.title('NAVIGATOR')
First_label = ct.CTkLabel(root, text='''Hello!!! This is Graph Navigator!!!
Please, add your graph''')
First_label.pack(pady=40)


functionlabel = ct.CTkLabel(root, text='write function')
entryoffunction = ct.CTkEntry(root)
functionlabel.pack(pady=10)
entryoffunction.pack(pady=20)



graphlabel = ct.CTkLabel(root, text='write graph matrix or massive of edges')
entryofgraph = ct.CTkEntry(root)
graphlabel.pack(pady=10)
entryofgraph.pack(pady=20)



typelabel=ct.CTkLabel(root,  text='write what you have chosen: massive of edges or graph of matrix')
entryoftype = ct.CTkEntry(root)
typelabel.pack(pady=10)
entryoftype.pack(pady=20)



fromtolabel=ct.CTkLabel(root,  text='write nodes which will be the start and the end in format: "A B"')
entryoffromto = ct.CTkEntry(root)
fromtolabel.pack(pady=10)
entryoffromto.pack(pady=20)

namlabel=ct.CTkLabel(root,  text='write names of nodes in format: "A B C ..."')
entryofnam = ct.CTkEntry(root)
namlabel.pack(pady=10)
entryofnam.pack(pady=20)


def go():
    fromto = entryoffromto.get().split()
    start = int(fromto[0])
    end = int(fromto[1])
    graph = PreparationForVisualization(test_graph, entryoftype.get(), entryofnam.get().split(), function=entryoffunction.get())
    graph.VisualisationOfShortestWay(start, end)


button = ct.CTkButton(root, text='ready', command=go)
button.pack()



test_graph = [
        [0, 1, 1, 1, INF],
        [1, 0, INF, 1, 1],
        [1, INF, 0, 1, INF],
        [1, 1, 1, 0, 1],
        [INF, 1, INF, 1, 0]]




root.mainloop()
