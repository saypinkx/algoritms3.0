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


n = int(input())
stack = Stack()
data = str(input()).split()
data = list(map(lambda x: int(x), data))
start_value = 0
for i in range(n):
    van = StackObj(data[i])
    stack.push(van)
    while stack.top is not None and stack.top.value - start_value == 1:
        start_value = stack.top.value
        stack.pop()

if stack.size() == 0:
    print('YES')
else:
    print('NO')







