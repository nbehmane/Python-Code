class Graph:
    def __init__(self, edgeList):
        self.edges = []
        self.verts = []
        self.clock = 0
        self._addEdges(edgeList)
        self.preVisit = [0 for i in range(len(self.verts))]
        self.postVisit = [0 for i in range(len(self.verts))]
        self.colors = [False for i in range(len(self.verts))]
        self.visited = [0 for i in range(len(self.verts))]
        self.adj = [[] for i in range(len(self.verts))]
        for edge in self.edges:
            self.adj[edge[0]].append(edge[1])
            self.adj[edge[1]].append(edge[0])
    
    def _addVerts(self, vert):
        self.verts.append(vert)
    
    def _addEdges(self, edgeList):
        for edge in edgeList:
            self.edges.append(edge)
            if edge[0] not in self.verts:
                self._addVerts(edge[0])
            if edge[1] not in self.verts:
                self._addVerts(edge[1])
    
    def explore(self, v):
        self.visited[v] = 1

        self.preVisit[v] = self.clock
        self.clock += 1

        for u in self.adj[v]:
            if self.visited[u] == 0:
                self.colors[u] = not self.colors[v]
                self.explore(u)
            if self.colors[u] == self.colors[v]:
                return False
        self.postVisit[v] = self.clock 
        self.clock += 1
        return True

    def dfs(self):
        components = []
        for v in self.verts:
            if self.visited[v] == 0:
                components.append(v)
                bipartite = self.explore(v)
                if bipartite == False:
                    print("NOT BIPARTITE")
                    return
        print("BIPARTITE")
    
    def __repr__(self):
        return (
        'EDGES {}\nVERTS {}\nADJ: {}\nVisited: {}\npre: {}\npost: {}\nColors: {}\n'.format(
            self.edges, self.verts, 
            self.adj, self.visited, 
            self.preVisit, self.postVisit, self.colors))


def main():
    edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5]]
    g = Graph(edges)
    print(g)
    print()
    g.dfs()
    print()
    print(g)

if __name__ == '__main__':
    main()
            
