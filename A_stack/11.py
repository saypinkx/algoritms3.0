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


stack = Stack()
f = open('02.txt', 'r')
file = f.readlines()
n = int(file[0])
for i in range(n):
    string = file[i+1].split()
    k = int(string[0])
    mass = list(map(lambda x: float(x), string[1:k + 1]))
    end = 0
    for new in mass:
        if stack.top is None:
            stack.push(StackObj(new))
        else:
            last = stack.top
            if new <= last.value:
                stack.push(StackObj(new))
            else:
                while last is not None and new > last.value and last.value >= end:
                    end = stack.pop()
                    last = stack.top
                stack.push(StackObj(new))
    while stack.top is not None and stack.top.value >= end:
        end = stack.pop()
    if stack.size() == 0:
        print(1)
    else:
        print(0)
