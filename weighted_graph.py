import math


class WeightedGraph(object):
    """WeightedGraph is a class that represents a weighted, undirected graph. It provides methods to add vertices and edges,
    retrieve edge weights, and compute shortest paths using the Floyd-Warshall algorithm.
    Attributes:
        _vertices (list): A list of vertex names in the graph.
        _adjMat (dict): A dictionary that maps vertex pairs (tuples) to their edge weights.
    Methods:
        __init__():
            Initializes an empty graph with no vertices or edges.
        nVertices():
            Returns the number of vertices in the graph.
        validIndex(n):
            Checks if the given vertex index is valid. Raises a ValueError if the index is invalid.
        addVertex(name):
            Adds a vertex with the given name to the graph and returns its index.
        addEdge(A, B, w):
            Adds an edge of weight `w` between two vertices `A` and `B`. Raises a ValueError if the indices are invalid
            or if an edge to itself is attempted.
        edgeWeight(A, B):
            Returns the weight of the edge between vertices `A` and `B`. If no edge exists, returns infinity.
        allShortestPathsMatrix():
            Computes the all-pairs shortest paths matrix using the Floyd-Warshall algorithm. Returns a dictionary
            representing the minimum costs between any two vertices, indexed as (i, j) pairs.
        getVertex(index):
            Returns the name of the vertex at the given index. Raises a ValueError if the index is invalid.
    """

    def __init__(self):
        self._vertices = []
        self._adjMat = {}

    def nVertices(self):
        """Return the number of vertices in the graph."""
        return len(self._vertices)

    def validIndex(self, n):
        """Check if vertex index n is valid."""
        if n < 0 or n >= self.nVertices():
            raise ValueError("Invalid vertex index")

    def addVertex(self, name):
        """Add a vertex with the given name to the graph."""
        self._vertices.append(name)
        return len(self._vertices) - 1  # Return the vertex index

    def addEdge(self, A, B, w):
        """Add edge of weight w between two vertices A & B."""
        self.validIndex(A)
        self.validIndex(B)
        if A == B:
            raise ValueError("Cannot create edge to self")
        self._adjMat[A, B] = w
        self._adjMat[B, A] = w

    def edgeWeight(self, A, B):
        """Get edge weight between vertices A and B."""
        self.validIndex(A)
        self.validIndex(B)
        return self._adjMat.get((A, B), math.inf)

    def allShortestPathsMatrix(self):
        """
        Compute the all-pairs shortest paths matrix using Floyd-Warshall algorithm.
        Returns a dictionary of minimum costs between any two vertices.
        The dictionary is indexed like the _adjMat attribute (as (i,j) pairs).
        """
        nVerts = self.nVertices()
        dist = {}

        # Initialize distance matrix
        for i in range(nVerts):
            for j in range(nVerts):
                if i == j:
                    dist[i, j] = 0  # Distance to self is 0
                else:
                    dist[i, j] = self.edgeWeight(i, j)  # Direct edge weight or infinity

        # Floyd-Warshall algorithm
        for k in range(nVerts):
            for i in range(nVerts):
                for j in range(nVerts):
                    if dist[i, j] > dist[i, k] + dist[k, j]:
                        dist[i, j] = dist[i, k] + dist[k, j]

        return dist

    def getVertex(self, index):
        """Get vertex name by index."""
        self.validIndex(index)
        return self._vertices[index]


# Create the graph from the screenshot
train_graph = WeightedGraph()

# Add stations (vertices)
stations = ["Leo", "Kamal", "Joe", "Naur", "Dahl", "Kay"]
station_indices = {}
for station in stations:
    station_indices[station] = train_graph.addVertex(station)

# Add connections (edges) with travel times
connections = [
    ("Leo", "Kamal", 28),
    ("Leo", "Joe", 24),
    ("Kamal", "Joe", 51),
    ("Kamal", "Naur", 17),
    ("Joe", "Naur", 26),
    ("Joe", "Dahl", 29),
    ("Naur", "Dahl", 11),
    ("Naur", "Kay", 20),
    ("Dahl", "Kay", 19),
]

for a, b, time in connections:
    train_graph.addEdge(station_indices[a], station_indices[b], time)

# Compute all shortest paths
shortest_paths = train_graph.allShortestPathsMatrix()

# Display results in a readable format
print("All shortest paths between stations (in minutes):")
print("From\\To", end="\t")
for i in range(len(stations)):
    print(stations[i][:4], end="\t")
print()

for i in range(len(stations)):
    print(stations[i][:4], end="\t")
    for j in range(len(stations)):
        time = shortest_paths[i, j]
        print(f"{time if time != math.inf else '-'}", end="\t")
    print()
