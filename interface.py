import customtkinter as ct
from готовоквыходу import PreparationForVisualization
import math
INF = math.inf

ct.set_appearance_mode('dark')
ct.set_default_color_theme('dark-blue')
root = ct.CTk()
root.geometry('700x1200')
root.title('NAVIGATOR')
First_label = ct.CTkLabel(root, text='''Please, add your graph''')
First_label.pack(pady=10)


functionlabel = ct.CTkLabel(root, text='write function')
entryoffunction = ct.CTkEntry(root)
functionlabel.pack(pady=10)
entryoffunction.pack(pady=20)



graphlabel = ct.CTkLabel(root, text='write graph matrix or massive of edges (if second, format must be: "1,2,12 2,3,22 name1,name2,length  ..."')
entryofgraph = ct.CTkEntry(root)
graphlabel.pack(pady=10)
entryofgraph.pack(pady=20)



typelabel=ct.CTkLabel(root,  text='write what you have chosen: massive of edges or graph of matrix')
entryoftype = ct.CTkEntry(root)
typelabel.pack(pady=10)
entryoftype.pack(pady=20)



fromtolabel=ct.CTkLabel(root,  text='write nodes which will be the start and the end in format: "1 2"')
entryoffromto = ct.CTkEntry(root)
fromtolabel.pack(pady=10)
entryoffromto.pack(pady=20)




def goD():
    fromto = entryoffromto.get().split()
    start = int(fromto[0])
    end = int(fromto[1])
    graph = PreparationForVisualization(test_graph, entryoftype.get(), function=entryoffunction.get())
    graph.VisualisationOfShortestWayD(start, end)

def goFW():
    fromto = entryoffromto.get().split()
    start = int(fromto[0])
    end = int(fromto[1])
    graph = PreparationForVisualization(test_graph, entryoftype.get(), function=entryoffunction.get())
    graph.VisualisationOfShortestWayFW(start, end)

def goFB():
    fromto = entryoffromto.get().split()
    start = int(fromto[0])
    end = int(fromto[1])
    graph = PreparationForVisualization(test_graph, entryoftype.get(), function=entryoffunction.get())
    graph.VisualisationOfShortestWayFB(start, end)


buttonD = ct.CTkButton(root, text='ready D', command=goD)
buttonFW = ct.CTkButton(root, text='ready FW', command=goFW)
buttonFB = ct.CTkButton(root, text='ready FB', command=goFB)
buttonD.pack()
buttonFW.pack()
buttonFB.pack()



#def newnodef():




#newnode = ct.CTkLabel(root, text='write new node')
#newnodew = ct.CTkEntry(root)
#nww = ct.CTkButton(root, text='ready', command=newnodef)
#newnode.pack(pady=10)
#newnodew.pack(pady=10)
#nww.pack(pady=10)


#def newedgef():




#newedgew = ct.CTkLabel(root, text='write new edge')
#newedgee = ct.CTkEntry(root)
#nwe = ct.CTkButton(root, text='ready', command=newedgef)
#newedgew.pack(pady=10)
#newedgee.pack(pady=10)
#nwe.pack(pady=10)


test_graph = [
        [0, 1, 1, 1, INF],
        [1, 0, INF, 1, 1],
        [1, INF, 0, 1, INF],
        [1, 1, 1, 0, 1],
        [INF, 1, INF, 1, 0]]




root.mainloop()


