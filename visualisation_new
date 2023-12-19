from pyvis.network import Network
from graph_main import Graph
import webbrowser
import math

INF = math.inf
net = Network('500px', '500px')

class PreparationForVisualization(Graph):
    def __init__(self, matr, nodes_titles):
        Graph.__init__(self, matr)
        uniq_nodes = []
        edges = self.edges
        for i in range(0, len(edges)):
            for j in range(0, 2):
                if edges[i][j] not in uniq_nodes:
                    uniq_nodes.append(edges[i][j])
        self.nodes = uniq_nodes
        self.nodes_titles = nodes_titles



    def Visualisation(self):
        net.add_nodes(self.nodes, label=self.nodes_titles)
        edges = self.edges
        for i in range(0, len(edges)):
            net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], physics=True)
        net.show_buttons(filter_='edges')

        net.repulsion(central_gravity=0, spring_length=200, spring_strength=0)
        net.show('visualisation.html')
        webbrowser.open_new('file:///Users/nikolajznamenskij/PycharmProjects/NAVIGATOR/visualisation.html')



    def VisualisationWithButtons(self):
        net.add_nodes(self.nodes, label=self.nodes_titles)
        edges = self.edges
        for i in range(0, len(edges)):
            net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], physics=True)
        net.show_buttons()

        net.repulsion(central_gravity=0, spring_length=200, spring_strength=0)
        net.show('visualisation.html')
        webbrowser.open_new('file:///Users/nikolajznamenskij/PycharmProjects/NAVIGATOR/visualisation.html')



    def VisualisationOfShortestWay(self, start, endt):
        way = Graph(self.matr).Dijkstra(start, endt)
        waynew = []

        length = len(way)
        for i in range(0, length - 1):
            waynew.append([way[i], way[i + 1]])

        for i in range(0, len(self.nodes)):
            if i == start or i == endt:
                net.add_node(i, label=self.nodes_titles[i], color='#FF0000')
            elif i in way:
                net.add_node(i, label=self.nodes_titles[i], color='#FFC0CB')
            else:
                net.add_node(i, label=self.nodes_titles[i])

        edges = self.edges
        for i in range(0, len(edges)):
            if [edges[i][0], edges[i][1]] in waynew:
                net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], color='#FF0000', physics=True)
            else:
                net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], color='a7f6f6', physics=True)


        net.repulsion(central_gravity=0, spring_length=200, spring_strength=0)
        net.show('visualisation.html')
        #webbrowser.open()#???
