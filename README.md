# Navigator project

This project is aimed at creating an interactive visualizater of graphs and different ways of finding shortest paths in them.

## Userguide:

Run graph_example_of_work.py and enjoy, the program is interactive

## File description:

![Setup](setup.jpg)

### graph_construct.py

This file contains code that allows the user to enter the size and contents of the graph matrix, which he already transmits further along the line (see Fig.)

### graph_main.py

It focuses on algorithms for finding the shortest path between two nodes of a graph and the main Graph() class, which stores data on edges, nodes and edge weights. Dijkstra, Floyd-Marshall and Ford-Bellman algorithms are currently being used. At the output we have an array containing the nodes of the shortest path. This information is transferred to the following files (see Fig.)

### graph_visualisation.py

Using the "networkx" library, this file contains functions that visualize the graph itself and, accordingly, the shortest path between the selected two nodes. The functions are transferred to the final file (see Fig.)

### graph_exapmle_of_work.py

Finally, here, using the Tkinter library, a user interface is created that allows you to change graph properties and get graphs without restarting the program.
