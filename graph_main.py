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
'''
[
[0,    1,    2,       3,  None],
[0,    1,    None,    3,  4],
[0,    None, 2,       3,  None],
[0,    1,    2,       3,  4],
[None, 1,    None,    3,  4]]
'''
#test graph: https://u.foxford.ngcdn.ru/uploads/tinymce_image/image/1959/1.png

class Graph():
	
	def __init__(self, matr):
		#takes the initialization matrix
		self.matr = matr
		self.size = len(self.matr)
		#self.edges = 
		
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
		
		#DP = [ [ [INF for j in range(self.size)] for i in range(self.size)] for k in range(self.size+1)]
		DP = self.matr
		prev = [[None for j in range(self.size)] for i in range(self.size)] #for path reconstruction, previous[start][end] contains node previous to end on shortest start-end path
		for i in range(self.size):
			for j in range(self.size):
				if self.matr[i][j] != INF: prev[i][j] = i

		for k in range(1, self.size):
			for i in range(self.size):
				for j in range(self.size):
					if DP[i][j] > DP[i][k] + DP[k][j]:
						DP[i][j] = DP[i][k] + DP[k][j]
						prev[i][j] = prev[k][j]
		
		#print(DP)
		#print(prev)
		#check if route is possible
		l = DP[start][end] #shortest path length
		if l == INF: return "Route not possible"
		#reconstruct the path
		path = [end]
		j = end
		while j != start:
			#print(j)
			path.append(prev[start][j])
			j = prev[start][j]
		path = path[::-1]
		
		return (l, path)
		
g = Graph(test_graph)
#print(g.dijkstra(3, 4))
#print(g.dijkstra(4, 5))
print('Dijkstra')
print("Shortest path from node 2 to node 4: " + '->'.join(str(node) for node in g.Dijkstra(2, 4)))
print('Floyd-Warshall')
res = g.FloydWarshall(2, 4)
print("Shortest path from node 2 to node 4: " + '->'.join(str(node) for node in res[1]))
print("Length: " + str(res[0]))
