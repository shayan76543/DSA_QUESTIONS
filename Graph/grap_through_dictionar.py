class Grap:
    def __init__(self,):
        self.adjlist={}
    def add_vertexs(self,vertexs):
        if vertexs not in self.adjlist:
            self.adjlist[vertexs]=[]
    def add_edges(self,src,dest):
        self.add_vertexs(src)
        self.add_vertexs(dest)
        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src)
    def print_graph(self):
        if self.adjlist:
            for vertexs in self.adjlist:
                print(vertexs ,"--->",self.adjlist[vertexs])
        else:
            print("graph is empty")
g=Grap()
g.add_edges(1,2)
g.add_edges(1,3)
g.add_edges(1,4)
g.add_edges(3,2)
g.print_graph()