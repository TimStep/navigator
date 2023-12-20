import math
import copy
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

paradox_graph = [
                  [0, 8, 5],
                  [8, 0, 2],
                  [5, 2, 0]]
#the paradox is that the edge 0-1 is not the shortest 0-1 path

class Graph():
	
	def __init__(self, matr):
		#takes the initialization matrix
		self.matr = matr
		self.size = len(self.matr)
		self.edges = []
		for node1 in range(self.size):
			for node2 in range(self.size):
				 if node1 != node2 and self.matr[node1][node2] != INF and True not in [(node2, node1, self.matr[node2][node1])  in self.edges]:
				 	self.edges.append((node1, node2, self.matr[node1][node2]))
		
	def Dijkstra(self, start, end):
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
	
	def FloydWarshall(self, start, end):
		
		# DP = self.matr
		DP = copy.deepcopy(self.matr)
		prev = [[None for j in range(self.size)] for i in range(self.size)] #for path reconstruction, previous[start][end] contains node previous to end on shortest start-end path
		for i in range(self.size):
			for j in range(self.size):
				if self.matr[i][j] != INF: prev[i][j] = i #still not sure if it works totally correct, but it even solves the paradox graph

		for k in range(1, self.size):
			for i in range(self.size):
				for j in range(self.size):
					print(k, i, j)
					if DP[i][j] > DP[i][k] + DP[k][j]:
						DP[i][j] = DP[i][k] + DP[k][j]
						prev[i][j] = prev[k][j]
		
		#check if route is possible
		l = DP[start][end] #shortest path length
		if l == INF: return "Route not possible"
		#reconstruct the path
		path = [end]
		j = end
		while j != start:
			path.append(prev[start][j])
			j = prev[start][j]
		path = path[::-1]
		
		return (l, path)
	
	def FordBellman(self, start, end):
		
		DP = [INF for i in range(self.size)]
		DP[start] = 0

		path = [[] for i in range(self.size)]
		path[start] = [start]
		
		#iterating by edges, faster if the graph in not dense
		if len(self.edges) < self.size**2 or True: #!!!remove "or True" when iterating by nodes variant will be done
			#print('not dense')
			for k in range(1, self.size):
				for edge in self.edges:
					if DP[edge[0]] + self.matr[edge[0]][edge[1]] < DP[edge[1]]:
						DP[edge[1]] = DP[edge[0]] + self.matr[edge[0]][edge[1]]
						path[edge[1]] = path[edge[0]] + [edge[1]]
					#review the edge in both ways
					if DP[edge[1]] + self.matr[edge[1]][edge[0]] < DP[edge[0]]:
						DP[edge[0]] = DP[edge[1]] + self.matr[edge[1]][edge[0]]
						path[edge[0]] = path[edge[1]] + [edge[0]]
					if k == self.size - 1 and (edge[0] == end or edge[1] == end): break
		'''
		else: #by nodes, if graph is dense
			for k in range(1, self.size):
				for i in range()
		'''
		if DP[end] == INF: return "Route not possible"
		return path[end]
	
g = Graph(paradox_graph)
print(g.edges)
print(g.matr)
print('Dijkstra')
print("Shortest path from node 2 to node 4: " + '->'.join(str(node) for node in g.Dijkstra(0, 1)))

print('Floyd-Warshall')
res = g.FloydWarshall(0, 1)
print("Shortest path from node 2 to node 4: " + '->'.join(str(node) for node in res[1]))
print("Length: " + str(res[0]))
print(g.edges)
print(g.matr)

print("Ford-Bellman")
print("Shortest path from node 2 to node 4: " + '->'.join(str(node) for node in g.FordBellman(0, 1)))
