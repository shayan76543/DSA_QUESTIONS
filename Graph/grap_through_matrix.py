class Graph:
    def __init__(self,vertexs):
        self.mat=[[0]*vertexs for i in range(vertexs)]
        self.vertexs=vertexs
        self.size=vertexs
    def add_edge(self,src,dist):
        if 0<=src<self.size and 0<=dist<self.size:
            self.mat[src][dist]=1
            self.mat[dist][src]=1
        else:
            print("Invalid edge")
    def print_mat(self):
        for row in self.mat:
            print(" ".join(map(str,row)))
G=Graph(6)
G.add_edge(3,3)
G.add_edge(1,2)
G.add_edge(4,3)
G.add_edge(3,2)
G.add_edge(2,2)
G.add_edge(1,1)
G.add_edge(2,3)
G.add_edge(0,3)
G.print_mat()
