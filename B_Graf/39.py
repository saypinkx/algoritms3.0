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


def create_graf_3d(n):
    graph = GraphList(n * n * n)
    matrix = []
    for i in range(n):
        line = input()
        for j in range(n):
            line = input()
            result = []
            for x in line:
                result.append(x)
            matrix.append(result)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value_ver = i * n + j
            ver = Graph(value=value_ver)
            graph.add_graph(ver)
    s = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                s = i * n + j
            if i % n == 0:
                neighbors = [(i + 1, j), (i, j - 1), (i, j + 1), (i - n, j), (i + n, j)]
            elif (i + 1) % n == 0:
                neighbors = [(i - 1, j), (i, j - 1), (i, j + 1), (i - n, j), (i + n, j)]
            else:
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - n, j), (i + n, j)]

            ver1 = graph.list[i * n + j]
            for x, y in neighbors:
                if x >= 0 and y >= 0 and x < n * n and y < n:
                    if matrix[i][j] in '.S' and matrix[x][y] in '.S':
                        ver2 = graph.list[x * n + y]
                        ver1: Graph
                        ver1.add_neighbour(ver2)
                        ver2: Graph
                        ver2.add_neighbour(ver1)

    return graph, s


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


n = int(input())

graph, s = create_graf_3d(n)
ver = graph.list[s]
short_path(ver)
path = 1000000
for i in range(n):
    for j in range(n):
        ver = graph.list[i * n + j]
        if ver.dist != 0:
            if path > ver.dist:
                path = ver.dist
print(path)
