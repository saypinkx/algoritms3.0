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
        self.transfer = -1
        self.line = None

    def add_neighbour(self, obj):
        if obj not in self.neighbors:
            self.neighbors.append(obj)

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


def create_graph_metro():
    n = int(input())
    m = int(input())
    graph = GraphList(m)
    for i in range(m):
        line = list(map(int, input().split()))
        line_set = set(line[1::])
        ver = Graph(i + 1)
        ver.line = line_set
        graph.add_graph(ver)
    for i in range(0, m):
        for j in range(i + 1, m):
            ver1: Graph = graph.list[i + 1]
            ver2: Graph = graph.list[j+1]
            set1: set = ver1.line
            set2: set = ver2.line
            if not set1.isdisjoint(set2):
                ver1.add_neighbour(ver2)
                ver2.add_neighbour(ver1)

    return graph


def short_path(graph1, graph2):
    queue = Queue()
    queue.push(QueueOBJ(graph1))
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
    return graph2.is_visited, graph2.dist


graph = create_graph_metro()
start, end = list(map(int, input().split()))
found_start = []
found_end = []
for j in range(1, len(graph.list)):
    i = graph.list[j]
    if start in i.line:
        found_start.append(i)
    if end in i.line:
        found_end.append(i)
result = []
for start in found_start:
    for end in found_end:
        x, y = short_path(start, end)
        if x != 0:
            result.append(y)
    for i in range(1, len(graph.list)):
        ver: Graph = graph.list[i]
        ver.dist = 0
        ver.is_visited =0
if result == []:
    print('-1')
else:
    print(min(result))
