class Graph:
    """
    Graph class represents a graph data structure with support for both directed and undirected graphs.

    Attributes:
        _vertices (list): A list of vertices in the graph.
        _adjMat (dict): An adjacency list representation of the graph.
        _directed (bool): A flag indicating whether the graph is directed.

    Methods:
        __init__(directed=False):
            Initializes the graph as directed or undirected.

        nVertices():
            Returns the number of vertices in the graph.

        nEdges():
            Returns the number of edges in the graph.

        addVertex(vertex):
            Adds a new vertex to the graph.

        validIndex(n):
            Checks if the given vertex index is valid.

        getVertex(n):
            Returns the vertex at the given index.

        addEdge(A, B):
            Adds an edge between two vertices A and B. Raises an error for self-loops.

        hasEdge(A, B):
            Checks if there is an edge between vertices A and B.

        vertices():
            Returns a range object representing all vertex indices.

        adjacentVertices(n):
            Returns an iterator over the vertices adjacent to the given vertex.

        adjacentUnvisitedVertices(n, visited, markVisits=True):
            Yields unvisited adjacent vertices of the given vertex.

        depthFirst(n):
            Performs a depth-first traversal starting from the given vertex.
            Yields tuples of the current vertex and the stack state.

        __str__():
            Returns a string representation of the graph.

        print(prefix=""):
            Prints the graph structure, including vertices and edges, with an optional prefix.
    """
    def __init__(self, directed=False):
        self._vertices = []
        self._adjMat = {}
        self._directed = directed

    def nVertices(self):
        return len(self._vertices)

    def nEdges(self):
        count = sum(len(neighbors) for neighbors in self._adjMat.values())
        return count if self._directed else count // 2

    def addVertex(self, vertex):
        idx = len(self._vertices)
        self._vertices.append(vertex)
        self._adjMat[idx] = set()

    def validIndex(self, n):
        if n < 0 or n >= self.nVertices():
            raise IndexError(f"Vertex index {n} out of bounds")
        return True

    def getVertex(self, n):
        if self.validIndex(n):
            return self._vertices[n]

    def addEdge(self, A, B):
        self.validIndex(A)
        self.validIndex(B)
        if A == B:
            raise ValueError("Self-loops are not allowed")
        self._adjMat[A].add(B)
        if not self._directed:
            self._adjMat[B].add(A)

    def hasEdge(self, A, B):
        self.validIndex(A)
        self.validIndex(B)
        return B in self._adjMat[A]

    def vertices(self):
        return range(self.nVertices())

    def adjacentVertices(self, n):
        self.validIndex(n)
        return iter(self._adjMat[n])

    def adjacentUnvisitedVertices(self, n, visited, markVisits=True):
        for j in self.adjacentVertices(n):
            if not visited[j]:
                if markVisits:
                    visited[j] = True
                yield j

    def depthFirst(self, n):
        self.validIndex(n)
        visited = [False] * self.nVertices()
        stack = Stack()
        stack.push(n)
        visited[n] = True
        yield (n, stack)
        while not stack.isEmpty():
            visit = stack.peek()
            adj = None
            for j in self.adjacentUnvisitedVertices(visit, visited):
                adj = j
                break
            if adj is not None:
                stack.push(adj)
                yield (adj, stack)
            else:
                stack.pop()

    def __str__(self):
        return f"<Graph with {self.nVertices()} vertices and {self.nEdges()} edges>"

    def print(self, prefix=""):
        print(f"{prefix}{self}")
        for vertex in self.vertices():
            print(f"{prefix}{vertex}: {self.getVertex(vertex).name}")
            for neighbor in self._adjMat[vertex]:
                print(
                    prefix,
                    self._vertices[vertex].name,
                    "->" if self._directed else "<->",
                    self._vertices[neighbor].name,
                )


class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        return self[-1]

    def isEmpty(self):
        return len(self) == 0


class Vertex:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# Creating an undirected graph for testing purpose
undirected_graph = Graph(directed=False)
vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for v in vertices:
    undirected_graph.addVertex(Vertex(v))
edges = ["AG", "AI", "CF", "DA", "DI", "HD", "HE", "HF", "HG", "IH", "JC", "JH"]
for edge in edges:
    A = ord(edge[0]) - ord("A")
    B = ord(edge[1]) - ord("A")
    undirected_graph.addEdge(A, B)

# Creating an directed graph for testing purpose
directed_graph = Graph(directed=True)
for v in vertices:
    directed_graph.addVertex(Vertex(v))
for edge in edges:
    A = ord(edge[0]) - ord("A")
    B = ord(edge[1]) - ord("A")
    directed_graph.addEdge(A, B)

# This will print both graphs
print("Undirected Graph:")
undirected_graph.print()
print("\nDirected Graph:")
directed_graph.print()

# Depth-first traversal from J for both graphs
print("\nDepth-first traversal from J in undirected graph:")
for vertex, path in undirected_graph.depthFirst(ord("J") - ord("A")):
    print(
        f"Vertex: {undirected_graph.getVertex(vertex)}, Path: {[undirected_graph.getVertex(v).name for v in path]}"
    )

print("\nDepth-first traversal from J in directed graph:")
for vertex, path in directed_graph.depthFirst(ord("J") - ord("A")):
    print(
        f"Vertex: {directed_graph.getVertex(vertex)}, Path: {[directed_graph.getVertex(v).name for v in path]}"
    )
