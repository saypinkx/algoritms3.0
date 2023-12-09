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


def create_graph_list():
    n, m = list(map(lambda x: int(x), input().split()))
    graphs = GraphList(n)
    for i in range(m):
        v1, v2 = list(map(lambda x: int(x), input().split()))
        graph1, graph2 = graphs.list[v1], graphs.list[v2]
        graph1.add_neighbour(graph2)
    return graphs


graphs = create_graph_list()

result = False
mass = []
start = None


def dfs_is_cycle(graph: Graph, last=None):
    global result
    global mass
    global start
    graph.flag = 1
    for neigh in graph.neighbors:
        if neigh.flag == 0:
            res = dfs_is_cycle(neigh, last=graph)
            if res:
                if graph.value != start:
                    mass.append(graph.value)
                    return True
        elif neigh.flag == 1 and last != neigh:
            if start is None:
                result = True
                mass.append(graph.value)
                start = neigh.value
                graph.flag = 2
                return True
    graph.flag = 2


def res():
    global result
    for i in range(1, len(graphs.list)):
        graph: Graph = graphs.list[i]
        if graph.flag == 0:
            dfs_is_cycle(graph)
    return result


ress = res()

if ress:
    print('-1')


else:
    is_vis = 1
    for i in range(1, len(graphs.list)):
        graph: Graph = graphs.list[i]
        if graph.is_visited == 0:
            graph.dfs_for_sort(is_vis)
            is_vis += 1
    print(*Graph.mass[::-1])
