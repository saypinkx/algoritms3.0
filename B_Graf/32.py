import sys
sys.setrecursionlimit(100000000)
class Graph:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.flag = None

    def add_neighbour(self, obj):
        if obj not in self.neighbors:
            self.neighbors.append(obj)

    def dfs(self, is_visited=1):
        self.flag = is_visited
        # a.add(self.value)
        for neighbour in self.neighbors:
            if neighbour.flag is None:
                neighbour.dfs(is_visited=is_visited)
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

    # def deep_search(self):
    #     obj: Graph = self.list[1]
    #     obj.dfs()
    #     result = []
    #     for i in range(1, len(self.list)):
    #         obj = self.list[i]
    #         if obj.flag is not None:
    #             result.append(obj.value)
    #     return result

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


def deep_search(graphs: GraphList):
    is_visited = 0
    for i in range(1, len(graphs.list)):
        graph: Graph = graphs.list[i]
        if graph.flag is None:
            is_visited += 1
            graph.dfs(is_visited=is_visited)
    result = {}
    for j in range(1, len(graphs.list)):
        graph: Graph = graphs.list[j]
        if graph.flag not in result:
            result[graph.flag] = [graph.value]
        else:
            result[graph.flag].append(graph.value)
    return result

graphs = create_graph_list_txt()

res = deep_search(graphs)
print(len(res))
for node in res.keys():
    print(len(res[node]))
    print(*res[node])