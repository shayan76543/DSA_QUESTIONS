from collections import deque
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
    def BFS(self,src):
        visited=[False]*self.vertexs
        queue=deque([src])
        while(queue):
            v=queue.popleft()
            if visited[v]==False:
                print(v,end=" ")
                visited[v]=True
            for i in range(self.size):
                if self.mat[v][i]==1 and visited[i]==False:
                    queue.append(i)
g=Graph(7)
g.add_edge(3,4)
g.add_edge(4,2)
g.add_edge(2,1)
g.add_edge(2,0)
g.add_edge(0,6)
g.add_edge(0,5)
g.BFS(3)

