import sys

class Graph:
    def __init__(self, edgeList):
        self.edges = []
        self.verts = []
        self.clock = 0
        self._addEdges(edgeList)
        self.verts.sort()
        self.preVisit = [0 for i in range(len(self.verts))]
        self.postVisit = [0 for i in range(len(self.verts))]
        self.colors = [False for i in range(len(self.verts))]
        self.visited = [0 for i in range(len(self.verts))]
        self.adj = [[] for i in range(len(self.verts))]
        for edge in self.edges:
            self.adj[edge[0]].append(edge[1])
            self.adj[edge[1]].append(edge[0])
        self.components = []
    
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
        for v in self.verts:
            if self.visited[v] == 0:
                self.components.append(v)
                bipartite = self.explore(v)
                if bipartite == False:
                    return False
        return True

    
    def __repr__(self):
        return (
        'EDGES {}\nVERTS {}\nADJ: {}\nVisited: {}\npre: {}\npost: {}\nColors: {}\n'.format(
            self.edges, self.verts, 
            self.adj, self.visited, 
            self.preVisit, self.postVisit, self.colors))


def getEdgeList(fil):
    f = open(fil, "r")
    edgeList = []

    while True:
        line = f.readline()
        line = line.replace(',', '')
        line = [int(x) for x in line.split()]
        if not line:
            break
        edgeList.append(line)

    f.close()
    return edgeList

def main():
    edges = getEdgeList(sys.argv[1])
    g = Graph(edges)
    
    if g.dfs():
        print("Is 2-colorable:")
        componentVerts = []
        colorVerts = []
        for i in range(len(g.components)):
            try:
                componentVerts.append(
                    g.verts[g.components[i]:g.components[i+1]])
            except IndexError:
                componentVerts.append(g.verts[g.components[i]:])
            try:
                colorVerts.append(
                    g.colors[g.components[i]:g.components[i+1]])
            except IndexError:
                colorVerts.append(g.colors[g.components[i]:])
            
        for i in range(len(componentVerts)):
            red = []
            blue = []
            for j in range(len(componentVerts[i])):
                if colorVerts[i][j] == False: 
                    red.append(str(componentVerts[i][j]))
                else:
                    blue.append(str(componentVerts[i][j]))
            
            print(', '.join(red))
            print(', '.join(blue))
    else:
        print("Is not 2-colorable.")
    

if __name__ == '__main__':
    main()
            
