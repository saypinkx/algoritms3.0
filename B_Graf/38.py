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
        self.prev = None

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

    def __str__(self):
        result = []
        node = self.head
        while node is not None:
            result.append(node)
            node = node.next

        result = list(map(lambda x: x.value.value, result))
        return str(result)


class QueueOBJ:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value.value)


def short_path(graph):
    queue = Queue()
    queue.push(QueueOBJ(graph))
    node = queue.head
    while node is not None:
        graph = node.value
        node.value.is_visited = 1
        for neigh in graph.neighbors:
            if neigh.is_visited == 0:
                neigh: Graph
                if neigh.dist == 0:
                    neigh.dist = graph.dist + 1
                    neigh.prev = graph
                    queue.push(QueueOBJ(neigh))
                else:
                    if neigh.dist > graph.dist + 1:
                        neigh.dist = graph.dist + 1
                        neigh.prev = graph
        node = node.next
        queue.pop()


# if graph1 == graph2:
#     print(0)
# elif graph2.dist == 0:
#     print(-1)
# else:
#     print(graph2.dist)
#     node: Graph = graph2
#     while node is not None:
#         result.append(node.value)
#         node = node.prev
#     print(result[::-1])

def create_matrix_graph(n, m):
    matrix = []
    k = 1
    graph = GraphList(n * m)
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(k)
            k += 1
    for i in range(n):
        for j in range(m):
            ver: Graph = graph.list[matrix[i][j]]
            paths = [(i - 2, j + 1), (i - 2, j - 1), (i + 2, j + 1), (i + 2, j - 1), (i + 1, j + 2), (i + 1, j - 2),
                     (i - 1, j + 2), (i - 1, j - 2)]
            for x, y in paths:
                if x >= 0 and y >= 0 and x < n and y < m:
                    ver_value = matrix[x][y]
                    neigh = graph.list[ver_value]
                    ver.add_neighbour(neigh)
                    neigh.add_neighbour(ver)

    return graph, matrix


def find_min_path(q, graph: GraphList, matrix, end_ver):
    min_path = 0
    for i in range(q):
        x, y = input().split()
        x, y = int(x), int(y)
        ver = graph.list[matrix[x - 1][y - 1]]
        if ver != end_ver and ver.dist == 0:
            return False
        else:
            min_path += ver.dist
    return min_path


n, m, s, t, q = list(map(lambda x: int(x), input().split()))
graph, matrix = create_matrix_graph(n, m)
end_ver = graph.list[matrix[s - 1][t - 1]]
short_path(end_ver)
result = find_min_path(q, graph, matrix, end_ver)
if result == False:
    print('-1')
else:
    print(result)
