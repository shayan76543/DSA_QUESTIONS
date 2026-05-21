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
    def dfs(self,src):
        visited=[False]*self.size
        stack=[src]
        while(stack):
            v=stack.pop()
            if visited[v]==False:
                print(v,end="-->")
                visited[v]=True
            for i in range(self.size):
                if self.mat[v][i]==1 and visited[i]==False:
                    stack.append(i)
G=Graph(6)
G.add_edge(1,0)
G.add_edge(0,2)
G.add_edge(2,3)
G.add_edge(3,5)
G.add_edge(5,4)
G.add_edge(2,4)
G.print_mat()
G.dfs(0)
