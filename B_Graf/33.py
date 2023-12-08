class Graph:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.flag = None
        self.color = None
        self.result = True

    def add_neighbour(self, obj):
        if obj not in self.neighbors:
            self.neighbors.append(obj)

    def dfs_color(self, is_visited=1, color=1, signal=True):
        self.flag = is_visited
        self.color = color
        for neighbour in self.neighbors:
            if neighbour.flag is None:
                neighbour.dfs_color(is_visited=is_visited, color=3 - color)
            if self.color == neighbour.color:
                self.result = False

        # return a

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
        graph2.add_neighbour(graph1)
    return graphs


def create_graph_list_txt():
    with open('16.txt', 'r') as file:
        n, m = file.readline().split()
        n, m = int(n), int(m)
        graphs = GraphList(n)
        for i in range(m):
            v1, v2 = file.readline().split()
            v1, v2 = int(v1), int(v2)
            graph1, graph2 = graphs.list[v1], graphs.list[v2]
            graph1.add_neighbour(graph2)
            graph2.add_neighbour(graph1)
        return graphs






graphs = create_graph_list()


def result(graphs):
    for i in range(1, len(graphs.list)):
        graph: Graph = graphs.list[i]
        if graph.flag is None:
            res = graph.dfs_color()
            if graph.result == False:
                return False
    return True


if result(graphs) == True:
    print('YES')
else:
    print('NO')
