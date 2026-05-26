class Graph:
    def __init__(self,vertexs):
        self.mat=[[0]*vertexs for i in range(vertexs)]
        self.vertexs=vertexs
        self.size=vertexs
    def add_edge(self,src,dest):
        if 0<=src<self.vertexs and 0<=dest<self.vertexs:
            self.mat[src][dest]=1
            self.mat[dest][src]=1
        else:
            print("Invalid Edge")
    def print_edge(self):  
        for row in self.mat:
            print(" ".join(map(str,row)))
                
    def DFS(self,src):
        visited=[0]*self.vertexs
        stack=[src]
        while(stack):
            v=stack.pop()
            if visited[v]==False:
                print(v,end="-->")
                visited[v]=True
            for i in range(self.size):
                if self.mat[v][i]==1 and visited[i]==False:
                    stack.append(i)
g=Graph(6)
g.add_edge(2,1)
g.add_edge(2,4)
g.add_edge(4,5)
g.print_edge()
g.DFS(1)