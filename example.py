test_graph = [
    [0, 1, 1, 1, INF],
    [1, 0, INF, 1, 1],
    [1, INF, 0, 1, INF],
    [1, 1, 1, 0, 1],
    [INF, 1, INF, 1, 0]]

graph = PreparationForVisualization(test_graph, ['A', 'B', "C", "D", "F"])
#graph.Visualisation()
graph.VisualisationOfShortestWay(1, 4)
