class Graph():

	def __init__(self, n):
		# membuat adjacency matriks yang merepsentasikan graph yang terdiri dari n node 
		self.num_of_nodes = n
		self.adj_matrix = [[0 for i in range(n)] for j in range(n)]


	def next(self, visited):
		temp = -10
		min_dist = float("inf")
		for i in range (self.num_of_nodes):
			if (visited[i][0] == 0) and (visited[i][1] < min_dist):
				temp = i
				min_dist = visited[i][1]
		
		return temp
	
	def connection(self, index):
		temp = []
		for i in range (self.num_of_nodes):
			if(self.adj_matrix[index][i] > 0):
				# temp.append(chr(ord("a") + i))
				temp.append(i)
		return temp

	def transpose(self, tr):
		for i in range(self.num_of_nodes):
			for j in range(self.num_of_nodes):
				tr[i][j] = self.adj_matrix[j][i]
  

	def isSymmetric(self):
		
		tr = [[0 for j in range(self.num_of_nodes)] for i in range(self.num_of_nodes) ]
		self.transpose(tr)
		for i in range(self.num_of_nodes):
			for j in range(self.num_of_nodes):
				if (self.adj_matrix[i][j] != tr[i][j]):
					return False
		return True

	def Dijkstra(self, src = "A", dst = "A"):
		solution = []
		
		src_name = ord(src)
		# node, distance, from
		visited = []
		step = []
		
		for i in range (self.num_of_nodes ):
			curr_distance = float("inf")
			if (i == (src_name - ord("A"))):
				curr_distance = 0
			visited.append([0, curr_distance,[chr(src_name)]])

		
		for i in range(self.num_of_nodes):
			if ( i == 0) : next = ord(src) - ord("A")			
			else : next = self.next(visited)
			# print(visited)
			step.append(chr(next + ord("A")))

			solution = self.connection(next)
			# print(chr(src_name + next - 1), visited[next][1])
			# print(solution)
			for node_tetangga in  (solution):
				if visited[node_tetangga][0] == 0:
					# print(chr(ord("a") + next ),  chr(ord("a") + j))
					new_distance = visited[next][1] + self.adj_matrix[next][node_tetangga]

					if visited[node_tetangga][1] > new_distance:
					
						visited[node_tetangga][1] = new_distance
						visited[node_tetangga][2] = list(visited[next][2])
						# visited[node_tetangga][2].append(chr(ord("a") + next))
						visited[node_tetangga][2].append(chr(ord("A") + node_tetangga))
						# visited[node_tetangga][2].append(chr(src_name + node_tetangga))
		
			visited[next][0] = 1

		
		
		# self.printSolution(visited)
		return(visited[ord(dst) - ord("A")][1], visited[ord(dst) - ord("A")][2], step)
		
		
if __name__=="__main__":
	test = Graph(9)
	test.adj_matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
			[4, 0, 8, 0, 0, 0, 0, 11, 0],
			[0, 8, 0, 7, 0, 4, 0, 0, 2],
			[0, 0, 7, 0, 9, 14, 0, 0, 0],
			[0, 0, 0, 9, 0, 10, 0, 0, 0],
			[0, 0, 4, 14, 10, 0, 2, 0, 0],
			[0, 0, 0, 0, 0, 2, 0, 1, 6],
			[8, 11, 0, 0, 0, 0, 1, 0, 7],
			[0, 0, 2, 0, 0, 0, 6, 7, 0]
			]

	if (test.isSymmetric()):
		print("tes")			
	x = test.Dijkstra("C", "B")
	print(x)