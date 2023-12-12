import networkx as nx
import matplotlib.pyplot as plt
from graph_main import Graph
import math



INF = math.inf

test_graph = [
    [0, 1, 1, 1, INF],
    [1, 0, INF, 1, 1],
    [1, INF, 0, 1, INF],
    [1, 1, 1, 0, 1],
    [INF, 1, INF, 1, 0]]

g=Graph(test_graph)
class Visualisate():
    def __init__(self,matr):
        self.edges_rev=[]
        self.matr = matr
        self.size = len(self.matr)

        for node1 in range(self.size):
            for node2 in range(self.size):
                if node1 != node2 and self.matr[node1][node2] != INF:
                    self.edges_rev.append((node1, node2, self.matr[node1][node2]))

    def vis_simple_graph(self):

        edges_rev = self.edges_rev
        G = nx.DiGraph()
        G.add_weighted_edges_from(edges_rev)
        weights = nx.get_edge_attributes(G, 'weight')
        pos = nx.circular_layout(G)
        nx.draw_networkx(G, pos=pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
        title = 'graph test'
        plt.title(title)
        plt.show()

    def vis_shortest_way(self,start,final):


        res= g.FordBellman(start, final)
        print(res)
        shortestpath=[]


        for i in range(len(res)):
            if i!=(len(res)-1):
                shortestpath.append((res[i], res[i+1]))


        edges = self.edges_rev


        G = nx.DiGraph()
        G.add_weighted_edges_from(edges)
        weights = nx.get_edge_attributes(G, 'weight')
        pos = nx.circular_layout(G)
        nx.draw_networkx(G, pos=pos)

        nx.draw_networkx_edges(G, pos=pos, edgelist=shortestpath, edge_color="r", width=3)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
        title = 'graph test'
        plt.title(title)
        plt.show()
        print(shortestpath)


a=Visualisate(test_graph)



from tkinter import *
from matplotlib.figure import Figure







app = Tk()





def entry_data():


    start = int(float(entry_widget1.get()))
    finish = int(float(entry_widget2.get()))
    return start,finish




def plot():

    fig = Figure(figsize=(5, 5),
                 dpi=100)
    start,finish = entry_data()
    print(start)
    print(finish)
    entry_widget1.delete(0, END)
    entry_widget2.delete(0, END)
    a.vis_shortest_way(start,finish)






canvas_widget = Canvas(app, width=500, height=500)
canvas_widget.pack()



label_widget1 = Label(app, text="Enter start")
canvas_widget.create_window(150, 160, window=label_widget1)


label_widget2 = Label(app, text="Enter finish")
canvas_widget.create_window(150, 200, window=label_widget2)


entry_widget1 = Entry(app)
canvas_widget.create_window(300, 160, window=entry_widget1)


entry_widget2 = Entry(app)
canvas_widget.create_window(300, 200, window=entry_widget2)








plot_button = Button(master=app,
                     command=plot,
                     height=2,
                     width=10,
                     text="Plot")

# place the button
# in main window
plot_button.pack()

# run the gui
app.mainloop()
