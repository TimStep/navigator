import networkx as nx
import matplotlib.pyplot as plt
from graph_main import Graph
import math



inf = math.inf

class Visualisate():
    def __init__(self,matr):
        self.edges_rev=[]
        self.matr = matr
        self.size = len(self.matr)

        for node1 in range(self.size):
            for node2 in range(self.size):
                if node1 != node2 and self.matr[node1][node2] != inf:
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

    def vis_shortest_way_FB(self,start,final):

        g=Graph(self.matr)
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
    def vis_shortest_way_D(self,start,final):

        g=Graph(self.matr)
        res= g.Dijkstra(start, final)
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
        title = 'shortest way with D algoritm'
        plt.title(title)
        plt.show()
    def vis_shortest_way_FW(self,start,final):

        g=Graph(self.matr)
        res= g.FloydWarshall(start, final)[1]
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
        title='shortest way with FW algoritm'
        plt.title(title)
        plt.show()



