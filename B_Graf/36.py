import sys

sys.setrecursionlimit(500000)


class Graph:
    mass = []

    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.flag = 0
        self.color = None
        self.result = False
        self.is_visited = 0
        self.dist = 0

    def add_neighbour(self, obj):
        if obj not in self.neighbors:
            self.neighbors.append(obj)

    def dfs_color(self, is_visited=1, color=1):
        self.flag = is_visited
        self.color = color
        for neighbour in self.neighbors:
            if neighbour.flag is None:
                neighbour.dfs_color(is_visited=is_visited, color=3 - color)
            if self.color == neighbour.color:
                self.result = False

    def dfs_for_sort(self, is_visited=1):
        self.is_visited = is_visited
        for neighbour in self.neighbors:
            neighbour: Graph
            if neighbour.is_visited == 0:
                neighbour.dfs_for_sort(is_visited)
        Graph.mass.append(self.value)

    def __str__(self):
        return str(self.value)

    def cat_neig(self):
        return str(self.neighbors)

    def __eq__(self, other):
        if type(other) == Graph:
            if self.value == other.value:
                return True
            return False
        else:
            return False

    def __hash__(self):
        return hash(self.value)


class GraphList:
    def __init__(self, n):
        self.list = [0] * (n + 1)
        for i in range(1, n + 1):
            self.add_graph(Graph(i))

    def add_graph(self, obj):
        self.list[obj.value] = obj

    def __str__(self):
        result = list(map(lambda x: x.value if x != 0 else 0, self.list))
        return str(result[1::])


def write_dist(graph: Graph, dist=0):
    graph.is_visited = 1
    if graph.dist == 0:
        graph.dist = dist
    else:
        if dist < graph.dist:
            graph.dist = dist
    for node in graph.neighbors:
        node: Graph
        if node.is_visited == 0 or node.dist > dist + 1:
            dist += 1
            write_dist(node, dist=dist)


def create_graph_matrix():
    n = int(input())
    graphs = GraphList(n)
    for i in range(n):
        string = str(input()).split()
        graph1: Graph = graphs.list[i + 1]
        for j in range(len(string)):
            if int(string[j]) == 1:
                graph2 = graphs.list[j + 1]
                graph1.add_neighbour(graph2)
                graph2.add_neighbour(graph1)
    return graphs


class Queue:
    def __init__(self):
        self.head = None

    def push(self, node):
        if self.head is None:
            self.head = node
        else:
            old_node = self.head
            while old_node.next is not None:
                old_node = old_node.next
            old_node.next = node

    def pop(self):
        old_node = self.head.next
        self.head = old_node


class QueueOBJ:
    def __init__(self, value):
        self.value = value
        self.next = None


queue = Queue()
grahlist = create_graph_matrix()
v1, v2 = list(map(lambda x: int(x), input().split()))
graph1, graph2 = grahlist.list[v1], grahlist.list[v2]

queue.push(QueueOBJ(graph1))

node = queue.head
result = []
while node is not None:
    graph = node.value
    node.value.is_visited = 1
    for neigh in graph.neighbors:
        if neigh.is_visited == 0:
            neigh: Graph
            if neigh.dist == 0:
                neigh.dist = graph.dist + 1
            else:
                neigh.dist = min(neigh.dist, graph.dist + 1)
            queue.push(QueueOBJ(neigh))
    node = node.next
    queue.pop()

if graph1 == graph2:
    print(0)
elif graph2.dist == 0:
    print(-1)
else:
    print(graph2.dist)
