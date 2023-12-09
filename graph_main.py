import math
INF = math.inf

#IMPORTANT: nodes are indexed by numbers starting from zero, NOT names
#If nodes are not connetcted the weight is INF
#In case the graph is oriented the logic is: A[from_node][to_node]
test_graph = [
             [0, 1, 1, 1, INF],
             [1, 0, INF, 1, 1], 
             [1, INF, 0, 1, INF], 
             [1, 1, 1, 0, 1], 
             [INF, 1, INF, 1, 0]]
#test graph: https://u.foxford.ngcdn.ru/uploads/tinymce_image/image/1959/1.png

class Graph():
	
	def __init__(self, matr):
		#takes the initialization matrix
		self.matr = matr
		self.size = len(self.matr)
		#self.edges = 
		
	def dijkstra(self, start, end):
		#array of distances from the start node to other nodes
		dist_from_start = [INF]*self.size
		dist_from_start[start] = 0
		
		#remembers the path to each node as arrays
		path_from_start = [[] for i in range(self.size)]
		path_from_start[start] = [start]
		#list of visited nodes, non-ordered
		visited = []
		
		curr_node = start
		
		while curr_node != end:
			
			#node relaxation
			for next_node in range(self.size):
				if self.matr[curr_node][next_node] + dist_from_start[curr_node] < dist_from_start[next_node]:
					dist_from_start[next_node] = self.matr[curr_node][next_node] + dist_from_start[curr_node]
					path_from_start[next_node] = path_from_start[curr_node] + [next_node]
			visited.append(curr_node)
			
			#choose next node to relax (curr_node)
			closest_dist = INF
			for candidate in range(self.size):
				if candidate not in visited and dist_from_start[candidate] < closest_dist:
					closest_dist = dist_from_start[candidate]
					curr_node = candidate
			
			#check if route is possible
			if closest_dist == INF: return "Route not possible"
		
		return path_from_start[end]

g = Graph(test_graph)
#print(g.dijkstra(3, 4))
#print(g.dijkstra(4, 5))
print("Shortest path from node 2 to node 4: " + '->'.join(str(node) for node in g.dijkstra(2, 4)))
