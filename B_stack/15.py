class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top == None:
            self.top = obj
        else:
            node = self.top
            self.top = obj
            obj.prev = node
        return 'ok'

    def pop(self):
        if self.top != None:
            node = self.top
            self.top = node.prev
            return node.value
        else:
            return 'error'

    def back(self):
        if self.top != None:
            return self.top.value
        else:
            return 'error'

    def size(self):
        if self.top == None:
            return 0
        length = 1
        node = self.top
        while node.prev != None:
            node = node.prev
            length += 1
        return length

    def clear(self):
        self.top = None
        return 'ok'

    def exit(self):
        return 'bye'


class StackObj:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.index = None


n = int(input())
cities = str(input()).split()
cities = list(map(lambda x: int(x), cities))
stack = Stack()
data = []
for i in range(n - 1):
    data.append(-1)
    city = StackObj(cities[i])
    city.index = i
    stack.push(city)
    while stack.top is not None and stack.top.value > cities[i+1]:
        data[stack.top.index] = i + 1
        stack.pop()
data.append(-1)
print(*data)







