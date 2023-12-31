import math
INF = math.inf
import copy

#IMPORTANT: nodes are indexed by numbers starting from zero, NOT names
#If nodes are not connetcted the weight is INF
#In case the graph is oriented the logic is: A[from_node][to_node]

class Graph():
	
	def __init__(self, matr, matr2 = None, func = None):
		self.iter = 0 #will count the number of iterations of every algorithm
		#takes the initialization matrix
		self.matr = matr
		self.size = len(self.matr)
		self.matr1 = self.matr
		self.matr2 = matr2
		#0 and 1 multipliers should be written, paramters are strictly x and y, do NOT write multiplication symbols
		self.kx = []
		self.ky = []
		if func:
			self.func = [k.strip() for k in func.split('+')]
			free = float(self.func.pop(-1))
			#print(self.func)
			for term in self.func:
				if term[1] == 'x':
					self.kx.append(float(term[0]))
				else:
					self.ky.append(float(term[0]))
					
			for i in range(self.size):
				for j in range(self.size):
					sumx = 0
					sumy = 0
					for k in range(len(self.kx)): sumx+=self.kx[k]*self.matr1[i][j]**(len(self.kx)-k) + free
					for k in range(len(self.ky)): sumy+=self.ky[k]*self.matr2[i][j]**(len(self.ky)-k) + free
					self.matr[i][j] = sumx + sumy
		#print(self.matr)
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
				self.iter+=1
				if self.matr[curr_node][next_node] + dist_from_start[curr_node] < dist_from_start[next_node]:
					dist_from_start[next_node] = self.matr[curr_node][next_node] + dist_from_start[curr_node]
					path_from_start[next_node] = path_from_start[curr_node] + [next_node]
			visited.append(curr_node)
			
			#choose next node to relax (curr_node)
			closest_dist = INF
			for candidate in range(self.size):
				self.iter+=1
				if candidate not in visited and dist_from_start[candidate] < closest_dist:
					closest_dist = dist_from_start[candidate]
					curr_node = candidate
			
			#check if route is possible
			if closest_dist == INF:
				self.iter = 0
				return "Route not possible"
		
		compl = self.iter
		self.iter = 0
		
		return (path_from_start[end], dist_from_start[end], compl)
	
	def FloydWarshall(self, start, end):
		
		DP = copy.deepcopy(self.matr)
		prev = [[None for j in range(self.size)] for i in range(self.size)] #for path reconstruction, previous[start][end] contains node previous to end on shortest start-end path
		for i in range(self.size):
			for j in range(self.size):
				if self.matr[i][j] != INF: prev[i][j] = i #still not sure if it works totally correct, but it even solves the paradox graph

		for k in range(1, self.size):
			for i in range(self.size):
				for j in range(self.size):
					self.iter+=1
					if DP[i][j] > DP[i][k] + DP[k][j]:
						DP[i][j] = DP[i][k] + DP[k][j]
						prev[i][j] = prev[k][j]
		
		#check if route is possible
		l = DP[start][end] #shortest path length
		if l == INF:
			self.iter = 0
			return "Route not possible"
		#reconstruct the path
		path = [end]
		j = end
		while j != start:
			path.append(prev[start][j])
			j = prev[start][j]
		path = path[::-1]
		
		compl = self.iter
		self.iter = 0
		
		return (path, l, compl)
	
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
					self.iter+=1
					if DP[edge[0]] + self.matr[edge[0]][edge[1]] < DP[edge[1]]:
						DP[edge[1]] = DP[edge[0]] + self.matr[edge[0]][edge[1]]
						path[edge[1]] = path[edge[0]] + [edge[1]]
					#review the edge in both ways
					if DP[edge[1]] + self.matr[edge[1]][edge[0]] < DP[edge[0]]:
						DP[edge[0]] = DP[edge[1]] + self.matr[edge[1]][edge[0]]
						path[edge[0]] = path[edge[1]] + [edge[0]]
					#if k == self.size - 1 and (edge[0] == end or edge[1] == end): break
		
		compl = self.iter
		self.iter = 0
		
		if DP[end] == INF: return "Route not possible"
		return (path[end], DP[end], compl)


