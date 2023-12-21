from pyvis.network import Network
from graph_main import Graph
import webbrowser
import math

INF = math.inf
net = Network('600px', '600px')

class PreparationForVisualization(Graph):
    def __init__(self, matr, type, function=None):
        Graph.__init__(self, matr, type)
        if function:
            self.function = function
        self.type = type
        if self.type == 'graph matrix':
            uniq_nodes = []
            edges = self.edges
            self.nodes = [i for i in range(0, max(len(matr), len(matr[1])))]
        if self.type == 'massive of edges':
            edges = []
            uniq_nodes = []
            matr = matr.split()
            for i in range(0, len(matr)):
                matr[i] = str(matr[i]).split(",")



            for i in range(0, len(matr)):
                if matr[i][0] not in uniq_nodes:
                    uniq_nodes.append(matr[i][0])
                if matr[i][1] not in uniq_nodes:
                    uniq_nodes.append(matr[i][1])
            self.nodes = uniq_nodes
            for i in range(0, len(matr)):
                edges.append((matr[i][0], matr[i][1], matr[i][2]))
            self.edges = edges
            matr1 = [[INF for j in uniq_nodes] for i in uniq_nodes]
            for i in range(0, len(edges)):
                matr1[int(edges[i][0]) - 1][int(edges[i][1]) - 1] = int(edges[i][2])
            self.matr = matr1




    def Visualisation(self):
        net.add_nodes(self.nodes)
        edges = self.edges
        for i in range(0, len(edges)):
            net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], physics=True)
        net.show_buttons(filter_='edges')

        net.set_options('''const options = {
  "configure": {
    "enabled": true
    },
  "nodes": {
    "borderWidth": null,
    "borderWidthSelected": null,
    "opacity": null,
    "size": null
  },
  "edges": {
    "color": {
      "inherit": true
    },
    "selfReferenceSize": null,
    "selfReference": {
      "angle": 0.7853981633974483
    },
    "smooth": false
  },
  "physics": {
    "repulsion": {
      "centralGravity": 0,
      "springConstant": 0
    },
    "minVelocity": 0.75,
    "solver": "repulsion"
  }
}
    ''')
        net.show('visualisation.html')
        webbrowser.open_new('file:///Users/nikolajznamenskij/PycharmProjects/NAVIGATOR/visualisation.html')



    def VisualisationWithButtons(self):
        net.add_nodes(self.nodes)
        edges = self.edges
        for i in range(0, len(edges)):
            net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], physics=True)
        net.show_buttons()
        net.show('visualisation.html')
        webbrowser.open_new('file:///Users/nikolajznamenskij/PycharmProjects/NAVIGATOR/visualisation.html')



    def VisualisationOfShortestWayD(self, start, endt):
        if True:
            way = Graph(self.matr, self.type).Dijkstra(start, endt)
            way1 = way[0]
            waynew = []

            length = len(way1)
            for i in range(0, length - 1):
                waynew.append([way1[i], way1[i + 1]])
            print(waynew)
            net.set_options('''const options = {
                  "configure": {
                    "enabled": false
                    },
                  "nodes": {
                    "borderWidth": null,
                    "borderWidthSelected": null,
                    "size": 10
                  },
                  "edges": {
                    "selfReference": {
                      "angle": 0.7853981633974483
                    },
                    "smooth": false
                  },
                  "physics": {
                    "repulsion": {
                      "centralGravity": 0,
                      "springConstant": 0
                    },
                    "minVelocity": 0.75,
                    "solver": "repulsion"
                  }
                }
                    ''')


            for i in range(0, len(self.nodes)):
                if self.nodes[i] == start or self.nodes[i] == endt:
                    net.add_node(self.nodes[i], label=str(self.nodes[i]), color='#FF0000')
                elif self.nodes[i] in way1:
                    net.add_node(self.nodes[i], label=str(self.nodes[i]), color='#FFC0CB')
                else:
                    net.add_node(self.nodes[i], label=str(self.nodes[i]))



            edges = self.edges
            for i in range(0, len(edges)):
                if [edges[i][0], edges[i][1]] in waynew or [edges[i][1], edges[i][0]] in waynew:
                    net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], color='#FF0000', physics=True)
                else:
                    net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], color='a7f6f6', physics=True)
                    2
        net.show('visualisation.html')
        webbrowser.open('file:///Users/nikolajznamenskij/PycharmProjects/NAVIGATOR/visualisation.html')




    def VisualisationOfShortestWayFW(self, start, endt):
        if True:
                way = Graph(self.matr, self.type).FloydWarshall(start, endt)
                way1 = way[0]
                waynew = []

                length = len(way1)
                for i in range(0, length - 1):
                    waynew.append([way1[i], way1[i + 1]])
                print(waynew)
                net.set_options('''const options = {
                      "configure": {
                        "enabled": false
                        },
                      "nodes": {
                        "borderWidth": null,
                        "borderWidthSelected": null,
                        "size": 10
                      },
                      "edges": {
                        "selfReference": {
                          "angle": 0.7853981633974483
                        },
                        "smooth": false
                      },
                      "physics": {
                        "repulsion": {
                          "centralGravity": 0,
                          "springConstant": 0
                        },
                        "minVelocity": 0.75,
                        "solver": "repulsion"
                      }
                    }
                        ''')

                for i in range(0, len(self.nodes)):
                    if self.nodes[i] == start or self.nodes[i] == endt:
                        net.add_node(self.nodes[i], label=str(self.nodes[i]), color='#FF0000')
                    elif self.nodes[i] in way1:
                        net.add_node(self.nodes[i], label=str(self.nodes[i]), color='#FFC0CB')
                    else:
                        net.add_node(self.nodes[i], label=str(self.nodes[i]))

                edges = self.edges
                for i in range(0, len(edges)):
                    if [edges[i][0], edges[i][1]] in waynew or [edges[i][1], edges[i][0]] in waynew:
                        net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], color='#FF0000', physics=True)
                    else:
                        net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], color='a7f6f6', physics=True)
        net.show('visualisation.html')
        webbrowser.open('file:///Users/nikolajznamenskij/PycharmProjects/NAVIGATOR/visualisation.html')


    def VisualisationOfShortestWayFB(self, start, endt):
        if True:
                    way = Graph(self.matr, self.type).FordBellman(start, endt)
                    way1 = way[0]
                    waynew = []

                    length = len(way1)
                    for i in range(0, length - 1):
                        waynew.append([way1[i], way1[i + 1]])
                    print(waynew)
                    net.set_options('''const options = {
                          "configure": {
                            "enabled": false
                            },
                          "nodes": {
                            "borderWidth": null,
                            "borderWidthSelected": null,
                            "size": 10
                          },
                          "edges": {
                            "selfReference": {
                              "angle": 0.7853981633974483
                            },
                            "smooth": false
                          },
                          "physics": {
                            "repulsion": {
                              "centralGravity": 0,
                              "springConstant": 0
                            },
                            "minVelocity": 0.75,
                            "solver": "repulsion"
                          }
                        }
                            ''')

                    for i in range(0, len(self.nodes)):
                        if self.nodes[i] == start or self.nodes[i] == endt:
                            net.add_node(self.nodes[i], label=str(self.nodes[i]), color='#FF0000')
                        elif self.nodes[i] in way1:
                            net.add_node(self.nodes[i], label=str(self.nodes[i]), color='#FFC0CB')
                        else:
                            net.add_node(self.nodes[i], label=str(self.nodes[i]))

                    edges = self.edges
                    for i in range(0, len(edges)):
                        if [edges[i][0], edges[i][1]] in waynew or [edges[i][1], edges[i][0]] in waynew:
                            net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], color='#FF0000', physics=True)
                        else:
                            net.add_edge(edges[i][0], edges[i][1], value=edges[i][2], color='a7f6f6', physics=True)

        net.show('visualisation.html')
        webbrowser.open('file:///Users/nikolajznamenskij/PycharmProjects/NAVIGATOR/visualisation.html')


#g = '1,2,4 2,3,5 4,5,6'

